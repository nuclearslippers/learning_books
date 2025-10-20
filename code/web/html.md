# 初始HTML
HTML（HyperText Markup Language，超文本标记语言）是网页的骨架——用于描述网页的结构和内容。它不是编程语言，而是一种标记语言。

## 基本结构
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>我的第一个网页</title>
  </head>
  <body>
    <h1>你好，世界！</h1>
    <p>这是我的第一个网页。</p>
  </body>
</html>
```

`head`部分存放网站的“元信息”，例如标题、编码、引入CSS/JS。
`body`部分是网页的主要内容部分。

## 常见标签举例
| 标签                       | 作用           | 示例                                            |
| ------------------------ | ------------ | --------------------------------------------- |
| `<h1>` ~ `<h6>`          | 标题（数字越小标题越大） | `<h1>主标题</h1>`                                |
| `<p>`                    | 段落           | `<p>这是一段文字。</p>`                              |
| `<a>`                    | 超链接          | `<a href="https://www.google.com">Google</a>` |
| `<img>`                  | 图片（单标签）      | `<img src="image.jpg" alt="描述">`              |
| `<ul>` / `<ol>` / `<li>` | 列表           | `<ul><li>项目1</li><li>项目2</li></ul>`           |
| `<div>`                  | 区块（常用于布局）    | `<div>内容块</div>`                              |
| `<span>`                 | 行内小块         | `<span>小文字</span>`                            |


## 属性
HTML 标签可以带“属性”，用于提供额外信息。
```html
<a href="https://example.com" target="_blank">访问示例网站</a>
```

## 结合CSS/JS
`<style></style>`用来表示CSS样式 `<script></script>`用来表示JS的行为