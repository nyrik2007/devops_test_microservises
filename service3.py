import time

from create_table import create_table, update_price_usd
from credentials import conn


create_table(conn)

if __name__ == "__main__":
    while True:
        update_price_usd(conn)
        print("updated")
        time.sleep(20)