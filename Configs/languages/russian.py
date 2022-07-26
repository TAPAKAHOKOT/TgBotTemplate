translations = {
    'commands': {
        'answers': {
            'start': 'Добро пожаловать, {user_name}!\nЯ - *{bot_name}*, помогу тебе получать уведомления из rocket. Введи /help чтобы получить инструкцию',
            'help': '/help команда',
            'settings': 'Выбери настройку',
            'role': {
                'root': 'Ты босс',
                'admin': 'Ты админ',
                'user': 'Ты пользователь, доступ закрыт((('
            }
        }
    },
    'answers': {
        'dont-understand': "Извините, я не понимаю, нажмите /start или /help"
    },
    'keyboards': {
        'answers': {
            'hello': 'Прив Привет',
            'joke': '<<Смешная шутка>>',
            'another-keyboard': 'Открываю другую клавиатуру',
            'write-to-dev': 'Enter below the message you want to send to the developers',
            'wrote-to-dev': 'Message sent to developers',
            'message-from-user': 'Message from user [ <a href=\'https://t.me/{username}\'>{username}</a> ]:\n\n{message}'
        },
        'buttons': {
            'hi': 'Приу',
            'joke': 'Шутка',
            'another-keyboard': 'Другая клавиатура',
            'write-to-dev': 'Write to the developer📝'
        }
    },
    'callbacks': {
        'answers': {
            'number-value': "Значение номера: {value}",
            'letter-value': "Значение буквы: {value}",
            'choose-language': 'Выбери язык',
            'language-updated-to': 'Язык обновлен на {language}'
        },
        'keyboards': {
            'settings': {
                'language': 'Язык'
            },
            'example': {
                '1': '1',
                '2': '2',
                '3': '3',
                'a': 'А',
                'b': 'Б',
                'c': 'В'
            }
        }
    }
}
