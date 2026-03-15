---
theme: apple-basic
title: 正则表达式（Regex）速学与练习
layout: intro
mdc: true
---

<style>
.regex-example {
  margin: 1rem 0;
  border: 1px solid #e5e7eb;
  padding: 0.8rem 1rem;
  border-radius: 6px;
  font-size: 1.5em;
  line-height: 1;
  white-space: pre-wrap;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}

.regex-example p {
  margin: 0;
}

.regex-pattern {
  margin: 1rem 0 0;
  padding: 0.7rem 0.9rem;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  background: #f1f5f9;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 1.15em;
}

.regex-pattern code {
  background: transparent;
  font-size: inherit;
}

.regex-swap {
  display: grid;
}

.regex-swap > * {
  grid-area: 1 / 1;
}

.match {
  background: #fae100;
  border-radius: 0.15em;
}
</style>

# 正则表达式（Regex）速学

## 东亚小孩版本

根据正则表达式，把匹配到的部分标出来

<div class="regex-example regex-swap">Regular Expression</div>

<div class="regex-pattern">Expression</div>

---
layout: default
---

# 基础匹配 Basic Matchers

<div class="regex-example regex-swap">
  <div v-click.hide>“Every man takes the limits of his own field of vision for the limits of the world.”</div>
  <div v-after>“Every man takes the limits <span class="match">of</span> his own field <span class="match">of</span> vision for the limits <span class="match">of</span> the world.”</div>
</div>

<div class="regex-pattern"><code>of</code></div>


普通字符默认按字面值匹配，所以 `of` 会匹配文本里连续出现的 `o` 和 `f`。

---
layout: default
---

# 通配符 The Full Stop `.`

`.` 匹配任意单个字符。  
换行除外，除非额外开单行模式。

<div class="regex-example regex-swap">
  <div v-click.hide>az AZ 09 \_- = !? ., :;</div>
  <div v-after><span class="match">az&nbsp;AZ&nbsp;09&nbsp;\_-&nbsp;=&nbsp;!?&nbsp;.,&nbsp;:;</span></div>
</div>

<div class="regex-pattern"><code>.</code></div>

*点哥写小作文不换行。*


`.` 默认匹配任意单个字符，但通常不匹配换行符；它一次只匹配一个位置上的一个字符。

---
layout: default
---

# 字符集 Character Set `[]`

匹配集合里的任一单字符。

<div class="regex-example regex-swap">
  <div v-click.hide>beer deer feer</div>
  <div v-after><span class="match">beer</span> <span class="match">deer</span> <span class="match">feer</span></div>
</div>

<div class="regex-pattern"><code>[bdf]eer</code></div>


`[]` 表示字符集，会从括号里的候选字符中任选一个来匹配当前位置。

---
layout: default
---

# 取反字符集 Negated Character Set `[^ ]`

匹配不在集合中的单字符。

<div class="regex-example regex-swap">
  <div v-click.hide>bear beor beer beur</div>
  <div v-after><span class="match">bear</span> beor <span class="match">beer</span> beur</div>
</div>

<div class="regex-pattern"><code>be[^ou]r</code></div>


`[^...]` 表示取反字符集，会匹配任何一个“不在集合里”的单字符。

---
layout: default
---

# 字母范围 Character Range `[g-k]`

<div class="regex-example regex-swap">
  <div v-click.hide>abcdefghijklmnopqrstuvwxyz</div>
  <div v-after>abcdef<span class="match">ghijk</span>lmnopqrstuvwxyz</div>
</div>

<div class="regex-pattern"><code>[g-k]</code></div>


在字符集里，`-` 可以表示范围，所以 `[g-k]` 会匹配从 `g` 到 `k` 的任意一个字符。

---
layout: default
---

# 重复量词 Zero or More `*`

<div class="regex-example regex-swap">
  <div v-click.hide>dp dep deep</div>
  <div v-after><span class="match">dp</span> <span class="match">dep</span> <span class="match">deep</span></div>
