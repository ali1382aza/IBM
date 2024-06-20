import asyncio
from aiogram import Bot, Dispatcher, types
import requests

async def start_command(message: types.Message):
    await message.reply("خوش آمدید")
    await show_main_menu(message)

async def show_main_menu(message: types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("آمار بازار"), types.KeyboardButton("اطلاعات کاربر"))
    await message.reply("Please choose an option:", reply_markup=keyboard)

async def back_to_main_menu_command(message: types.Message):
    
    await show_main_menu(message)

async def option_1_command(message: types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("نمایش قیمت تمامی ارز‌های موجود"), types.KeyboardButton("نمایش قیمت ارز انتخابی"))
    keyboard.add(types.KeyboardButton("Back to Main Menu"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)

async def sub_option_1_command(message: types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Back to Option 1 Menu"))
    await message.reply("Please choose an option:", reply_markup=keyboard)

async def tamam_arz(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("به ریال"),types.KeyboardButton("به دلار"))
    keyboard.add(types.KeyboardButton("Back to Menu 1"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)


async def option_2_command(message: types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Sub Option 1"), types.KeyboardButton("Sub Option 2"))
    keyboard.add(types.KeyboardButton("Sub Option 3"), types.KeyboardButton("Sub Option 4"), types.KeyboardButton("Sub Option 5"))
    keyboard.add(types.KeyboardButton("Back to Main Menu"))
    await message.reply("Please choose an option:", reply_markup=keyboard)

async def usdt_tamam(message: types.Message):
    response = requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    data = response.json()['global']['binance']
    binance_data_str = str(data)
    
    chunk_size = 4096  
    for i in range(0, len(binance_data_str), chunk_size):
        await message.reply(binance_data_str[i:i + chunk_size])
    
async def main():
    
    bot = Bot(token="6819049569:AAHdaEjILbHFL7EvMBXh64Io1FAFfLrKC2U", proxy="http://10.111.222.1:8080/")


    dp = Dispatcher(bot)

    
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(show_main_menu, text="Main Menu")
    dp.register_message_handler(back_to_main_menu_command, text="Back to Main Menu")
    dp.register_message_handler(option_1_command, text="آمار بازار")
    dp.register_message_handler(sub_option_1_command, text="Sub Option 1")
    dp.register_message_handler(option_2_command, text="اطلاعات کاربر")

    dp.register_message_handler(option_1_command, text="Back to Menu 1")
    dp.register_message_handler(tamam_arz,text="نمایش قیمت تمامی ارز‌های موجود")
    dp.register_message_handler(usdt_tamam,text="به ریال")


    
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())