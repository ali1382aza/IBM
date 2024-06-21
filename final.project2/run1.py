import asyncio
from aiogram import Bot, Dispatcher, types
import requests
import aiohttp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor


headers = {'Authorization': f'Token {token}'}

async def start_command(message: types.Message):
    await message.reply("خوش آمدید")
    await show_main_menu(message)


async def show_main_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("آمار بازار"), types.KeyboardButton("اطلاعات کاربر"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)


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
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)


async def tamam_arz(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("به ریال"),types.KeyboardButton("به دلار"))
    keyboard.add(types.KeyboardButton("Back to Menu 1"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)


# async def arz_entekhb(message: types.Message):




async def option_2_command(message: types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("پروفایل کاربر"), types.KeyboardButton("کیف پول"))
    keyboard.add(types.KeyboardButton("لیست تراکنش ها"), types.KeyboardButton("لیست واریزی ها"))
    keyboard.add(types.KeyboardButton("بازار های مورد علاقه"))
    keyboard.add(types.KeyboardButton("Back to Main Menu"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)




#منو تمامی ارز ها
async def usdt_tamam(message: types.Message):
    response = requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    data = response.json()['global']['binance']
    binance_data_str = str(data)
    
    chunk_size = 4096  
    for i in range(0, len(binance_data_str), chunk_size):
        await message.reply(binance_data_str[i:i + chunk_size])


async def rls_tamam(message: types.Message):
    response = requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=rls')
    data = response.json()['global']['binance']
    binance_data_str = str(data)
    
    chunk_size = 4096  
    for i in range(0, len(binance_data_str), chunk_size):
        await message.reply(binance_data_str[i:i + chunk_size])

currencies=['rls','btc','eth','ltc','usdt','xrp','bch','bnb','eos','xlm','etc','trx',
           'pmn','doge','uni','dai','link','dot','aave','ada','shib','ftm','matic',
           'axs','mana','sand','avax','mkr','gmt','usdc']

async def list_arz(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('rls'),types.KeyboardButton('btc'),types.KeyboardButton('eth'))
    keyboard.add(types.KeyboardButton('ltc'),types.KeyboardButton('usdt'),types.KeyboardButton('xrp'))
    keyboard.add(types.KeyboardButton('bch'),types.KeyboardButton('bnb'),types.KeyboardButton('eos'))
    keyboard.add(types.KeyboardButton('xlm'),types.KeyboardButton('etc'),types.KeyboardButton('trx'))
    keyboard.add(types.KeyboardButton('pmn'),types.KeyboardButton('doge'),types.KeyboardButton('uni'))
    keyboard.add(types.KeyboardButton('dai'),types.KeyboardButton('link'),types.KeyboardButton('dot'))
    keyboard.add(types.KeyboardButton('aave'),types.KeyboardButton('ada'),types.KeyboardButton('shib'))
    keyboard.add(types.KeyboardButton('ftm'),types.KeyboardButton('matic'),types.KeyboardButton('axs'))
    keyboard.add(types.KeyboardButton('mana'),types.KeyboardButton('sand'),types.KeyboardButton('avax'))
    keyboard.add(types.KeyboardButton('mkr'),types.KeyboardButton('gmt'),types.KeyboardButton('usdc'))
    keyboard.add(types.KeyboardButton("Back to Main Menu"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)

    
#پروفایل کاربر

async def user_profile(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.nobitex.ir/users/profile', headers=headers) as response:
            data = await response.json()
            await message.reply(data)


#منو کیف پول

async def kif(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("دریافت لیست کیف پول ها"))
    keyboard.add(types.KeyboardButton("نمایش موجودی هر کیف پول"))
    keyboard.add(types.KeyboardButton("نمایش کل موجودی"))
    keyboard.add(types.KeyboardButton("Back to Main Menu"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)



#کیف های پول کاربر

async def list_kif(message: types.Message):
    response = requests.get('https://api.nobitex.ir/users/wallets/list', headers=headers)
    data = response.json()["wallets"]
    binance_data_str = str(data)
    
    chunk_size = 4096  
    for i in range(0, len(binance_data_str), chunk_size):
        await message.reply(binance_data_str[i:i + chunk_size])


#موجودی هر کیف پول
async def mojoodi(message: types.Message):
    response = requests.get('https://api.nobitex.ir/users/wallets/list')
    data = response.json()
    binance_data_str = str(data)
    
    chunk_size = 4096  
    for i in range(0, len(binance_data_str), chunk_size):
        await message.reply(binance_data_str[i:i + chunk_size])


#موجودی کل کیف پول ها
async def mojoodi_kol(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.nobitex.ir/v2/wallets?currencies=rls,btc', headers=headers) as response:
            data = await response.json()
            await message.reply(data)

#لیست تراکنش ها
async def tarakonesh(message: types.Message):
    response = requests.get('https://api.nobitex.ir/users/wallets/transactions/list?wallet=80928448',headers=headers)
    data = response.json()['transactions']
    binance_data_str = str(data)
    
    chunk_size = 4096  
    for i in range(0, len(binance_data_str), chunk_size):
        await message.reply(binance_data_str[i:i + chunk_size])

#منو بازار های مورد علاقه 







#لیست بازار های مورد علاقه
async def usdt_tamam(message: types.Message):
    response = requests.get('https://api.nobitex.ir/users/markets/favorite')
    data = response.json()
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
    dp.register_message_handler(usdt_tamam,text="به دلار")
    dp.register_message_handler(rls_tamam,text="به ریال")
    dp.register_message_handler(list_arz,text="نمایش قیمت ارز انتخابی")

    dp.register_message_handler(kif,text="کیف پول")
    dp.register_message_handler(user_profile,text="پروفایل کاربر")
    dp.register_message_handler(list_kif,text="دریافت لیست کیف پول ها")
    dp.register_message_handler(mojoodi,text="نمایش موجودی هر کیف پول")
    dp.register_message_handler(mojoodi_kol,text="نمایش کل موجودی")
    dp.register_message_handler(tarakonesh,text="لیست تراکنش ها")
    
    await dp.start_polling()

#قیمت ارز انتخابی




if __name__ == "__main__":
    asyncio.run(main())