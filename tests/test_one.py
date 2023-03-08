from sqlalchemy import create_engine
from transaction import Transaction
from create_table import insert_transaction, create_table, update_price_usd, update_transaction, get_transactions


def test_service1(conn_with_data: str):
     engine = create_engine(conn_with_data)
     conn = engine.connect()

     transaction = Transaction(
         description="test_description",
         price_kzt=100,
         quantity=1000,
         amount=0,
         price_usd=0,
     )
     insert_transaction(conn, transaction)

     transaction = get_transactions(conn)
     assert len(transaction) == 4
     transaction = transaction[-1]
     assert transaction.description == "test_description"

     update_transaction(conn)
     transaction = get_transactions(conn)
     for transaction in transaction:
         assert transaction.price_kzt * transaction.quantity == transaction.amount


