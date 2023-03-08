import random
import time
from create_table import create_table, insert_transaction
from transaction import Transaction
from credentials import conn


create_table(conn)

if __name__ == "__main__":
    while True:
        insert_transaction(
            conn,
            Transaction(
                description="test",
                price_kzt=random.randint(1,100),
                quantity=random.randint(1,10),
                amount=0,
                price_usd=0,
            )
        )
        print("inserted")
        time.sleep(1)
