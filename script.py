# Description: Currency Converter
# Reza Ghasemi

import check as ch

amount = float(input('* Please enter the amount of money you want to convert:\n'))
base = input('* What is your base currency?\n')
convert_to = input('* What is your target currency?\n')

ch.check_base(base)