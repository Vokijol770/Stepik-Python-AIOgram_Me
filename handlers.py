from aiogram.types import Message
from data import dp
from filters import custom_filter_3


async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )

dp.message.register(send_echo, custom_filter_3)