</div>

<div class="regex-pattern"><code>de*p</code></div>

*星星一闪一闪，忽隐忽现，时长时短。*


`*` 表示前一个字符或前一个分组可以出现 0 次、1 次或多次，所以 `e*` 可以没有，也可以重复很多次。

---
layout: default
---

# 重复量词 One or More `+`

<div class="regex-example regex-swap">
  <div v-click.hide>dp dep deep</div>
  <div v-after>dp <span class="match">dep</span> <span class="match">deep</span></div>
</div>

<div class="regex-pattern"><code>de+p</code></div>


`+` 表示前一个字符或前一个分组至少出现 1 次，因此不能没有，只能出现一次或多次。

---
layout: default
---

# 重复量词 Optional `?`

<div class="regex-example regex-swap">
  <div v-click.hide>a an</div>
  <div v-after><span class="match">a</span> <span class="match">an</span></div>
</div>

<div class="regex-pattern"><code>an?</code></div>


`?` 表示前一个字符或前一个分组最多出现 1 次，也就是“有或没有都可以”，但不能重复多次。

---
layout: default
---

# 量词 Exact Quantifier `{n}`

<div class="regex-example regex-swap">
  <div v-click.hide>Release 10/9/2021</div>
  <div v-after>Release 10/9/<span class="match">2021</span></div>
</div>

<div class="regex-pattern"><code>[0-9]{4}</code></div>


`{n}` 表示前一个字符类或分组必须恰好重复 `n` 次，所以这里要求正好是 4 位数字。

---
layout: default
---

# 量词 Open-Ended Quantifier `{n,}`

<div class="regex-example regex-swap">
  <div v-click.hide>Release 10/9/2021</div>
  <div v-after>Release <span class="match">10</span>/9/<span class="match">2021</span></div>
</div>

<div class="regex-pattern"><code>[0-9]{2,}</code></div>


`{n,}` 表示前一个字符类或分组至少重复 `n` 次，没有上限，所以这里匹配 2 位及以上的数字串。

---
layout: default
---

# 量词 Range Quantifier `{m,n}`

<div class="regex-example regex-swap">
  <div v-click.hide>Release 10/9/2021</div>
  <div v-after>Release <span class="match">10</span>/<span class="match">9</span>/<span class="match">2021</span></div>
</div>

<div class="regex-pattern"><code>[0-9]{1,4}</code></div>


`{m,n}` 表示前一个字符类或分组重复次数在 `m` 到 `n` 之间，包含边界值。

---
layout: default
---

# 分组 Grouping `( )`

把一段模式整体视为一个单元。

<div class="regex-example regex-swap">
  <div v-click.hide>ha-ha,haa-haa</div>
  <div v-after>ha-ha,<span class="match">haa</span>-<span class="match">haa</span></div>
</div>

<div class="regex-pattern"><code>(haa)</code></div>


`()` 会把一段模式当成一个整体，后续量词、捕获和引用都可以作用在这个整体上。

---
layout: default
---

# Group 作用 1：结构化匹配 Structural Grouping

- 用 `()` 把一段模式包起来后，这段模式就能作为整体处理。
- 这样量词作用的是整组，不是前面那一个字符。

例子：

<div class="regex-pattern"><code>(ab)+</code></div>

它匹配：

- `ab`
- `abab`
- `ababab`

如果没有括号，`ab+` 的意思就完全变了。


分组最基础的作用是改变结构边界，让“重复谁、组合谁”这件事变得明确。

---
layout: default
---

# Group 作用 2：捕获匹配内容 Capturing Group

- 默认括号是捕获分组。
- 它会把匹配到的内容记下来，方便后续复用。

例子：

<div class="regex-pattern"><code>(\d{4})-(\d{2})-(\d{2})</code></div>

匹配 `2025-08-10` 时会捕获：

