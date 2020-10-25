import currencies as c
import script as s

def check_base(base):
    if base == 'GBP':
        c.GBP(s.convert_to)
    elif base == 'USD':
        c.USD(s.convert_to)
    elif base == 'EUR':
        c.EUR(s.convert_to)
    elif base == 'HKD':
        c.HKD(s.convert_to)
    elif base == 'IDR':
        c.IDR(s.convert_to)
    elif base == 'ILS':
        c.ILS(s.convert_to)
    elif base == 'DKK':
        c.DKK(s.convert_to)
    elif base == 'INR':
        c.INR(s.convert_to)
    elif base == 'CHF':
        c.CHF(s.convert_to)
    elif base == 'MXN':
        c.MXN(s.convert_to)
    elif base == 'CZK':
        c.CZK(s.convert_to)
    elif base == 'SGD':
        c.SGD(s.convert_to)
    elif base == 'THB':
        c.THB(s.convert_to)
    elif base == 'HRK':
        c.HRK(s.convert_to)
    elif base == 'MYR':
        c.MYR(s.convert_to)
    elif base == 'NOK':
        c.NOK(s.convert_to)
    elif base == 'CNY':
        c.CNY(s.convert_to)
    elif base == 'BGN':
        c.BGN(s.convert_to)
    elif base == 'PHP':
        c.PHP(s.convert_to)
    elif base == 'PLN':
        c.PLN(s.convert_to)
    elif base == 'ZAR':
        c.ZAR(s.convert_to)
    elif base == 'CAD':
        c.CAD(s.convert_to)
    elif base == 'ISK':
        c.ISK(s.convert_to)
    elif base == 'BRL':
        c.BRL(s.convert_to)
    elif base == 'RON':
        c.RON(s.convert_to)
    elif base == 'NZD':
        c.NZD(s.convert_to)
    elif base == 'TRY':
        c.TRY(s.convert_to)
    elif base == 'JPY':
        c.JPY(s.convert_to)
    elif base == 'RUB':
        c.RUB(s.convert_to)
    elif base == 'KRW':
        c.KRW(s.convert_to)
    elif base == 'AUD':
        c.AUD(s.convert_to)
    elif base == 'HUF':
        c.HUF(s.convert_to)
    elif base == 'SEK':
        c.SEK(s.convert_to)
    else:
        print('Please enter a valid currency.')


