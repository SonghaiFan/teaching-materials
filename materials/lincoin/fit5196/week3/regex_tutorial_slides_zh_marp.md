---
marp: true
title: 正则表达式（Regex）速学与练习
paginate: true
theme: default
lang: zh
footer: 正则表达式入门练习
---

<style>
blockquote {
  font-size: 1.5em; /* Make quotes bigger */
  border: 1px solid #eee;
  padding: 0;
  line-height: 1;
  white-space: pre-wrap;
  font-family: monospace;
}
</style>

# /正则表达式速通记忆决（东亚小孩版本）/g

如何使用如下练习：
根据正则表达式，用荧光笔把匹配到的部分标出来

> Regular Expression

```
Expression
```

---

# 基础匹配 Basic Matchers

> “Every man takes the limits of his own field of vision for the limits of the world.”

```
of
```

---

# 通配符 The Full Stop `.`

`.` 匹配任意单个字符（换行除外，除非加单行/单点模式）

> az AZ 09 \_- = !? ., :;

```
.
```

(点哥写小作文不换行)

---

# 字符集 Character Set `[]` (one of)

匹配集合里的“任一单字符”

> beer deer feer

```
[bdf]eer
```

---

# 取反字符集 `[^ ]` (none of)

匹配不在集合中的单字符

> bear beor beer beur

```
be[^ou]r
```

---

# 字母范围 `[g-k]`

> abcdefghijklmnopqrstuvwxyz

```
[g-k]
```

---

# 重复量词 `*` (0 or n)

> dp dep deep

```
de*p
```

(星星 ✨ 一闪一闪，忽隐忽现，时长时短)

---

# 重复量词 `+` （1 or n）

> dp dep deep

```
de+p
```

---

# 重复量词 `?` （0 or 1）

> a an

```
an?
```

---

# 量词 `{n}` 四位数字

> Release 10/9/2021

```
[0-9]{4}
```

---

# 量词 `{n,}` 至少两位数字

> Release 10/9/2021

```
[0-9]{2,}
```

---

# 量词 `{1,4}` 1 到 4 位数字

> Release 10/9/2021

```
[0-9]{1,4}
```

---

# 分组 `( )` 与 思想

把一段模式整体视为“一个单元”

> ha-ha,haa-haa

```
(haa)
```

---

# 引用分组 反向引用

> ha-ha,haa-haa

```
(ha)-\1,(haa)-
```

---

> ha-ha,haa-haa

```
(ha)-\1,(haa)-\2
```

---

# 非捕获分组 `(?: )`

不需要后续引用时，用它减少开销

> ha-ha,haa-haa

```
(?:ha)-ha,(haa)-\1
```

---

# 选择 | vs 字符集 []

> cat rat dog

```
(c|r)at|dog
```

- `|` 在“子表达式”之间做选择（整段）
- `[]` 在“单字符”间选择

---

# 转义 `\`

需要匹配元字符本身： `{ } [ ] / \ + * . $ ^ | ?`

> (\*) Asterisk.

```
(\*|\.)
```

---

# 行首 `^`

> 1. 3 eggs, beaten
> 2. 1 tsp sunflower oil

```
^[0-9]
```

（在外出头，在家逆反：匹配行开头的数字）

---

# 行尾 `$`

> domain.com/what-is-html.html
> otherdomain.com/html-elements
> website.com/html5-features.html

```
html$
```

（到头来还是钱：匹配行结尾的数字）

---

# 单词字符 `\w`

> abcABC123 \_.:!?

```
\w
```

---

# 非单词字符 `\W`

> abcABC123 \_.:!?

```
\W
```

（人长大了成了和小时候相反的人，丢了底线，多了人和人之间的空间）

---

# 数字字符 `\d`

> abcABC123 \_.:!?

```
\d+
```

---

# 非数字字符 `\D`

> abcABC123 \_.:!?

```
\D+
```

---

# 空白字符 `\s`

> abcABC123 \_.:!?

```
\s
```

---

# 非空白字符 `\S`

> abcABC123 \_.:!?

```
\S+
```

---

# Lookaround 概念

四种：`(?=…)` `(?!=…)` `(?<=…)` `(?<!…)`

---

# 正向先行 `(?=…)`

> Date: 4 Aug 3PM

```
\d+(?=PM)
```

（别问问就是向前看）

---

# 负向先行 `(?!…)`

> Date: 4 Aug 3PM

```
\d+(?!PM)
```

---

# 正向后顾 `(?<=…)`

> Product Code: 1064 Price: $5

```
(?<=\$)\d+
```

---

# 负向后顾 `(?<!…)`

> Product Code: 1064 Price: $5

```
(?<!\$)\d+
```

（匹配前面不是 $ 的数字）

---

# Flag 概念

> 修改匹配模式的“开关”

---

# 全局 flag `g`

> domain.com, test.com, site.com

```
/\w+\.com/g
```

---

# 多行 flag `m`

> domain.com
> test.com
> DOMAIN.COM
> TEST.COM

```
/\w+\.com/m
```

---

# 忽略大小写 `i`

> domain.com
> test.com
> DOMAIN.COM
> TEST.COM

```
/\w+\.com/i
```

---

# Python 示例

```python
text = "Product Code: 1064 Price: $5"

# 用 r"..."
pattern_raw = r"(?<=\$)\d+"

# 不用 r"..."
pattern_no_r = "(?<=\\$)\\d+"  # 反斜杠要写成双的

print(re.findall(pattern_raw, text))   # ['5']
print(re.findall(pattern_no_r, text))  # ['5']
```

---

# 贪婪匹配 (Greedy)

> ber beer beeer beeeer

```
b.*r
```

（问问你还想多贪：尽可能长）

---

# 懒惰匹配 (Lazy)

> ber beer beeer beeeer

```
b.*?r
```

（加 ? 让它尽可能短）

---

# END

本练习在线版 [RegexLearn](https://regexlearn.com/learn/regex101)。
可视化测试工具（[regex101](https://regex101.com/), [regexper](https://regexper.com) 等）
