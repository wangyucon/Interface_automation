import pytest

from common.logger import Log


@pytest.fixture(scope='class')
def set_up():
    log = Log()
    log.info("--------接口自动化测试开始------------")
    yield
    log.info("--------接口自动化测试结束------------")

@pytest.fixture(scope="function")
def set_up_function():
    print("----------开始断言处理-------------")
    yield
    print("----------断言结束----------------")
