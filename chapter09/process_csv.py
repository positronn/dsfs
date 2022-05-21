# process_csv.py

# just generating the data...
with open('tab_delimited_stock_prices.txt', 'w') as f:
    f.write("""6/20/2014\tAAPL\t90.91
6/20/2014\tMSFT\t41.68
6/20/2014\tFB\t64.5
6/19/2014\tAAPL\t91.86
6/19/2014\tMSFT\t41.51
6/19/2014\tFB\t64.34
""")

import csv

def process(date: str, symbol: str, closing_price: float) -> None:
    # Imaginge that this function actually does something.
    assert closing_price > 0.0


with open('tab_delimited_stock_prices.txt', 'r') as f:
    tab_reader = csv.reader(f, delimiter='\t')
    for row in tab_reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)