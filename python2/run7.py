import asyncio
from aiogram import Bot, Dispatcher, types

async def start_command(message: types.Message):
    # Sending welcome message
    await message.reply("Welcome to the bot!")
    # Show main menu
    await show_menu(message)

async def show_menu(message: types.Message):
    # Sending main menu options
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Option One"), types.KeyboardButton("Option Two"), types.KeyboardButton("Option Three"))
    await message.reply("Please choose an option:", reply_markup=keyboard)

async def main_menu_command(message: types.Message):
    # Sending main menu options
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Option One"), types.KeyboardButton("Option Two"), types.KeyboardButton("Option Three"))
    await message.reply("Please choose an option:", reply_markup=keyboard)

async def option_two_command(message: types.Message):
    # Sending options for the second menu
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Option One"), types.KeyboardButton("Option Two"), types.KeyboardButton("Option Three"))
    await message.reply("Please choose an option:", reply_markup=keyboard)

async def cancel_command(message: types.Message):
    # Sending cancellation message
    await message.reply("Operation cancelled.")

async def main():
    # Creating a bot instance
    bot = Bot(token="6819049569:AAHdaEjILbHFL7EvMBXh64Io1FAFfLrKC2U", proxy="http://10.111.222.1:8080/")

    # Creating a Dispatcher instance
    dp = Dispatcher(bot)

    # Registering commands
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(main_menu_command, text="Main Menu")
    dp.register_message_handler(option_two_command, text="Option Two")
    dp.register_message_handler(cancel_command, text="Cancel")

    # Starting the bot polling
    await dp.start_polling()

# Running the asyncio main loop
if __name__ == "__main__":
    asyncio.run(main())
