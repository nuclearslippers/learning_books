# 补充知识

1. URL规则 - '?'分割符
```url
http://127.0.0.1:8000/items/5?q=runoob
```
`?`: 路径和查询参数之间的分隔符

2. Pydantic模型
Pydantic 是一个用于数据验证和序列化的 Python 模型库。
它在 FastAPI 中广泛使用，用于定义请求体、响应体和其他数据模型，提供了强大的类型检查和自动文档生成功能。

（1） 在FASTAPI使用过程中，可用用它定义数据类型，然后自动进行数据验证。
（2） 此外，pydantic的另外一个重要的功能就是它可以自动生成FASTAPI交互文档

3. Query 查询声明
```python
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/items/")
def read_item(item: Item, q: str = Query(..., max_length=10)):
    return {"item": item, "q": q}
```

这里`q: str = Query(..., max_length=10)` 中的 `=` 并不是赋值的意思，而是一种声明。告诉FASTAPI这个参数的检查规则（长度不能超过10）