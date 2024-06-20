import asyncio
from aiogram import Bot, Dispatcher, types

async def start_command(message: types.Message):
    # Sending welcome message
    await message.reply("خوش آمدید")
    # Show main menu
    await show_main_menu(message)

async def show_main_menu(message: types.Message):
    # Showing main menu options
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("آمار بازار"), types.KeyboardButton("اطلاعات کاربر"))
    await message.reply("Please choose an option:", reply_markup=keyboard)

async def back_to_main_menu_command(message: types.Message):
    # Showing main menu options
    await show_main_menu(message)

async def option_1_command(message: types.Message):
    # Showing options for the first menu
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Sub Option 1"), types.KeyboardButton("Sub Option 2"))
    keyboard.add(types.KeyboardButton("Back to Main Menu"))
    await message.reply("Please choose an option:", reply_markup=keyboard)

async def sub_option_1_command(message: types.Message):
    # Sending options for the first sub menu
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Back to Option 1 Menu"))
    await message.reply("Please choose an option:", reply_markup=keyboard)

async def option_2_command(message: types.Message):
    # Showing options for the second menu
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Sub Option 1"), types.KeyboardButton("Sub Option 2"))
    keyboard.add(types.KeyboardButton("Sub Option 3"), types.KeyboardButton("Sub Option 4"), types.KeyboardButton("Sub Option 5"))
    keyboard.add(types.KeyboardButton("Back to Main Menu"))
    await message.reply("Please choose an option:", reply_markup=keyboard)

async def main():
    # Creating a bot instance
    bot = Bot(token="6819049569:AAHdaEjILbHFL7EvMBXh64Io1FAFfLrKC2U", proxy="http://10.111.222.1:8080/")

    # Creating a Dispatcher instance
    dp = Dispatcher(bot)

    # Registering commands
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(show_main_menu, text="Main Menu")
    dp.register_message_handler(back_to_main_menu_command, text="Back to Main Menu")
    dp.register_message_handler(option_1_command, text="آمار بازار")
    dp.register_message_handler(sub_option_1_command, text="Sub Option 1")
    dp.register_message_handler(option_2_command, text="اطلاعات کاربر")

    # Starting the bot polling
    await dp.start_polling()

# Running the asyncio main loop
if __name__ == "__main__":
    asyncio.run(main())

