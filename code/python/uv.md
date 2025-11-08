# uv包管理器

轻量，快速。这就是uv的设计理念

### 安装

1. python环境安装
```bash
pip install uv
```

2. 官方安装方法
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


### 常用指令
| 任务              | conda / pip 用法                      | uv 对应命令                                 |
| --------------- | ----------------------------------- | --------------------------------------- |
| 创建环境            | `conda create -n myenv python=3.10` | `uv venv myenv --python 3.10`           |
| 激活环境            | `conda activate myenv`              | `source myenv/bin/activate`（或 `uv run`） |
| 安装包             | `pip install numpy`                 | `uv add numpy`                          |
| 移除包             | `pip uninstall numpy`               | `uv remove numpy`                       |
| 列出包             | `pip list`                          | `uv pip list`                           |
| 冻结依赖            | `pip freeze > requirements.txt`     | `uv export > requirements.txt`          |
| 锁定依赖（类似 poetry） | 无                                   | `uv lock`                               |
| 执行命令（临时环境）      | `python script.py`                  | `uv run python script.py`               |


### 常见工作流

1. 创建新项目
```bash
mkdir demo && cd demo
uv init
# 等价于
uv init demo
cd demo
```
会生成以下内容：
```text
demo/
├── pyproject.toml
└── main.py
```
2. 创建虚拟环境
创建一个虚拟环境在 `.env` 文件中
```bash
# 指定python version
uv venv --python=3.10
```

3. 添加依赖包
```bash
uv add pandas
```

4. 清理依赖/从头再来
```bash
rm uv.lock
uv sync

# 删除已经安装的包
rm -rf .env/
```