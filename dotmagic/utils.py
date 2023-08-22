import re


class dotdict(dict):
    """
    dotdict is a dictionary that allows you to access its values using dot
    notation.

    Args:
        `dict` (dict): The dictionary to convert to a dotdict.

    Returns:
        dotdict: The dotdict.

    Examples:
        >>> dotdict({"key": "value"})
        {"key": "value"}
        >>> dotdict({"key": "value"}).key
        "value"
        >>> dotdict({"key": "value"})["key"]
        "value"
        >>> dotdict({"key": "value"}).key == dotdict({"key": "value"})["key"]
        True
        >>> dotdict({"key": "value"})["key"] == dotdict({"key": "value"}).key
        True
    """

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    __getitem__ = dict.__getitem__
    __setitem__ = dict.__setitem__
    __delitem__ = dict.__delitem__


def seconds(time_string):
    """
    seconds converts a time string to seconds.

    Args:
        `time_string` (str): The time string to convert.

    Raises:
        ValueError: If the time string is invalid.

    Returns:
        int: The time string in seconds.

    Examples:
        >>> seconds("1d")
        86400
        >>> seconds("1d1h")
        90000
        >>> seconds("1d1h1m")
        90060
        >>> seconds("1d1h1m1s")
        90061
    """
    pattern = r"^(?:(\d+)d)?(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$"
    matches = re.match(pattern, time_string)
    if not matches:
        raise ValueError(
            "Invalid time string. Valid examples: 1d, 1d1h, 1d1h1m, 1d1h1m1s")  # fmt: skip
    days = int(matches.group(1) or 0)
    hours = int(matches.group(2) or 0)
    minutes = int(matches.group(3) or 0)
    seconds = int(matches.group(4) or 0)
    print(days, hours, minutes, seconds)
    total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
    return total_seconds
