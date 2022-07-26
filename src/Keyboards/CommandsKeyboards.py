from aiogram import types

from Configs import translations


class CommandsKeyboards:
    def __init__(self):
        pass

    def get_main_keyboard(self) -> types.ReplyKeyboardMarkup:
        self.start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        self.start.add(
            types.KeyboardButton(text=translations.get('keyboards.buttons.hi')),
            types.KeyboardButton(text=translations.get('keyboards.buttons.joke')),
            types.KeyboardButton(text=translations.get('keyboards.buttons.another-keyboard')),

            types.KeyboardButton(text=''),
            types.KeyboardButton(text='/settings'),
            types.KeyboardButton(text=''),

            types.KeyboardButton(text=''),
            types.KeyboardButton(text=translations.get('keyboards.buttons.write-to-dev')),
            types.KeyboardButton(text='')
        )

        return self.start
