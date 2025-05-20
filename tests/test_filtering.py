import unittest
from utils.date_utils import is_yesterday, get_yesterday_date

class TestDateFiltering(unittest.TestCase):
    def test_is_yesterday(self):
        date = get_yesterday_date().strftime("%d.%m.")
        assert is_yesterday(date)
    
    def test_is_not_yesterday(self):
        assert not is_yesterday("01.01.")

    def test_invalid_date_format(self):
        assert not is_yesterday("invalid_date")

if __name__ == "__main__":
    unittest.main()