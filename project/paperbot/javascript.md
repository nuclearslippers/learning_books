# 初识JavaScript
JavaScript是为网页添加动态交互功能的核心编程语言，它让网页从静态内容变为能响应操作的应用。
## 基本语法和变量
1. JS有 `let` 可变变量， `const` 不可变变量之分。（还有一个`var`，但不推荐使用）
2. 语句的结尾需要分号。
```JS
let x = 10;       // 可变变量
const name = "Alice"; // 常量
```

## 数据类型
```JS
let a = 10;         // Number（整型/浮点统一）
let b = 3.14;
let c = "hello";    // String
let d = true;       // Boolean
let e = [1,2,3];    // Array
let f = {x:1};      // Object
```

1. JS 中 `Number` 类型既表示整数也表示浮点数
2. 字典在 JS 中叫 `Object`


## 条件语句和循环
```JS
if (x > 0) {
    console.log("positive");
} else {
    console.log("non-positive");
}

for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

1. JS 用 `{}` 包围代码块
2. 打印用 `console.log()`

## 函数定义
```JS
function add(a, b) {
    return a + b;
}

// ES6 箭头函数
const add2 = (a, b) => a + b;

console.log(add(2,3));
console.log(add2(2,3));
```
1. 箭头函数 `(a, b) => a+b` 会继承外层 `this`，常用于回调。


## 其他重要特性
1. 动态数据类型
```JS
let x = 10;  // 现在是 Number
x = "hello"; // 变成 String
```

2. 异步编程
JS 是事件驱动的语言，常用 回调、Promise 和 async/await。

3. 对象与原型链
JS 的对象继承是基于原型（prototype），不是类继承（Python 主要是类继承）。

主要是由于两者类使用时候的区别。python定义类，然后创建实例，继承是发生在创建类的时候。而JS直接在定义实例的时候就完成了继承（它建立变量是不需要提前定义类的）。

```JS
// JavaScript
// 父对象
const animal = {
  eats: true,
  walk() {
    console.log("Animal walks");
  }
};

// 子对象继承自父对象
const rabbit = {
  jumps: true,
  __proto__: animal  // 设置原型链
};

console.log(rabbit.eats); // true - 从原型继承
rabbit.walk(); // "Animal walks" - 从原型继承
```

```Python
# python
# 父类
class Animal:
    def __init__(self):
        self.eats = True
    
    def walk(self):
        print("Animal walks")

# 子类继承父类
class Rabbit(Animal):
    def __init__(self):
        super().__init__()
        self.jumps = True

rabbit = Rabbit()
print(rabbit.eats)  # True - 从父类继承
rabbit.walk()       # "Animal walks" - 从父类继承
```


4. 作用域与闭包（Closure）
JS 的闭包很重要，常用于保存函数内部状态。
闭包其实就是给一些变量设置了特别的属性，外部无法直接进行修改，而是需要使用提供的特殊接口进行修改。
一般来说，闭包的实现就是通过函数（类）内部再设置一个函数（类），然后返回内部的那个类。

```JS
function createPerson(name) {
  let privateAge = 0; // 类似于私有变量

  return {
    getName: () => name,
    getAge: () => privateAge,
    setAge: (newAge) => { 
      if (newAge > 0) privateAge = newAge; 
    },
    celebrateBirthday: () => {
      privateAge++;
      console.log(`Happy Birthday, ${name}! You are ${privateAge}.`);
    }
  };
}

const john = createPerson("John");
console.log(john.getName()); // "John"
john.setAge(30);
john.celebrateBirthday(); // "Happy Birthday, John! You are 31."
// 外部无法直接修改 privateAge 和 name，只能通过提供的方法
```
