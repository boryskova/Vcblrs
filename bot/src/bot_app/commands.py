from aiogram import types
from aiogram.dispatcher import FSMContext

from .app import dp, bot
from . import messages


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(messages.WELCOME_MESSAGE)
    await send_menu(message.chat.id)


async def send_menu(chat_id):
    # Create the menu keyboard
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Button 1', 'Button 2')

    # Send the menu with buttons to the user
    await bot.send_message(chat_id, 'Choose an option:', reply_markup=keyboard)


# @dp.message_handler(text='Button 1')
# async def handle_button1_choice(message: Message, state: FSMContext):
#     # Handle the user's choice for Button 1
#     await message.answer('You selected Button 1.')
#
# @dp.message_handler(text='Button 2')
# async def handle_button2_choice(message: Message, state: FSMContext):
#     # Handle the user's choice for Button 2
#     await message.answer('You selected Button 2.')
#
# @dp.message_handler()
# async def handle_other_messages(message: Message, state: FSMContext):
#     # Handle other messages from the user
#     await message.answer('You said: ' + message.text)
