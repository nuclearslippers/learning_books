# VUE框架的基础知识

VUE 是一款用于构建用户界面的 JavaScript 框架。

## 基础文件结构
```plain
my-vue-project/
├── src/ # 源代码目录
│ ├── assets/ # 静态资源
│ │ ├── images/ # 图片资源
│ │ ├── fonts/ # 字体文件
│ │ └── styles/ # 全局样式
│ ├── components/ # 可复用组件
│ │ ├── common/ # 全局通用组件
│ │ ├── business/ # 业务组件
│ │ └── ui/ # UI基础组件
│ ├── App.vue # 根组件
│ └── main.js # 入口文件
├── node_modules/ # 依赖包
├── index.html    # 
├── .env # 环境变量
├── .env.development # 开发环境变量
├── .env.production # 生产环境变量
├── package.json # 项目配置和依赖
├── vue.config.js # Vue CLI配置
├── README.md # 项目说明
└── gitignore # Git忽略配置
```

首先浏览器从 `index.html` 开始页面渲染。一般来说，里面会包含引入 `main.js`。
`main.js` 会导入核心组件 `App.vue` 并且将其挂载到对应的挂载点上（一般来说是 `index.html` 的一个 `<div>` 标签。
`App.vue` 就是最基本的核心组件，是VUE框架提供的脚手架（即有一套新的语言规范，不过类似于HTML，CSS，JS）

## .vue文件的结构
`.vue` 文件一般由三个部分组成。
```plain
<script setup> ... </script>   ← 脚本逻辑部分（定义变量、函数、生命周期）
<template> ... </template>     ← 视图结构部分（HTML模板）
<style scoped> ... </style>    ← 样式部分（CSS）
```

## .vue的一些特性
1. `import Home from './components/Home.vue'`
这是从 `Home.vue` 文件中导入一个Vue对象, 然后命名为 `Home`