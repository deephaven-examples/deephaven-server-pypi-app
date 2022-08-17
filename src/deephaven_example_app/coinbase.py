import json
import websocket
from deephaven import dtypes, DynamicTableWriter
from deephaven.time import to_datetime


def table_writer(columns):
    writer = DynamicTableWriter(columns)

    def convert(value, column_type):
        if column_type == dtypes.int_:
            return int(value)
        if column_type == dtypes.string:
            return str(value)
        if column_type == dtypes.float_:
            return float(value)
        if column_type == dtypes.DateTime:
            return to_datetime(f"{value[0:-1]} UTC")
        return value

    def map_row(data, columns):
        row = []
        for column_name, column_type in columns.items():
            value = convert(data[column_name], column_type)
            row.append(value)
        return row

    def write_row(s):
        row = map_row(json.loads(s), columns)
        writer.write_row(*row)

    return writer.table, write_row


def matches():
    return table_writer(
        {
            "product_id": dtypes.string,
            "time": dtypes.DateTime,
            "side": dtypes.string,
            "size": dtypes.float_,
            "price": dtypes.float_,
            "type": dtypes.string,
            "trade_id": dtypes.int_,
            "maker_order_id": dtypes.string,
            "taker_order_id": dtypes.string,
            "sequence": dtypes.int_,
        }
    )


def subscribe_matches(ws, product_ids=["BTC-USD", "ETH-USD"]):
    ws.send(
        json.dumps(
            {"type": "subscribe", "product_ids": product_ids, "channels": ["matches"]}
        )
    )
    ws.recv()


def run_matches_loop(consumer):
    ws = websocket.create_connection("wss://ws-feed.exchange.coinbase.com")
    subscribe_matches(ws)
    while True:
        consumer(ws.recv())
