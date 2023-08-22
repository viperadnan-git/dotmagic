import unittest

from .config_test import TestConfig, TestConfigParse
from .utils_test import TestDotDict, TestSeconds

__all__ = ["TestConfigParse", "TestConfig", "TestDotDict", "TestSeconds"]

if __name__ == "__main__":
    unittest.main()
