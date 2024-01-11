import pytest
import random
from search.binary_search import BinarySearch

@pytest.fixture
def binary_search():
    return BinarySearch()

def test_binary_search(binary_search):
    list = [1, 2, 3, 4, 5]
    item = 3
    result = binary_search.search(list, item)
    assert result == 2

def test_binary_long_array_search(binary_search):
    list = [i for i in range(1, 10000001)]
    item_index = random.randint(0, 9999999)
    item = list[item_index]
    result = binary_search.search(list, item)
    assert result == item_index