1. `2025`
2. `08`
3. `10`

替换时可以写成：

<div class="regex-pattern"><code>$3/$2/$1</code></div>


捕获分组会把每个括号匹配到的内容按顺序编号保存，后续可以在替换或反向引用中再次使用。

---
layout: default
---

# 反向引用 Backreference `\1`

<div class="regex-example regex-swap">
  <div v-click.hide>ha-ha,haa-haa</div>
  <div v-after><span class="match">ha-ha,haa-</span>haa</div>
</div>

<div class="regex-pattern"><code>(ha)-\1,(haa)-</code></div>


`\1` 表示“重复第 1 个捕获分组之前匹配到的内容”，所以它引用的不是模式本身，而是已经捕获到的结果。

---
layout: default
---

# 反向引用 Backreference `\2`

<div class="regex-example regex-swap">
  <div v-click.hide>ha-ha,haa-haa</div>
  <div v-after><span class="match">ha-ha,haa-haa</span></div>
</div>

<div class="regex-pattern"><code>(ha)-\1,(haa)-\2</code></div>


`\2` 表示引用第 2 个捕获分组的内容；分组编号按左括号出现的顺序从左到右计算。

---
layout: default
---

# Python 示例 Python Example for Backreference `\2`

```python
import re

text = "ha-ha,haa-haa"
pattern = r"(ha)-\1,(haa)-\2"

match = re.search(pattern, text)

print(match.group(0))  # ha-ha,haa-haa
print(match.group(1))  # ha
print(match.group(2))  # haa
```

- 第 1 对括号 `(ha)` 是 group 1，所以 `\1` 要求后面再出现一次 `ha`
- 第 2 对括号 `(haa)` 是 group 2，所以 `\2` 要求后面再出现一次 `haa`

在 Python 的 `re` 里，最好把模式写成 raw string，也就是 `r"..."`；这样 `\1` 和 `\2` 会按正则里的反向引用来解释，而不是被 Python 字符串先处理掉。

---
layout: default
---

# 非捕获分组 Non-capturing Group `(?: )`

不需要后续引用时，用它减少开销。

<div class="regex-example regex-swap">
  <div v-click.hide>ha-ha,haa-haa</div>
  <div v-after><span class="match">ha-ha,haa-haa</span></div>
</div>

<div class="regex-pattern"><code>(?:ha)-ha,(haa)-\1</code></div>


`(?:...)` 仍然能把模式作为整体分组，但不会为它分配捕获编号，适合只想分组、不想保存内容的场景。

---
layout: default
---

# Group 作用 3：控制优先级 Precedence Control

- `|` 的优先级很低，常常需要括号限制范围。
- 不加括号时，意思很容易跑偏。

例子：

<div class="regex-pattern"><code>gr(a|e)y</code></div>

它匹配：

- `gray`
- `grey`


括号还可以明确运算范围，避免 `|` 等低优先级操作符把表达式拆错位置。

---
layout: default
---

# 选择 Alternation `|` vs 字符集 Character Set `[]`

<div class="regex-example regex-swap">
  <div v-click.hide>cat rat dog</div>
  <div v-after><span class="match">cat</span> <span class="match">rat</span> <span class="match">dog</span></div>
</div>

<div class="regex-pattern"><code>(c|r)at|dog</code></div>

- `|` 在子表达式之间做选择
- `[]` 在单字符之间做选择


`|` 用来在多个完整子表达式之间二选一或多选一，而 `[]` 只在“单个字符”层面做选择。

---
layout: default
---

# 转义 Escaping `\`

需要匹配元字符本身：  
`{ } [ ] / \ + * . $ ^ | ?`

<div class="regex-example regex-swap">
  <div v-click.hide>(\*) Asterisk.</div>
  <div v-after>(<span class="match">\*</span>) Asterisk<span class="match">.</span></div>
</div>

<div class="regex-pattern"><code>(\*|\.)</code></div>


