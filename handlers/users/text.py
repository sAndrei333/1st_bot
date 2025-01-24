from aiogram.types import Message
from loader import router
from  aiogram import F

@router.message(F.text =='joke')
async def fun_text(message: Message):
    dice_mess = await message.aswer_dice(emoji='')
    value_dice = dice_mess.dice.value
    if value_dice < 32:
        await message.answer(text='GG, WP')
    else:
        await message.answer(text=f'your money {value_dice}')
