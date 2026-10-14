"""脚手架自检：确认包能导入、可编辑安装生效、共享 fixture 可用。"""

import importlib.metadata
from pathlib import Path

import learnpython


def test_package_is_importable() -> None:
    assert learnpython.__name__ == "learnpython"


def test_main_is_callable() -> None:
    assert callable(learnpython.main)


def test_distribution_is_installed() -> None:
    """可编辑安装生效：importlib.metadata 能查到本发行包。

    这条同时验证 src 布局没有配错 —— 若测试是靠 pythonpath 兜底才能导入，
    这里就会失败。
    """
    assert importlib.metadata.version("learnpython")


def test_project_root_fixture_points_at_repo(project_root: Path) -> None:
    assert (project_root / "pyproject.toml").is_file()
