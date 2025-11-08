# Tailwindcss 基础知识

Tailwind CSS 是实用优先的 CSS 框架，核心是通过预设类名直接写在 HTML 中实现样式，无需单独写 CSS 文件。
```html
<div class="flex">
    content
</div>
```
核心逻辑：将 CSS 属性封装成类名，比如 `color: red` 对应 `text-red-500`，`margin-top: 2rem` 对应 `mt-8`。

## 基础常见的类型

#### 1. 布局与盒模型
- **容器与对齐**
  - `container`：固定宽度容器（自动居中）
  - `mx-auto`：水平自动边距（居中）
  - `flex`：启用弹性布局
  - `grid`：启用网格布局
- **尺寸控制**
  - 宽度：`w-0` 到 `w-96`（步长 4px）、`w-full`（100%）、`w-screen`（屏幕宽度）
  - 高度：`h-0` 到 `h-96`、`h-full`（100%）、`h-screen`（屏幕高度）
  - 最小/最大：`min-w-xx`、`max-w-xx`、`min-h-xx`、`max-h-xx`
- **边距与内边距**
  - 外边距：`m-0` 到 `m-24`（步长 4px），方向细分 `mt-xx`（上）、`mr-xx`（右）、`mb-xx`（下）、`ml-xx`（左）、`mx-xx`（水平）、`my-xx`（垂直）
  - 内边距：`p-0` 到 `p-24`，方向细分 `pt-xx`、`pr-xx`、`pb-xx`、`pl-xx`、`px-xx`（水平）、`py-xx`（垂直）
- **弹性布局细节**
  - 主轴对齐：`justify-start`、`justify-center`、`justify-end`、`justify-between`、`justify-around`
  - 交叉轴对齐：`items-start`、`items-center`、`items-end`、`items-baseline`、`items-stretch`
  - 方向：`flex-row`（默认横向）、`flex-col`（纵向）、`flex-row-reverse`、`flex-col-reverse`

#### 2. 文字样式
- **字体大小**：`text-xs`（12px）、`text-sm`（14px）、`text-base`（16px）、`text-lg`（18px）、`text-xl`（20px）、`text-2xl` 到 `text-9xl`（逐级增大）
- **颜色**：`text-颜色-权重`，如 `text-gray-500`、`text-blue-600`、`text-red-400`（颜色支持：gray/red/orange/yellow/green/blue/purple/pink 等，权重 100-900）
- **对齐与换行**：`text-left`、`text-center`、`text-right`、`text-justify`；`whitespace-nowrap`（不换行）、`truncate`（单行溢出省略）、`break-words`（单词内换行）
- **字体属性**：
  - 粗细：`font-light`（300）、`font-normal`（400）、`font-medium`（500）、`font-semibold`（600）、`font-bold`（700）、`font-black`（900）
  - 样式：`italic`（斜体）、`not-italic`（正常）
  - 装饰：`underline`（下划线）、`line-through`（删除线）、`no-underline`（无装饰）

#### 3. 背景与边框
- **背景**：
  - 颜色：`bg-颜色-权重`，如 `bg-gray-100`、`bg-blue-500`
  - 透明度：`bg-opacity-0` 到 `bg-opacity-100`（百分比透明度）
  - 图片：`bg-cover`（覆盖）、`bg-contain`（包含）、`bg-center`（居中）
- **边框**：
  - 宽度：`border-0`、`border`（1px）、`border-2`、`border-4`、`border-8`；方向细分 `border-t-xx`（上）、`border-r-xx`（右）等
  - 颜色：`border-颜色-权重`，如 `border-red-300`、`border-gray-400`
  - 圆角：`rounded-sm`、`rounded`、`rounded-md`、`rounded-lg`、`rounded-xl`、`rounded-2xl`、`rounded-full`（圆形）；方向细分 `rounded-tl-xx`（左上）等
- **阴影**：`shadow-sm`、`shadow`、`shadow-md`、`shadow-lg`、`shadow-xl`、`shadow-2xl`、`shadow-inner`（内阴影）

#### 4. 交互与显示
- **显示状态**：`block`、`inline`、`inline-block`、`hidden`（隐藏）、`opacity-0` 到 `opacity-100`（透明度）
- **鼠标交互**：
  - 光标：`cursor-pointer`（手型）、`cursor-default`（默认）、`cursor-not-allowed`（禁止）
  - 状态伪类：`hover:xxx`（悬停）、`focus:xxx`（聚焦）、`active:xxx`（点击）、`disabled:xxx`（禁用）
  - 示例：`hover:bg-blue-600`、`focus:outline-none`、`active:scale-95`
- **变换与过渡**：
  - 缩放：`scale-90`、`scale-100`、`scale-110`
  - 过渡：`transition`（默认过渡）、`transition-colors`（仅颜色过渡）、`duration-300`（过渡时长）

#### 5. 响应式常用
- **断点前缀**（移动优先，从小到大）：
  - `sm:`：≥640px（小屏幕）
  - `md:`：≥768px（中等屏幕）
  - `lg:`：≥1024px（大屏幕）
  - `xl:`：≥1280px（超大屏幕）
  - `2xl:`：≥1536px（特大屏幕）
- **示例**：
  - `sm:text-base md:text-lg`（小屏基础字体，中屏放大）
  - `flex flex-col md:flex-row`（默认纵向排列，中屏横向）
  - `hidden md:block`（小屏隐藏，中屏显示）