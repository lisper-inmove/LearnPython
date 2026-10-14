"""全测试套件共享的 fixture。

放在这里的 fixture 无需 import，同目录及子目录的测试文件按名字直接引用即可。
"""

from pathlib import Path

import pytest

from learnpython import main


@pytest.fixture(scope="session")
def project_root() -> Path:
    """仓库根目录（tests/ 的上一级）。

    session 作用域：整个测试会话只计算一次，适合放只读的、昂贵的资源。
    """
    return Path(__file__).resolve().parent.parent


@pytest.fixture
def main_output(capsys: pytest.CaptureFixture[str]) -> str:
    """运行 learnpython.main()，返回它写入 stdout 的内容。

    演示 fixture 组合 fixture：这里复用了 pytest 内置的 capsys。
    """
    main()
    return capsys.readouterr().out
