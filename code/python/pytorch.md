# pytorch相关的学习笔记

## DataLoader
PyTorch的DataLoader是一个用于加载数据的重要方法。
```python
from torch.utils.data import DataLoader
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
```
DataLoader要求输入的数据集是一个PyTorch的Dataset对象。并且实现__getitem__和__len__方法。