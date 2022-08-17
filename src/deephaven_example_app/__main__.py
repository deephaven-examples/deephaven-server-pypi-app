import deephaven_server


if __name__ == "__main__":
    server = deephaven_server.Server()
    server.start()

    from . import coinbase
    from deephaven import agg
    from deephaven.table import Table

    # Initialize the matches table
    matches_table, matches_writer = coinbase.matches()

    # Create a simple aggregation
    matches_stats = matches_table.update_view(["volume=price*size"]).agg_by(
        [
            agg.count_("count"),
            agg.sum_("volume"),
            agg.last(["time", "last_price=price", "last_size=size"]),
            agg.weighted_avg("size", "avg_price=price"),
        ],
        ["product_id"],
    )

    # Show the most recent rows first
    matches_table = matches_table.reverse()

    print(f"Connect to the Deephaven IDE @ http://localhost:{server.port}/ide/")
    for table_name in [
        name for name, value in globals().items() if isinstance(value, Table)
    ]:
        print(
            f"Connect to {table_name} @ http://localhost:{server.port}/iframe/table/?name={table_name}"
        )

    # Hook up the data source
    coinbase.run_matches_loop(matches_writer)
