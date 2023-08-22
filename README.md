# dotmagic

A Python library consists of a set of utilities for managing configuration files.

## Installation

```console
pip install dotmagic
```

### Usage of `Config` Class

The `Config` class is designed to simplify the management of configuration values from various sources, such as `.env` files or dictionaries. It also provides the option to override environment variables with the loaded configuration.

### Importing `Config`

First, import the `Config` class into your Python script:

```python
from dotmagic.config import Config
```

### Creating a `Config` Instance

To use the `Config` class, create an instance of it. You can specify the configuration source (`.env` file or dictionary), default values, and whether to override environment variables.

```python
# Example 1: Load from a .env file
config = Config(".env")

# Example 2: Load from a dictionary
config_data = {
    "PORT": "8080",
    "DEBUG": "True",
}
config = Config(config_data)

# Example 3: Load from a .env file and override environment variables
config = Config(".env", override=True)
```

### Accessing Configuration Values

You can access configuration values using dot notation or dictionary-style indexing.

```python
# Accessing values using dot notation
port = config.PORT
debug = config.DEBUG

# Accessing values using dictionary-style indexing
port = config["PORT"]
debug = config["DEBUG"]
```

### Handling Missing Values

The `Config` class provides a way to handle missing values. If a value is not found and is marked as required, it will raise a `KeyError`. If it's not required, it will return `None`.

```python
try:
    missing_value = config.required.MISSING_KEY  # Raises KeyError
except KeyError:
    print("MISSING_KEY is required but missing.")

missing_value = config.MISSING_KEY  # None
```

### Examples

Here are some examples of using the `Config` class:

```python
# Example 1: Loading from a .env file
config = Config(".env")
port = config.PORT  # Access the PORT value from the .env file

# Example 2: Loading from a dictionary
config_data = {
    "PORT": "8080",
    "DEBUG": "True",
}
config = Config(config_data)
port = config.PORT  # Access the PORT value as an integer (parsed from a string)

# Example 3: Using ConfigParse for parsing configuration values from a dictionary
config_data = {
    "PORT": "8080",
    "DEBUG": "True",
}
config = ConfigParse(config_data)
port = config.PORT  # Access the PORT value as an integer (parsed from a string)
```

The `Config` class simplifies the management of configuration values, making it easy to work with environment variables and configuration files.

### Usage of `dotdict`

`dotdict` is a custom dictionary class that allows you to access its values using dot notation. Here's how you can use it:

```python
# Import the dotdict class
from dotdict import dotdict

# Create a dotdict from a dictionary
my_dict = {"key1": "value1", "key2": "value2"}
dot_dict = dotdict(my_dict)

# Access values using dot notation
value1 = dot_dict.key1  # "value1"
value2 = dot_dict.key2  # "value2"

# You can also access values using dictionary-style indexing
value1 = dot_dict["key1"]  # "value1"
value2 = dot_dict["key2"]  # "value2"
```

### Usage of `seconds`

`seconds` is a function that converts a time string into seconds. Here's how you can use it:

```python
# Import the seconds function
from dotdict import seconds

# Convert time strings to seconds
seconds_in_a_day = seconds("1d")          # 86400
seconds_in_a_day_and_an_hour = seconds("1d1h")     # 90000
seconds_in_a_day_hour_and_minute = seconds("1d1h1m")   # 90060
seconds_in_a_day_hour_minute_and_second = seconds("1d1h1m1s")  # 90061
```

The `seconds` function takes a time string as input and returns the equivalent time duration in seconds. It supports various formats, such as "1d" (1 day), "1d1h" (1 day and 1 hour), "1d1h1m" (1 day, 1 hour, and 1 minute), and "1d1h1m1s" (1 day, 1 hour, 1 minute, and 1 second). If the input time string is invalid, it raises a `ValueError`.

## License

This project is licensed under the terms of the [GNU General Public License v3.0.](./LICENSE)