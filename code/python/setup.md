# python包安装相关

`pyproject.toml` 和 `setup.py` 是两个我们经常在构建/安装python包中遇到的文件。他们使我们可以方便的再现作者当时的环境。
两个是新旧时代的配置构建系统。

### setup.py 传统打包方式

1. 常见文件结构，直接抄就完了

```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    author="Xujie",
    description="A demo Python package",
    packages=find_packages(),  # 自动找到所有包含 __init__.py 的包
    install_requires=[
        "numpy>=1.20.0",
        "requests"
    ],
    python_requires=">=3.8",
)
```

2. 常见使用命令

```bash
# 本地以开发模型安装
pip install -e . 
```

### pyproject.toml 现代化配置方法

`.toml` 文件的核心设计理念 : __“比 JSON 更好看，比 YAML 更稳定。”__

1. 常见的文件内容

```python
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
description = "A demo Python package"
authors = [
    {name = "Xujie", email = "xujie@example.com"}
]
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.8"
dependencies = ["numpy>=1.20.0", "requests"]

[project.urls]
"Homepage" = "https://github.com/xujie/my_package"
```

2. 使用

```bash
pip install -e .
```