反斜杠 `\` 可以把元字符转成字面字符来匹配，例如 `\*` 匹配星号本身，`\.` 匹配句点本身。

---
layout: default
---

# 行首 Start Anchor `^`

<div class="regex-example regex-swap">
  <div v-click.hide>1. 3 eggs, beaten<br>2. 1 tsp sunflower oil</div>
  <div v-after><span class="match">1</span>. 3 eggs, beaten<br><span class="match">2</span>. 1 tsp sunflower oil</div>
</div>

<div class="regex-pattern"><code>^[0-9]</code></div>

*在外出头，在家逆反。*


`^` 在方括号外时表示行首或字符串开头，所以 `^[0-9]` 的意思是“从每一行最前面找数字”。

---
layout: default
---

# 行尾 End Anchor `$`

<div class="regex-example regex-swap">
  <div v-click.hide>domain.com/what-is-html.html<br>otherdomain.com/html-elements<br>website.com/html5-features.html</div>
  <div v-after>domain.com/what-is-html.<span class="match">html</span><br>otherdomain.com/html-elements<br>website.com/html5-features.<span class="match">html</span></div>
</div>

<div class="regex-pattern"><code>html$</code></div>

*到头来还是钱。*


`$` 表示行尾或字符串结尾，所以 `html$` 只会匹配那些以 `html` 结束的位置。

---
layout: default
---

# 单词字符 Word Character `\w`

<div class="regex-example regex-swap">
  <div v-click.hide>abcABC123 \_.:!?</div>
  <div v-after><span class="match">abcABC123</span> \<span class="match">_</span>.:!?</div>
</div>

<div class="regex-pattern"><code>\w</code></div>


`\w` 通常表示字母、数字和下划线这三类“单词字符”的并集。

---
layout: default
---

# 非单词字符 Non-word Character `\W`

<div class="regex-example regex-swap">
  <div v-click.hide>abcABC123 \_.:!?</div>
  <div v-after>abcABC123<span class="match">&nbsp;</span><span class="match">\</span>_<span class="match">.:!?</span></div>
</div>

<div class="regex-pattern"><code>\W</code></div>

*人长大了成了和小时候相反的人，丢了底线，多了人和人之间的空间。*


`\W` 表示非单词字符，也就是不属于字母、数字、下划线这一类的字符；空格和标点通常都属于 `\W`。

---
layout: default
---

# 数字字符 Digit Character `\d`

<div class="regex-example regex-swap">
  <div v-click.hide>abcABC123 \_.:!?</div>
  <div v-after>abcABC<span class="match">123</span> \_.:!?</div>
</div>

<div class="regex-pattern"><code>\d+</code></div>


`\d` 表示数字字符，通常等价于 `[0-9]`；这里的 `+` 表示连续匹配一个或多个数字。

---
layout: default
---

# 非数字字符 Non-digit Character `\D`

<div class="regex-example regex-swap">
  <div v-click.hide>abcABC123 \_.:!?</div>
  <div v-after><span class="match">abcABC</span>123<span class="match">&nbsp;\_.:!?</span></div>
</div>

<div class="regex-pattern"><code>\D+</code></div>


`\D` 表示任何非数字字符，也就是不属于 `[0-9]` 的字符。

---
layout: default
---

# 空白字符 Whitespace Character `\s`

<div class="regex-example regex-swap">
  <div v-click.hide>abcABC123 \_.:!?</div>
  <div v-after>abcABC123<span class="match">&nbsp;</span>\_.:!?</div>
</div>

<div class="regex-pattern"><code>\s</code></div>


`\s` 表示空白字符，通常包括空格、制表符和换行等空白分隔符。

---
layout: default
---

# 非空白字符 Non-whitespace Character `\S`

<div class="regex-example regex-swap">
  <div v-click.hide>abcABC123 \_.:!?</div>
  <div v-after><span class="match">abcABC123</span> <span class="match">\_.:!?</span></div>
</div>

<div class="regex-pattern"><code>\S+</code></div>


`\S` 表示非空白字符，也就是除了空格、制表符、换行等空白分隔符之外的字符。

---
layout: default
---

# Lookaround 概念 Lookaround Overview

四种：

- `(?=...)`
- `(?!...)`
- `(?<=...)`
- `(?<!...)`


Lookaround 是一类“断言”，只检查某个位置左右两边是否满足条件，本身不消耗字符。

---
layout: default
---

# 正向先行 Positive Lookahead `(?=...)`

<div class="regex-example regex-swap">
  <div v-click.hide>Date: 4 Aug 3PM</div>
  <div v-after>Date: 4 Aug <span class="match">3</span>PM</div>
</div>

<div class="regex-pattern"><code>\d+(?=PM)</code></div>

*别问，问就是向前看。*


`(?=...)` 是正向先行断言，要求当前位置右边必须满足某个模式，但断言本身不消耗字符，所以真正返回的仍然是前面的匹配结果。

---
layout: default
---

# 负向先行 Negative Lookahead `(?!...)`

<div class="regex-example regex-swap">
  <div v-click.hide>Date: 4 Aug 3PM</div>
  <div v-after>Date: <span class="match">4</span> Aug 3PM</div>
</div>

<div class="regex-pattern"><code>\d+(?!PM)</code></div>


`(?!...)` 是负向先行断言，要求当前位置右边不能满足某个模式；断言本身不消耗字符。

---
layout: default
---

# 正向后顾 Positive Lookbehind `(?<=...)`

<div class="regex-example regex-swap">
  <div v-click.hide>Product Code: 1064 Price: $5</div>
  <div v-after>Product Code: 1064 Price: $<span class="match">5</span></div>
</div>

<div class="regex-pattern"><code>(?&lt;=\$)\d+</code></div>


`(?<=...)` 是正向后顾断言，要求当前位置左边必须满足某个模式；这里要求数字前面必须是 `$`。

---
layout: default
---

# 负向后顾 Negative Lookbehind `(?<!...)`

<div class="regex-example regex-swap">
  <div v-click.hide>Product Code: 1064 Price: $5</div>
  <div v-after>Product Code: <span class="match">1064</span> Price: $5</div>
</div>

<div class="regex-pattern"><code>(?&lt;!\$)\d+</code></div>

*匹配前面不是 `$` 的数字。*


`(?<!...)` 是负向后顾断言，要求当前位置左边不能满足某个模式；这里表示数字前面不能是 `$`。

---
layout: default
---

# Flag 概念 Flags Overview

修改匹配模式的开关。


Flags 是附加在正则表达式后面的模式开关，用来改变匹配范围、大小写规则或锚点行为。

---
layout: default
---

# 全局 flag Global Flag `g`

<div class="regex-example regex-swap">
  <div v-click.hide>domain.com, test.com, site.com</div>
  <div v-after><span class="match">domain.com</span>, <span class="match">test.com</span>, <span class="match">site.com</span></div>
</div>

<div class="regex-pattern"><code>/\w+\.com/g</code></div>


`g` 表示全局匹配，不会在找到第一个结果后停止，而是继续向后查找所有匹配结果。

---
layout: default
---

# 多行 flag Multiline Flag `m`

<div class="regex-example regex-swap">
  <div v-click.hide>domain.com<br>test.com<br>DOMAIN.COM<br>TEST.COM</div>
  <div v-after><span class="match">domain.com</span><br><span class="match">test.com</span><br>DOMAIN.COM<br>TEST.COM</div>
</div>

<div class="regex-pattern"><code>/\w+\.com/m</code></div>


`m` 会改变 `^` 和 `$` 的行为，让它们按“每一行的开头和结尾”来判断，而不只是整个字符串的两端。

---
layout: default
---

# 忽略大小写 flag Case-insensitive Flag `i`

<div class="regex-example regex-swap">
  <div v-click.hide>domain.com<br>test.com<br>DOMAIN.COM<br>TEST.COM</div>
  <div v-after><span class="match">domain.com</span><br><span class="match">test.com</span><br><span class="match">DOMAIN.COM</span><br><span class="match">TEST.COM</span></div>
</div>

<div class="regex-pattern"><code>/\w+\.com/i</code></div>


`i` 表示忽略大小写，因此大小写不同但字母相同的文本都会被视为可匹配。

---
layout: default
---

# Python 示例

```python
text = "Product Code: 1064 Price: $5"

