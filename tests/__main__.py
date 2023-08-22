from .config_test import TestConfigParse, TestConfig
from .utils_test import TestDotDict, TestSeconds
import unittest

__all__ = [
    "TestConfigParse",
    "TestConfig",
    "TestDotDict",
    "TestSeconds"
]

if __name__ == '__main__':
    unittest.main()