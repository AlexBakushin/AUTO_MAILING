import logging
import pytz
from datetime import datetime, timedelta
from django.conf import settings
from django.utils import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from django.core.mail import send_mail

from main.models import Logs, Settings

logger = logging.getLogger(__name__)


def my_job():
    timezone.activate('UTC')
    today = datetime.now()
    moscow_tz = pytz.timezone('UTC')
    today = today.astimezone(moscow_tz)
    mail_settings = Settings.objects.all()
    result = ''

    for setting in mail_settings:
        if today >= setting.time and setting.status == 'created' and setting.frequency == 'once_a_day':
            for client in setting.client.all():
                result = send_mail(
                    subject=setting.massage.head,
                    message=setting.massage.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.mail],
                )
            setting.time = datetime.now().astimezone(moscow_tz) + timedelta(days=1)
            setting.save()
            Logs.objects.create(datatime=datetime.now().astimezone(moscow_tz), status='finish', response=result)
        elif today >= setting.time and setting.status and setting.frequency == 'once_a_week':
            for client in setting.client.all():
                send_mail(
                    subject=setting.massage.head,
                    message=setting.massage.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.mail],

                )
            setting.time = datetime.now().astimezone(moscow_tz) + timedelta(days=7)
            setting.save()
            Logs.objects.create(datatime=datetime.now().astimezone(moscow_tz), status='finish', response=result)
        elif today >= setting.time and setting.status and setting.frequency == 'once_a_month':
            for client in setting.client.all():
                send_mail(
                    subject=setting.massage.head,
                    message=setting.massage.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.mail],
                )
            setting.time = datetime.now().astimezone(moscow_tz) + timedelta(days=30)
            setting.save()
            Logs.objects.create(datatime=datetime.now().astimezone(moscow_tz), status='finish', response=result)


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),
            id="my_job",
            max_instances=1,
            replace_existing=True,
        )
        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()
