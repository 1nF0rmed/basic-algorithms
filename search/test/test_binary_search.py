import pytest
from search.binary_search import BinarySearch

@pytest.fixture
def binary_search():
    return BinarySearch()

def test_binary_search(binary_search):
    list = [1, 2, 3, 4, 5]
    item = 3
    result = binary_search.search(list, item)
    assert result == 2
