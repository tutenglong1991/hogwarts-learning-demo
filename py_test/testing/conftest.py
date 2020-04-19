import pprint

import pytest
from _pytest.main import Session


# 自定义case执行顺序，用例设计最好不依赖顺序
def pytest_collection_modifyitems(session: Session, config, items: list):
    # called after collection is completed
    # you can modify the ``items`` list
    # items.reverse()
    session.items = items
