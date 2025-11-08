# 前端基础知识

## HTML
1. 常见的代码框架

```html
<!DOCTYPE html>  <!-- 1. 声明文档类型：告诉浏览器这是HTML5文档 -->
<html lang="zh-CN">  <!-- 2. 根标签：所有内容的父容器，lang定义页面语言（zh-CN=中文） -->
  <head>  <!-- 3. 头部：存储页面“元信息”（不直接显示在页面上） -->
    <meta charset="UTF-8">  <!-- 关键元信息：定义字符编码（UTF-8支持所有语言，避免乱码） -->
    <title>我的第一个网页</title>  <!-- 页面标题：显示在浏览器标签栏，SEO核心 -->
    <link rel="stylesheet" href="style.css">  <!-- 引入外部CSS（美化样式） --> 
    <!-- rel 是relationship 代表资源和网页的关系  -->
    <script src="script.js"></script>  <!-- 引入外部JavaScript（交互功能） -->
  </head>
  <body>  <!-- 4. 主体：页面“可见内容”的容器（文字、图片、按钮等都在这里） -->
    <h1>欢迎来到我的网页</h1>  <!-- 一级标题 -->
    <p>这是一个HTML基础示例。</p>  <!-- 段落文本 -->
    <img src="photo.jpg" alt="示例图片">  <!-- 图片 -->
    <div>123</div> <!-- div是通用容器，本身不会产生任何视觉效果。就是用来装其他东西的 -->
  </body>
</html>
```

2. DOM树
DOM 树（Document Object Model Tree，文档对象模型树）是浏览器对 HTML 文档的结构化表示方式，它将 HTML 中的所有元素、属性、文本等都转换为 “节点（Node）”，并通过层级关系（父子、兄弟）组织成树形结构，让编程语言（如 JavaScript）能轻松访问和操作网页内容。

作用： 连接HTML和JS的桥梁


3. 常用长度单位

(1) rem（Root EM）
最常用的单位。是一种相对的单位，相对于根元素（html）的字体大小
默认： 1rem = 16px(浏览器默认的字体大小)

(2) em:相对于当前元素的字体大小
```css
.card {
  font-size: 14px;
  padding: 2em; /* 2 × 14px = 28px */
}
```

(3) vx/vh: 视口宽度/高度的1%
```css
.header {
  height: 10vh; /* 视口高度的10% */
  width: 80vw;  /* 视口宽度的80% */
}
```

(4) px: 像素,固定单位，最基础的单位