from main import BooksCollector
import pytest
@pytest.fixture # фикстура
def collector():
    collector = BooksCollector()
    return collector