import csv

todays_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}

with open('comma_delimited_stock_prices.txt', 'w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    for stock, price in todays_prices.items():
        csv_writer.writerow([stock, price])
