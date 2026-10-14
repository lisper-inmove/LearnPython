"""learnpython.main 的行为测试。"""

from learnpython import main


def test_main_prints_greeting(main_output: str) -> None:
    """main() 向 stdout 打印问候语。"""
    assert main_output == "Hello from learnpython!\n"


def test_main_returns_none(capsys) -> None:
    """main() 是脚本入口，不返回值。"""
    assert main() is None
