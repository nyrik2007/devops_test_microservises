from sqlalchemy.engine import Connection
from sqlalchemy import text

from transaction import Transaction



def create_table(conn: Connection):
    query ="""
    CREATE TABLE IF NOT EXISTS transactions_konakbayev(
        id SERIAL PRIMARY KEY,
        description VARCHAR(255) NOT NULL,
        price_kzt INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        amount INTEGER,
        price_usd INTEGER,
        created DATE DEFAULT NOW()
        )
        """


    conn.execute(text(query))
    conn.commit()


def insert_transaction(conn: Connection, transaction: Transaction):
    query = """
    INSERT INTO transactions_konakbayev(description, price_kzt, quantity, amount, price_usd)
    VALUES(:description, :price_kzt, :quantity, :amount, :price_usd);
    """
    conn.execute(
        text(query),
        parameters={
            "description": transaction.description,
            "price_kzt": transaction.price_kzt,
            "quantity": transaction.quantity,
            "amount": transaction.amount,
            "price_usd": transaction.price_usd,
        },
    )
    conn.commit()


def update_transaction(conn: Connection):
    query = "UPDATE transactions_konakbayev SET amount= transactions_konakbayev.price_kzt * quantity WHERE amount = 0 "
    conn.execute(text(query))
    conn.commit()

def update_price_usd(conn: Connection):
    query = "UPDATE transactions_konakbayev SET price_usd = amount * 460 WHERE price_usd = 0 "
    conn.execute(text(query))
    conn.commit()

def get_transactions(conn: Connection) -> list[Transaction]:
    query = "SELECT * FROM transactions_konakbayev;"
    print("nice")
    transaction  = conn.execute(text(query)).fetchall()
    print("ddd1")
    return [Transaction(
        id=transaction[0],
        description=transaction[1],
        price_kzt=transaction[2],
        quantity=transaction[3],
        amount=transaction[4],
        price_usd=transaction[5],
        created=transaction[6],
    ) for transaction in transaction]
