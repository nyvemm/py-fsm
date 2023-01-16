
import unittest
from flask_caching import Cache


class TestCache(unittest.TestCase):
    def test_cache_type(self):
        cache = Cache(config={'CACHE_TYPE': 'simple'})
        self.assertEqual(cache.config['CACHE_TYPE'], 'simple')


if __name__ == '__main__':
    unittest.main()
