# deephaven-example-app

This is an example [Deephaven](https://github.com/deephaven/deephaven-core) application
built using the [deephaven-server](https://pypi.org/project/deephaven-server/) PyPi package.

It demonstrates connecting to a real-time data source, performing simple operations on that data,
and presenting the data to the user in the [web UI](https://github.com/deephaven/web-client-ui).

The [Coinbase websocket exchange feed](https://docs.cloud.coinbase.com/exchange/docs/websocket-overview)
was chosen as a data source for this example as it's simple to get up and running. It is not meant to
have exhaustive coverage.


## Requirements
 
 * Python >= 3.7
 * Java >= 11

A [virtual environment](https://docs.python.org/3/tutorial/venv.html) is recommended.


## Quickstart

curl one-liner:

```shell
curl -fsSL https://raw.github.com/deephaven-examples/deephaven-server-pypi-app/main/deephaven-example-app.sh | bash
```

wget one-liner:

```shell
wget https://raw.github.com/deephaven-examples/deephaven-server-pypi-app/main/deephaven-example-app.sh -O - | bash
```

Or more explicitly:

```shell
export JAVA_HOME=/path/to/java_home
source /path/to/venv/bin/activate

pip install deephaven-example-app

python -m deephaven_example_app
```

## Development


```shell
export JAVA_HOME=/path/to/java_home
source /path/to/dev-venv/bin/activate

pip install -e .

python -m deephaven_example_app
```
