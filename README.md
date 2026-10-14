# learnpython

## 环境准备

```bash
uv sync
```

## 运行测试

```bash
uv run pytest
```

只跑单个文件或单个用例：

```bash
uv run pytest tests/test_main.py
uv run pytest tests/test_main.py::test_main_prints_greeting
```

覆盖率配置在 `pyproject.toml` 中，默认每次运行都会打印报告。若嫌输出冗长，可把
`addopts` 里的 `--cov=learnpython --cov-report=term-missing` 去掉，改成按需执行
`uv run pytest --cov=learnpython`。

## 测试结构

| 文件 | 用途 |
| --- | --- |
| `tests/__init__.py` | 把 `tests/` 标记为包，避免同名测试模块互相覆盖 |
| `tests/conftest.py` | 全套件共享的 fixture，无需 import 即可使用 |
| `tests/test_main.py` | 行为测试，文件名与被测模块对应 |
| `tests/test_smoke.py` | 脚手架自检：包可导入、可编辑安装生效 |