# 用 r"..."
pattern_raw = r"(?<=\$)\d+"

# 不用 r"..."
pattern_no_r = "(?<=\\$)\\d+"

print(re.findall(pattern_raw, text))   # ['5']
print(re.findall(pattern_no_r, text))  # ['5']
```

---
layout: default
---

# 贪婪匹配 Greedy Matching

<div class="regex-example regex-swap">
  <div v-click.hide>ber beer beeer beeeer</div>
  <div v-after><span class="match">ber&nbsp;beer&nbsp;beeer&nbsp;beeeer</span></div>
</div>

<div class="regex-pattern"><code>b.*r</code></div>

*问问你还想多贪：尽可能长。*


贪婪匹配会在满足整体匹配成功的前提下，尽可能多地吞掉字符，所以 `.*` 会优先取最长结果。

---
layout: default
---

# 懒惰匹配 Lazy Matching

<div class="regex-example regex-swap">
  <div v-click.hide>ber beer beeer beeeer</div>
  <div v-after><span class="match">ber</span> <span class="match">beer</span> <span class="match">beeer</span> <span class="match">beeeer</span></div>
</div>

<div class="regex-pattern"><code>b.*?r</code></div>

*加 `?` 让它尽可能短。*


懒惰匹配会在满足整体匹配成功的前提下，尽可能少地吞掉字符，所以 `.*?` 会优先取最短结果。

---
layout: default
---

# Cheat Sheet

- 字面匹配 Literal Match: `abc` 就匹配 `abc`
- 通配符 Wildcard: `.` 匹配任意单个字符，通常不含换行
- 字符集 Character Set: `[abc]` 选一个，`[^abc]` 选“不在里面”的一个
- 范围 Range: `[a-z]`、`[0-9]`
- 量词 Quantifiers: `*` 0 次或多次，`+` 1 次或多次，`?` 0 次或 1 次，`{m,n}` 重复区间
- 分组 Grouping: `()` 用来打包、捕获、控制优先级
- 反向引用 Backreference: `\1`、`\2` 引用前面第 1、2 个捕获分组
- 选择 Alternation: `a|b` 表示二选一
- 转义 Escaping: `\.` 匹配句点本身，`\*` 匹配星号本身
- 锚点 Anchors: `^` 行首，`$` 行尾
- 简写字符 Classes: `\w` 单词字符，`\d` 数字，`\s` 空白；大写版 `\W \D \S` 表示相反
- 断言 Lookaround: `(?=...)` 向前看，`(?!...)` 向前不看，`(?<=...)` 向后看，`(?<!...)` 向后不看
- Flags: `g` 找全部，`m` 让 `^ $` 按多行工作，`i` 忽略大小写
- 贪婪 / 懒惰 Greedy / Lazy: `.*` 尽量多吃，`.*?` 尽量少吃

记忆提醒：
- 方括号 `[]` 管“单个字符”的选择，圆括号 `()` 管“一整段模式”的打包
- `|` 是在模式和模式之间做选择，不是字符集
- 写 Python 时优先用 `r"..."`，避免反斜杠被字符串先吃掉

---
layout: end
---

# End

本练习在线版：[RegexLearn](https://regexlearn.com/learn/regex101)  
可视化测试工具：[regex101](https://regex101.com)、[regexper](https://regexper.com)
