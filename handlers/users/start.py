

from aiogram.filters import Command
from aiogram.types import Message
from loader import router
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_start
from loader import router, cursor, con

@router.message(Command('start'))
async def fun_start(message: Message):
    id_user = message.chat.id


    builder = ReplyKeyboardBuilder()
    if id_user in con:
        cursor.execute('SELECT id FROM id_money WHERE id=(?) )',[id_user])
    else:
        cursor.execute('INSERT INTO id_money (id) VALUES (?)', [id_user])
        con.commit()
    for button in kb_start:
        builder.add(button)
    builder.adjust(1)

    await message.answer(text='hi', reply_markup=builder.as_markup(resize_keyboard=True))