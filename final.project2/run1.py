import asyncio
from aiogram import Bot, Dispatcher, types
import requests
import aiohttp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import json



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
    keyboard.add(types.KeyboardButton("برگشت به منو اصلی"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)


async def sub_option_1_command(message: types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("برگشت به منو اصلی"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)


async def tamam_arz(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("به ریال"),types.KeyboardButton("به دلار"))
    keyboard.add(types.KeyboardButton("برگشت به منو اصلی"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)


# async def arz_entekhb(message: types.Message):




async def option_2_command(message: types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("پروفایل کاربر"), types.KeyboardButton("کیف پول"))
    keyboard.add(types.KeyboardButton("لیست تراکنش ها"), types.KeyboardButton("لیست واریزی ها"))
    keyboard.add(types.KeyboardButton("بازار های مورد علاقه"))
    keyboard.add(types.KeyboardButton("برگشت به منو اصلی"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)




#منو تمامی ارز ها
async def usdt_tamam(message: types.Message):
    
    response = requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    data = response.json()['global']['binance']
    formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
    binance_data_str = str(formatted_data)
    
    chunk_size = 4096
    for i in range(0, len(binance_data_str), chunk_size):
        await message.reply(binance_data_str[i:i + chunk_size])


async def rls_tamam(message: types.Message):
    response = requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=rls')
    data = response.json()['global']['binance']
    formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
    binance_data_str = str(formatted_data)
    
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
    keyboard.add(types.KeyboardButton("برگشت به منو اصلی"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)



#پروفایل کاربر

async def user_profile(message: types.Message):
    data=requests.get('https://api.nobitex.ir/users/profile', headers=headers)
    data2=data.json()
    formatted_data = json.dumps(data2, indent=4, ensure_ascii=False)
    await message.reply(formatted_data)


#منو کیف پول

async def kif(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("دریافت لیست کیف پول ها"))
    keyboard.add(types.KeyboardButton("نمایش موجودی هر کیف پول"))
    keyboard.add(types.KeyboardButton("نمایش کل موجودی"))
    keyboard.add(types.KeyboardButton("برگشت به منو اصلی"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)



#کیف های پول کاربر

async def list_kif(message: types.Message):
    response = requests.get('https://api.nobitex.ir/users/wallets/list', headers=headers)
    data = response.json().get("wallets", [])
        
        
    formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
        
    chunk_size = 4096  
    for i in range(0, len(formatted_data), chunk_size):
        await message.reply(formatted_data[i:i + chunk_size])
    


#موجودی هر کیف پول
async def mojoodi(message: types.Message):
    response = requests.get('https://api.nobitex.ir/users/wallets/list', headers=headers)
    data = response.json()

    wallets = data.get('wallets', [])
    response_message = "موجودی کیف پول‌ها:\n"
    for wallet in wallets:
        currency = wallet.get('currency', 'Unknown')
        balance = wallet.get('balance', 'Unknown')
        response_message += f"{currency}: {balance}\n"

    await message.reply(response_message)


#موجودی کل کیف پول ها

async def mojoodi_kol(message: types.Message):
    
    response = requests.get('https://api.nobitex.ir/users/wallets/list', headers=headers)
    data = response.json()
    
    wallets = data.get('wallets', [])
    
    total_balance = sum(float(wallet.get('balance', '0')) for wallet in wallets)
    
    await message.reply(f"موجودی کل کیف پول‌ها: {total_balance}")



#لیست تراکنش ها
async def tarakonesh(message: types.Message):
    response = requests.get('https://api.nobitex.ir/users/wallets/transactions/list?wallet=80928448',headers=headers)
    data = response.json()['transactions']
    binance_data_str = str(data)
    
    chunk_size = 4096  
    for i in range(0, len(binance_data_str), chunk_size):
        await message.reply(f'transactions for wallet(80928448):{binance_data_str[i:i + chunk_size]}')

#لیست واریزی ها
async def variz(message: types.Message):
    response = requests.get('https://api.nobitex.ir/users/wallets/deposits/list?wallet=80928448',headers=headers)
    data = response.json()['deposits']
    binance_data_str = str(data)
    
    chunk_size = 4096  
    for i in range(0, len(binance_data_str), chunk_size):
        await message.reply(f'deposits for wallet(80928448):{binance_data_str[i:i + chunk_size]}')

#منو بازار های مورد علاقه 
async def menu_bazar(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("لیست بازار های مورد علاقه"))
    keyboard.add(types.KeyboardButton("اضافه کردن بازار مورد علاقه"))
    keyboard.add(types.KeyboardButton("حذف بازار مورد علاقه"))
    keyboard.add(types.KeyboardButton("برگشت به منو اصلی"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)



#لیست بازار های مورد علاقه
async def favorite_list(message: types.Message):
    response = requests.get('https://api.nobitex.ir/users/markets/favorite',headers=headers)
    data = response.json()["favoriteMarkets"]
    binance_data_str = str(data)

    chunk_size = 4096  
    for i in range(0, len(binance_data_str), chunk_size):
        await message.reply(binance_data_str[i:i + chunk_size])



#قیمت ارز ها 
async def btc(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def rls(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=rls&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=rls&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def eth(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=eth&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=eth&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def ltc(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=ltc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=ltc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def usdt(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=usdt&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=usdt&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def xrp(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def btc(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def btc(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def btc(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def btc(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def btc(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def btc(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def btc(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def rls(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=rls&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=rls&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def eth(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=eth&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=eth&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def ltc(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=ltc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=ltc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def usdt(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=usdt&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=usdt&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def xrp(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def bch(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=bch&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=bch&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def bnb(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=bnb&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=bnb&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def eos(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=eos&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=eos&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def xlm(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=xlm&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=xlm&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def etc(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=etc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=etc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def trx(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=trx&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=trx&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def pmn(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=pmn&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=pmn&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def doge(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=doge&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=doge&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def uni(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=uni&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=uni&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def dai(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=dai&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=dai&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def link(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=link&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=link&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def dot(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=dot&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=dot&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def aave(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=aave&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=aave&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def pmn(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=pmn&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=pmn&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def doge(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=doge&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=doge&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def uni(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=uni&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=uni&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def dai(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=dai&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=dai&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def link(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=link&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=link&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def dot(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=dot&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=dot&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def aave(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=aave&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=aave&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def ada(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=ada&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=ada&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def shib(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=shib&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=shib&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def ftm(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=ftm&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=ftm&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def matic(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=matic&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=matic&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def axs(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=axs&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=axs&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def mana(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=mana&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=mana&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def sand(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=sand&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=sand&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def avax(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=avax&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=avax&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def mkr(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=mkr&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=mkr&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def gmt(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=gmt&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=gmt&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")

async def usdc(message: types.Message):
    response= requests.get('https://api.nobitex.ir/market/stats?srcCurrency=usdc&dstCurrency=usdt')
    response2 =requests.get('https://api.nobitex.ir/market/stats?srcCurrency=usdc&dstCurrency=rls')
    datai = response.json()['stats']
    datai2 = response2.json()['stats']
    data = json.dumps(datai, indent=4, ensure_ascii=False)
    data2 = json.dumps(datai2, indent=4, ensure_ascii=False)
    await message.reply(f"usdt:{data}\n\nrial:{data2}")


# ثبت بازار های مورد علاقه
async def list_arz2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('BTCIRT ثبت'),types.KeyboardButton('ETHIRT ثبت'))
    keyboard.add(types.KeyboardButton('LTCIRT ثبت'),types.KeyboardButton('USDTIRT ثبت'))
    keyboard.add(types.KeyboardButton('XRPIRT ثبت'),types.KeyboardButton('BCHIRT ثبت'))
    keyboard.add(types.KeyboardButton('BTCUSDT ثبت'),types.KeyboardButton('ETHUSDT ثبت'))
    keyboard.add(types.KeyboardButton('LTCUSDT ثبت'),types.KeyboardButton('XRPUSDT ثبت'))
    keyboard.add(types.KeyboardButton('BCHUSDT ثبت'),types.KeyboardButton('BNBUSDT ثبت'))
    keyboard.add(types.KeyboardButton("برگشت به منو اصلی"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)


#حذف بازار های مورد علاقه
async def list_arz3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('BTCIRT حذف'),types.KeyboardButton('ETHIRT حذف'))
    keyboard.add(types.KeyboardButton('LTCIRT حذف'),types.KeyboardButton('USDTIRT حذف'))
    keyboard.add(types.KeyboardButton('XRPIRT حذف'),types.KeyboardButton('BCHIRT حذف'))
    keyboard.add(types.KeyboardButton('BTCUSDT حذف'),types.KeyboardButton('ETHUSDT حذف'))
    keyboard.add(types.KeyboardButton('LTCUSDT حذف'),types.KeyboardButton('XRPUSDT حذف'))
    keyboard.add(types.KeyboardButton('BCHUSDT حذف'),types.KeyboardButton('BNBUSDT حذف'))
    keyboard.add(types.KeyboardButton("برگشت به منو اصلی"))
    await message.reply("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard)




async def BTCIRT_s(message: types.Message):
    url='https://api.nobitex.ir/users/markets/favorite'
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        await message.reply("عملیات ثبت با موفیقت انجام شد")
        
    else:
        await message.reply("عملیات ثبت با شکست مواجه شد")



async def BTCIRT_d(message: types.Message):
    url='https://api.nobitex.ir/users/markets/favorite'
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        await message.reply("عملیات حذف با موفیقت انجام شد")
        
    else:
        await message.reply("عملیات حذف با شکست مواجه شد")




async def main():
    bot = Bot(token="6819049569:AAHdaEjILbHFL7EvMBXh64Io1FAFfLrKC2U")
    dp = Dispatcher(bot)


    
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(show_main_menu, text="Main Menu")
    dp.register_message_handler(back_to_main_menu_command, text="برگشت به منو اصلی")
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
    dp.register_message_handler(variz,text="لیست واریزی ها")
    
    dp.register_message_handler(favorite_list,text="لیست بازار های مورد علاقه")
    dp.register_message_handler(list_arz2,text="اضافه کردن بازار مورد علاقه")
    dp.register_message_handler(list_arz3,text="حذف بازار مورد علاقه")


    dp.register_message_handler(btc,text="btc")
    dp.register_message_handler(rls,text="rls")
    dp.register_message_handler(eth,text="eth")
    dp.register_message_handler(ltc,text="ltc")
    dp.register_message_handler(usdt,text="usdt")
    dp.register_message_handler(xrp,text="xrp")
    dp.register_message_handler(bch,text="bch")
    dp.register_message_handler(bnb,text="bnb")
    dp.register_message_handler(eos,text="eos")
    dp.register_message_handler(xlm,text="xlm")
    dp.register_message_handler(etc,text="etc")
    dp.register_message_handler(trx,text="trx")
    dp.register_message_handler(pmn,text="pmn")
    dp.register_message_handler(doge,text="doge")
    dp.register_message_handler(uni,text="uni")
    dp.register_message_handler(dai,text="dai")
    dp.register_message_handler(link,text="link")
    dp.register_message_handler(dot,text="dot")
    dp.register_message_handler(aave,text="aave")
    dp.register_message_handler(ada,text="ada")
    dp.register_message_handler(shib,text="shib")
    dp.register_message_handler(ftm,text="ftm")
    dp.register_message_handler(matic,text="matic")
    dp.register_message_handler(axs,text="axs")
    dp.register_message_handler(mana,text="mana")
    dp.register_message_handler(sand,text="sand")
    dp.register_message_handler(avax,text="avax")
    dp.register_message_handler(mkr,text="mkr")
    dp.register_message_handler(gmt,text="gmt")
    dp.register_message_handler(usdc,text="usdc")

    dp.register_message_handler(menu_bazar,text="بازار های مورد علاقه")
    dp.register_message_handler(BTCIRT_s,text="BTCIRT ثبت")
    dp.register_message_handler(BTCIRT_d,text='BTCIRT حذف')

    await dp.start_polling()






if __name__ == "__main__":
    asyncio.run(main())