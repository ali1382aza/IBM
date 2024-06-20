import requests

response = requests.get('https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt')
token = 'd416a76ad6af5d4997aaffb78b802585636bf2f5'
htt = 'https://api.nobitex.ir/users/profile'

headers = {
    'Authorization': f'Token {token}'
}

response2 = requests.get(htt,headers=headers)




data = response.json()['global']['binance']
#print(data)

data2 = response2.json()

print(data2)