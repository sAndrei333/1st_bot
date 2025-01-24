from aiogram import  types
kb_start = [
    types.KeyboardButtom(text='play!'),
    types.KeyboardButtom(texrt='menu')


]
kb_game = [
    types.KeyboardButton(text='stavka 10$', calback_data='bet_10'),
    types.KeyboardButton(text='stavka 20$', calback_data='bet_20'),
    types.KeyboardButton(text='stavka 50$', calback_data='bet_50'),
    types.KeyboardButton(text='stavka 100$', calback_data='bet_100'),
]