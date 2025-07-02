import traceback

import pytest
from utils.commen import try_back_to_home




# 每个用例开始前打印函数名
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    print(f"\n...正在执行测试用例: {item.nodeid}")


# 每个用例运行完成后处理异常情况
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        print(f"\n❌用例失败: {item.name}，尝试执行恢复逻辑...")
        if call.excinfo:
            exc_type = call.excinfo.type.__name__
            exc_msg = str(call.excinfo.value)
            tb = "".join(traceback.format_exception(call.excinfo.type, call.excinfo.value, call.excinfo.tb))
            print(f"异常类型: {exc_type}")
            print(f"异常信息: {exc_msg}")
            print(f"完整堆栈:\n{tb}")
        try_back_to_home()
