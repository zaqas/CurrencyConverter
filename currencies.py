import requests
import script as sc

# US Dollar (USD)
def USD(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=USD').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Euro (EUR)
def EUR(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=EUR').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# British Pound (GBP)
def GBP(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=GBP').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Hong Kong Dollar (HKD)
def HKD(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=HKD').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Indonesian Rupiah (IDR)
def IDR(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=IDR').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Israeli Shekel (ILS)
def ILS(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=ILS').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Danish Krone (DKK)
def DKK(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=DKK').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Indian Rupee (INR)
def INR(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=INR').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Swiss Franc (CHF)
def CHF(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=CHF').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Mexican Peso (MXN)
def MXN(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=MXN').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Czech Koruna (CZK)
def CZK(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=CZK').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Singapore Dollar (SGD)
def SGD(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=SGD').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Thai Baht (THB)
def THB(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=THB').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Croatian Kuna (HRK)
def HRK(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=HRK').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Malaysian Ringgit (MYR)
def MYR(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=MYR').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Norwegian Krone (NOK)
def NOK(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=NOK').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Chinese Yuan (CNY)
def CNY(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=CNY').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Bulgarian Lev (BGN)
def BGN(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=BGN').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Philippine Peso (PHP)
def PHP(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=PHP').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Polish Zloty (PLN)
def PLN(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=PLN').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# South African Rand (ZAR)
def ZAR(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=ZAR').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Canadian Dollar (CAD)
def CAD(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=CAD').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Icelandic Krona (ISK)
def ISK(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=ISK').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Brasilian Real (BRL)
def BRL(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=BRL').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Romanian Leu (RON)
def RON(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=RON').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# New Zealand Dollar (NZD)
def NZD(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=NZD').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Turkish Lira (TRY)
def TRY(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=TRY').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Japanese Yen (JPY)
def JPY(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=JPY').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Russian Rouble (RUB)
def RUB(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=RUB').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# South Korean Won (KRW)
def KRW(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=KRW').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Australian Dollar (AUD)
def AUD(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=AUD').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Hungarian Forint (HUF)
def HUF(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=HUF').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)


# Swedish Krona (SEK)
def SEK(convert_to):
    result = requests.get('https://api.openrates.io/latest?base=SEK').json()
    conversion = result['rates']
    value = conversion.get(convert_to)
    currencies = list(conversion.keys())
    for currency in currencies:
        if currency == convert_to:
            print(sc.amount * value)
