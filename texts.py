# your_lang = 'Это твой язык'

def generate_confirmation_msg(name):
    return f"{name} - так будет называться Ваша команда. Уверены?"

help_message = """По всем вопросам обращайтесь к координаторам в мастер-локации."""

no_code_enter = 'Вы вошли не по коду'

welcome = """С днём шахтёра!
QR-квест состоит из 7 локаций с заданиями.
Выполняйте задания в локациях, пишите ответы в чат-бот и повышайте уровень веселья своей
команды."""

enter_team_name = "Готовы? Напишите название своей команды."

enter_another_name = "Хорошо, введите другое имя для вашей команды."

succes_registrated = "Отлично! Ваша команда зарегистрирована. Чтобы начать QR-квест, нажмите на кнопку ⤵"

map_instruction = """Это карта с локациями QR-квеста. Порядок прохождения локаций указан в вашем маршрутном листе.
Двигайтесь строго по указанному маршруту."""

route_header = "Маршрут вашей команды:"

route_instruction = 'Чтобы приступить к выполнению задания, нажмите на кнопку с названием локации.'

task1 = """Угадайте ингредиенты коктейля и напишите сюда ваши ответы.
Важно: каждый ингредиент необходимо прислать отдельным сообщением!"""

task2 = """Сканируйте QR-код, чтобы узнать задание. Напишите сюда ваши ответы.
Важно: каждый ответ необходимо прислать отдельным сообщением!"""

task3 = """Украсьте шахтерскую каску росписью и отправьте мне фотографию каски."""
task3_2 = """Какая красивая каска! Я в восторге! Вы можете оставить её себе или подарить шахтёрам в Якутии.
Что вы выберете?"""

task4 = """Сканируйте QR-код, чтобы узнать задание. Задание проверит координатор в мастер-локации."""

task5 = """Сканируйте QR-код, чтобы узнать задание. Напишите сюда ваши ответы.
Важно: каждый ответ необходимо прислать отдельным сообщением!"""



ask_for_points = 'Напишите результат команды в этом задании.'

already_answered = 'Уже было.'

wrong_answer = 'Ответ неверный.'

confirm_task_finish = 'Вы уверены, что хотите закончить? Позже вы не сможете вернуться к этому заданию.'

use_kb = 'Используйте клавиатуру.'

correct_ans_header = 'Верно!'

task_already_completed = 'Задание уже пройдено'

send_photo = "Присылайне фото"

number_expected = 'Вводите число'





task1_ans = {'МЯТА': '1',
             'ЛАЙМ': '2',
             'СИРОП БУЗИНЫ': '3', 
             'БУЗИНА': '3', 
             'СОДОВАЯ' : '4',
             'ПРОСЕККО': '5', 
             'ПРОСЕКО': '5', 
             'ПРОССЕКО':'5', 
             'PROSECCO': '5'}

task2_ans = {'ГЛУХАРЬ': '1',
             'БУРАТИНО': '2',
             'БОЧКА': '3',
             'БАБА ЯГА': '4',
             'БАБА-ЯГА': '4',
             'ТАБЛЕТКА': '5',
             'БАРАН': '6',
             'ВЕРБЛЮД': '7',
             'КАРАНДАШ': '8',
             'КОРЖ': '9',
             'СЛОН': '10',}

task5_ans = {'ОТ КРИВОГО КОПРА НЕ ЖДИ ДОБРА': '1',
             'МНОГО УГЛЯ ДОБЫВАТЬ БОЛЬШЕ ХЛЕБА ЖЕВАТЬ': '2',
             'КТО ЛОВКО МАШИНОЙ ВЛАДЕЕТ ТОТ ЛЮБОЙ ПЛАСТ ОДОЛЕЕТ': '3',
             'ЗАКОН ШАХТЁРСКИЙ НЕ ЗАБУДЬ СТЫДИСЬ РАБОТАТЬ КАК-НИБУДЬ': '4',
             'ЗАЗНАЙКА И БЮРОКРАТ ШАХТЁРУ НЕ БРАТ': '5',
             'ГОРНЯЦКАЯ ДРУЖБА КРЕПКА НЕ ЛЕСТЬЮ А ПРАВДОЙ И ЧЕСТЬЮ': '6',
             'С НОВОЙ ТЕХНИКОЙ ШАХТЁРУ ЛЕГЧЕ УГОЛЬ СЛАТЬ НА ГОРУ': '7',
             'НИЧЕГО ЧТО ЛИЦО В ПЫЛИ БЫЛА БЫ ДУША ЧИСТОЙ': '8',
             'УГОЛЁК ЧТО ЗОЛОТО И БЛЕСТИТ И ЦЕНИТСЯ': '9',
             'НЕ ТОТ УГОЛЬ ЧТО В ЗАБОЕ А ТОТ ЧТО В ЭШЕЛОНЕ': '10',}


begin_quest_btn = "Начать QR-квест"
yes_btn = 'Да'
no_btn = 'Нет'
places_btns = ['Коктейли', 'Послание в бутылке',
               'Роспись касок', 'Фотодобыча', 
               'Числошифры', 'Танцевальный баттл', 'Подарки']
finish_task_btn = 'Закончить'
send_helmet_btn = "Отправить фото каски"
give_helmet_btn = "Подарим шахтёрам"
take_helmet_btn = "Оставим себе"
task_completed_btn = 'Задание выполнено'


