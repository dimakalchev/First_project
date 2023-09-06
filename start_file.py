import time

import price_monitoring
from price_monitoring import Monitoring
from price_monitoring import book
# print(price_monitoring.myvar)
# print(price_monitoring.mydiet.loc[[0, 2]])
# print(price_monitoring.df2)

with Monitoring() as bot:
    bot.land_first_page()
    bot.filtres()
    bot.create_book()
    bot.take_data()

time.sleep(300)