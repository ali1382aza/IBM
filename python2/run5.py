import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
#from aiogram.utils import executor
from aiogram.client.session.aiohttp import AiohttpSession

# توکن ربات خود را اینجا قرار دهید
API_TOKEN = '6819049569:AAHdaEjILbHFL7EvMBXh64Io1FAFfLrKC2U'

session = AiohttpSession(proxy="http://10.111.222.1:8080/")
bot = Bot(token=API_TOKEN, session=session)

# تنظیمات لاگینگ
logging.basicConfig(level=logging.INFO)

# ایجاد نمونه‌های Bot و Dispatcher

dp = Dispatcher()

# ایجاد دکمه‌ها
button1 = KeyboardButton('b1')
button2 = KeyboardButton('b2')
button3 = KeyboardButton('b3')
button4 = KeyboardButton('b4')
button5 = KeyboardButton('b5')
button6 = KeyboardButton('b6')
back_button = KeyboardButton('back')

# دکمه‌های زیرمنوی گزینه 2
sub_button1 = KeyboardButton('bb1')
sub_button2 = KeyboardButton('bb2')
sub_back_button = KeyboardButton('back')

# منو اصلی
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(button1, button2, button3, button4, button5, button6)

# منو با دکمه بازگشت
back_menu = ReplyKeyboardMarkup(resize_keyboard=True)
back_menu.add(back_button)

# زیرمنوی گزینه 2
submenu = ReplyKeyboardMarkup(resize_keyboard=True)
submenu.add(sub_button1, sub_button2, sub_back_button)

# هندلر برای فرمان /start
@dp.message_handler(Command("start"))
async def send_welcome(message: Message):
    await message.answer("hi,please", reply_markup=main_menu)

# هندلر برای گزینه‌های منو
@dp.message_handler(lambda message: message.text in ['b1', 'b2', 'b3', 'b4', 'b5', 'b6'])
async def handle_option(message: Message):
    if message.text == 'b2':
        await message.answer("شما گزینه ۲ را انتخاب کردید. یکی از زیرگزینه‌ها را انتخاب کنید:", reply_markup=submenu)
    else:
        await message.answer(f"شما {message.text} را انتخاب کردید. برای بازگشت، دکمه بازگشت را بزنید.", reply_markup=back_menu)

# هندلر برای زیرمنوی گزینه 2
@dp.message_handler(lambda message: message.text in ['زیرگزینه ۱', 'زیرگزینه ۲'])
async def handle_sub_option(message: Message):
    await message.answer(f"شما {message.text} را انتخاب کردید. برای بازگشت، دکمه بازگشت به منوی اصلی را بزنید.", reply_markup=submenu)

# هندلر برای بازگشت به منو اصلی از زیرمنوی گزینه 2
@dp.message_handler(lambda message: message.text == 'بازگشت به منوی اصلی')
async def handle_sub_back(message: Message):
    await message.answer("بازگشت به منو اصلی. یکی از گزینه‌ها را انتخاب کنید:", reply_markup=main_menu)

# هندلر برای بازگشت به منو اصلی از منوی بازگشت
@dp.message_handler(lambda message: message.text == 'بازگشت')
async def handle_back(message: Message):
    await message.answer("بازگشت به منو اصلی. یکی از گزینه‌ها را انتخاب کنید:", reply_markup=main_menu)

# راه‌اندازی ربات
if __name__ == '__main__':
    dp.run_polling(bot)
