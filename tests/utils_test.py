import unittest

from src.utils import dotdict, seconds


class TestDotDict(unittest.TestCase):
    def test_dot_access(self):
        data = {"key": "value", "nested": {"nested_key": "nested_value"}}
        dot_data = dotdict(data)

        self.assertEqual(dot_data.key, "value")
        self.assertEqual(dot_data.nested["nested_key"], "nested_value")

    def test_bracket_access(self):
        data = {"key": "value", "nested": {"nested_key": "nested_value"}}
        dot_data = dotdict(data)

        self.assertEqual(dot_data["key"], "value")
        self.assertEqual(dot_data["nested"]["nested_key"], "nested_value")

    def test_equality(self):
        data1 = {"key": "value"}
        data2 = {"key": "value"}
        dot_data1 = dotdict(data1)
        dot_data2 = dotdict(data2)

        self.assertEqual(dot_data1.key, dot_data2.key)


class TestSeconds(unittest.TestCase):
    def test_valid_time_strings(self):
        self.assertEqual(seconds("1d"), 86400)
        self.assertEqual(seconds("1d1h"), 90000)
        self.assertEqual(seconds("1d1h1m"), 90060)
        self.assertEqual(seconds("1d1h1m1s"), 90061)

    def test_invalid_time_strings(self):
        with self.assertRaises(ValueError):
            seconds("1d1x")  # Invalid character 'x'
        with self.assertRaises(ValueError):
            seconds("1d1h1m1s1x")  # Invalid character 'x'
        with self.assertRaises(ValueError):
            seconds("1dd1h")  # Duplicate 'd'
        with self.assertRaises(ValueError):
            seconds("1h1h")  # Duplicate 'h'
        with self.assertRaises(ValueError):
            seconds("1m1m")  # Duplicate 'm'
        with self.assertRaises(ValueError):
            seconds("1s1s")  # Duplicate 's'
        with self.assertRaises(ValueError):
            seconds("1d1h1m1s1s")  # Duplicate 's' at the end


if __name__ == "__main__":
    unittest.main()
