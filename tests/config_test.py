import unittest

from src.config import ConfigParse, Config

class TestConfigParse(unittest.TestCase):

    def test_get_attribute(self):
        config = ConfigParse({"PORT": "8080"})
        self.assertEqual(config.PORT, 8080)

    def test_get_item(self):
        config = ConfigParse({"PORT": "8080"})
        self.assertEqual(config["PORT"], 8080)

    def test_missing_value_required(self):
        config = ConfigParse({}, required=True)
        with self.assertRaises(KeyError):
            port = config.PORT

    def test_missing_value_not_required(self):
        config = ConfigParse({})
        self.assertIsNone(config.PORT)

    def test_str_representation(self):
        config = ConfigParse({"PORT": "8080"})
        self.assertEqual(str(config), "{'PORT': '8080'}")

    def test_contains(self):
        config = ConfigParse({"PORT": "8080"})
        self.assertIn("PORT", config)
        self.assertNotIn("HOST", config)


class TestConfig(unittest.TestCase):

    def test_loading_from_dict(self):
        config = Config(config={"PORT": "8080"})
        self.assertEqual(config.PORT, 8080)

    def test_loading_from_env_file(self):
        # Assuming a test .env file exists with "PORT=8080"
        config = Config(config="tests/.env.test")
        self.assertEqual(config.PORT, 8080)

    def test_loading_with_override(self):
        # Assuming a test .env file exists with "PORT=8080" and "DATABASE_URL=sqlite://test.db"
        config = Config(config="tests/.env.test", override=True)
        self.assertEqual(config.PORT, 8080)
        self.assertEqual(config.DATABASE_URL, "sqlite://test.db")

    def test_loading_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            config = Config(config=".nonexistent_env_file")

    def test_loading_invalid_config_type(self):
        with self.assertRaises(TypeError):
            config = Config(config=123)

if __name__ == '__main__':
    unittest.main()