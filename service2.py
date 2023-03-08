import time
from create_table import create_table, update_transaction
from credentials import conn


create_table(conn)

if __name__ == "__main__":
    while True:
        update_transaction(conn)
        print("updated")
        time.sleep(20)
