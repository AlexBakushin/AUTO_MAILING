***Auto Mailing***
===

Это веб-приложение на django в котором каждый может зарегистрировать своих клиентов, написать письмо и настроить рассылки.
Затем сайт автоматически отправить запланникованные письма клиентам.
Сайт доступен по локальному адресу `http://127.0.0.1:8000/`

---
**Структура сайта:**
-
На главной странице вас будет встречать главное меню, меню навигации, краткая статистика и небольшое окно со статьями из блога - что являются ссылками на источник.
``Главное меню``
1. `Список рассылок` - там находится список из всех писем записанных на сайте, ваши помеченны галочкой, все можно открыть и просмотреть, ваши - редактировать. Редактировать можно `Тему` и `Тело` письма.
2. `Список клиентов` - список из записанных вам клиентов (получателей), просмотр чужих не предусмотрем! Редактировать клиента можно в любое время. Для записи необходимо ввести електронный адрес клиента.
3. `Список настроек` - список со вмеми настройками рассылок на сайте, ваши помеченны галочкой, все можно открыть и просмотреть, ваши - редактировать. В редактирование входит: `время рассылки` - когда будет произведена рассылка, `периодичность` (раз в день, раз в неделю, раз в месяц), `Клиенты` - список из ваших клиентов, которых можно подключить к рассылке, `Письма` - список из ваших писем, которые будут отправлены клиентам.
4. `Отчет по рассылкам` - таблица с отчетом все произведенных и не произведенных рассылок, ваши отмеченны галочкой. Таблица выводит всю инвормацию по рассылке, если на одну рассылку записано несколько клиентов, то в одной строке будет выведена инвормация о рассылке в столбик по очереди.
5. ``Cписок пользователей`` - только для менеджеров! Представляет собой список зарегистрированных пользователей с возможностью их блокировки.
---
``Меню навигации``
1. `Главная` - возвращает на главную страницу.
2. `Блог` - отрывает под-сайт с блогом.
3. `Профиль - Войти` - Открывает ваш профиль с возможносью редиктирования, если вы не авторизированны - отроет окно авторизации.
4. `Выйти - Зарегистрироваться` - диавторизирут вас с сайта, если не авторизированны - откроет форму регистрации на сайте, при регистрации присылает письмо на введенную электронную почту.
---
``Блог``
Мини-сайт с возможность писать сообщения и прикреплять к ним изображения на стене, также последние 3 поста будут выведены на главной странице основного сайта.

Для начала работы вам необходимо зарегистрироваться на сайте или войти в уже существующий аккаунт.
Далее необходимо создать письмо рассылки и записать клиента.
Затем создать настройку и в ней выбрать время рассылки, периодичность и, ранее записанные письмо(а) и клиента(ов).
Далее приложение проверит время настройки, соглассно которому и будет производится рассылка.
---
Все необходиммые данные стрятанны в переменные окружения!

---
Для запуска локального сервера с приложением предусмотрена команда 
-
````
python manage.py runserver
````

Для запуска рассылки необходимо в консоль ввести команду
-
````
python manage.py runapscheduler
````

---
Для работы программы необходима библиотека `requests`!
-
A также брокер `Redis`!
-

Для быстрой установки зависимостей предусмотрен файл `requirements.txt`.

В терминал вводится команда:
````
pip install -r requirements.txt
````