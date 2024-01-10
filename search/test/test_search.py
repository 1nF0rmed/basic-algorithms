import pytest
from search.search import Search

@pytest.fixture
def search():
    return Search()

def test_search(search):
    list = [1, 2, 3, 4, 5]
    item = 3
    result = search.search(list, item)
    assert result == 2

