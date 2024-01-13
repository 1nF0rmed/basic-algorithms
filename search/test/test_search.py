import pytest
import random
from search.search import Search

@pytest.fixture
def search():
    return Search()

def test_search(search):
    list = [1, 2, 3, 4, 5]
    item = 3
    result = search.search(list, item)
    assert result == 2

def test_unsorted_search(search):
    list = [5, 2, 1, 4, 3]
    item = 4
    result = search.search(list, item)
    assert result == 3

def test_long_array_search(search):
    list = [i for i in range(1, 10000001)]
    random.shuffle(list)
    item_index = random.randint(0, 9999999)
    item = list[item_index]
    result = search.search(list, item)
    assert result == item_index

def test_array_search_time(search):
    list = [i for i in range(1, 100000001)]
    item_index = random.randint(0, 99999999)
    item = list[item_index]
    import time
    start_time = time.time()
    result = search.search(list, item)
    end_time = time.time()
    assert result == item_index
    assert end_time - start_time <= 1
