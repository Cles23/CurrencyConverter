# write your code here!
from urllib.request import urlopen
import json

def convert(currency):
    url = 'http://www.floatrates.com/daily/'f'{currency}''.json'
    response = urlopen(url)
    data = json.loads(response.read())
    return data

def main():
    currency = input().lower()
    data = convert(currency)
    cache = {}
    if 'usd' in data:
        cache['usd'] = data['usd']['rate']
    if 'eur' in data:
        cache['eur'] = data['eur']['rate']
    while True:
        currency_2 = input().lower()
        if currency_2 == '':
            break

        currency_amount = float(input())
        if currency_2 in cache:
            print('Checking the cache...')
            print('Oh! It is in the cache!')
            print('You received', round(currency_amount * cache[currency_2], 2), currency_2.upper() + '.')
        else:
            print('Checking the cache...')
            print('Sorry, but it is not in the cache!')
            print('You received', round(currency_amount * data[currency_2]['rate'], 2), currency_2.upper() + '.')
        cache[currency_2] = data[currency_2]['rate']
main()
