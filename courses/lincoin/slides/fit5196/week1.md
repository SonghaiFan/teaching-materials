---
theme: default
title: FIT5196 - Week 1 Introduction
layout: cover
info: |
  ## FIT5196 Week 1
  Introduction to Data Visualisation
highlighter: shiki
drawings:
  persist: false
transition: slide-left
---

# FIT5196 Data Visualisation

## Week 1: Introduction to Data Visualisation

---

# Agenda

1. Course Overview
2. What is Data Visualisation?
3. Why Visualise Data?
4. The Visualisation Pipeline
5. Key Principles
6. Tools and Technologies

---
layout: section
---

# Course Overview

---

# Learning Objectives

By the end of this course, you will be able to:

- **Design** effective visualisations for different data types
- **Implement** interactive visualisations using modern tools
- **Evaluate** visualisation designs using principles and heuristics
- **Apply** visualisation techniques to real-world problems

---
layout: two-cols
---

# Assessment Structure

| Component | Weight | Due Date |
|-----------|--------|----------|
| Assignment 1 | 20% | Week 4 |
| Assignment 2 | 30% | Week 8 |
| Final Project | 40% | Week 12 |
| Participation | 10% | Ongoing |

::right::

<div class="border border-slate-300 bg-white/60 p-4">
  <p class="text-xs uppercase tracking-[0.18em] text-slate-500">Key Dates</p>
  <ul class="mt-3 text-sm">
    <li>Census Date: Week 2</li>
    <li>Mid-semester Break: Week 6</li>
    <li>Final Presentations: Week 12</li>
  </ul>
</div>

---
layout: section
---

# What is Data Visualisation?

---

# Definition

> "Data visualisation is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualisation tools provide an accessible way to see and understand trends, outliers, and patterns in data."

<div class="mt-6 border-l-2 border-sky-700 pl-4 text-sm text-slate-600">
In simpler terms: Turning numbers into pictures to help people understand them better.
</div>

---

# The Goal of Visualisation

<div class="grid grid-cols-2 gap-6">

<div class="border border-slate-300 bg-white/60 p-4">
  <h3 class="text-lg font-bold mb-2">Analytical</h3>
  <ul class="text-sm">
    <li>Explore data patterns</li>
    <li>Discover insights</li>
    <li>Support decision-making</li>
    <li>Answer specific questions</li>
  </ul>
</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <h3 class="text-lg font-bold mb-2">Presentational</h3>
  <ul class="text-sm">
    <li>Communicate findings</li>
    <li>Persuade audiences</li>
    <li>Tell stories with data</li>
    <li>Share knowledge</li>
  </ul>
</div>

</div>

---
layout: section
---

# Why Visualise Data?

---

# Anscombe's Quartet

Four datasets with identical statistical properties:

| Statistic | Value |
|-----------|-------|
| Mean of x | 9 |
| Mean of y | 7.5 |
| Variance of x | 11 |
| Variance of y | 4.12 |
| Correlation | 0.816 |

<div class="mt-4 border-l-2 border-sky-700 pl-4 text-sm text-slate-600">
Yet they look completely different when visualised!
</div>

---
layout: image-right
image: https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Anscombe%27s_quartet_3.svg/800px-Anscombe%27s_quartet_3.svg.png
---

# The Power of Visualisation

Numbers alone can be misleading.

Visualisation reveals:
- **Patterns** hidden in tables
- **Outliers** that affect statistics
- **Relationships** between variables
- **Trends** over time

<div class="mt-6 border border-slate-300 bg-white/55 p-4 text-sm">
This is why we visualise: to see what statistics cannot tell us.
</div>

---
layout: section
---

# The Visualisation Pipeline

---

# From Data to Insight

<div class="grid grid-cols-4 gap-4 text-center">

<div class="border border-slate-300 bg-white/60 p-4">
  <div class="text-2xl mb-2">📊</div>
  <h3 class="font-bold">Data</h3>
  <p class="text-xs mt-2">Raw values, tables, databases</p>
</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <div class="text-2xl mb-2">⚙️</div>
  <h3 class="font-bold">Process</h3>
  <p class="text-xs mt-2">Clean, transform, aggregate</p>
</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <div class="text-2xl mb-2">🎨</div>
  <h3 class="font-bold">Visual</h3>
  <p class="text-xs mt-2">Map data to visual elements</p>
</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <div class="text-2xl mb-2">💡</div>
  <h3 class="font-bold">Insight</h3>
  <p class="text-xs mt-2">Understanding, decisions</p>
</div>

</div>

---

# Key Considerations

<div class="grid grid-cols-2 gap-6">

<div>

## Data Characteristics

- **Type**: Categorical, numerical, temporal, spatial
- **Size**: Small, medium, large, massive
- **Structure**: Tabular, hierarchical, network, text

</div>

<div>

## Visual Choices

- **Marks**: Points, lines, bars, areas
- **Channels**: Position, size, color, shape
- **Scales**: Linear, logarithmic, ordinal

</div>

</div>

---
layout: section
---

# Key Principles

---

# The Visual Hierarchy

<div class="border border-slate-300 bg-white/60 p-4 mb-4">

**Most Accurate to Least Accurate:**

1. **Position** (most accurate)
2. **Length**
3. **Angle**
4. **Area**
5. **Volume**
6. **Color** (least accurate for magnitude)

</div>

<div class="text-sm text-slate-600">
Choose your visual encoding based on what you want to communicate.
</div>

---

# Design Guidelines

<div class="grid grid-cols-2 gap-6">

<div class="border border-slate-300 bg-white/60 p-4">
  <h3 class="font-bold text-green-700">✓ Do</h3>
  <ul class="text-sm mt-2">
    <li>Start with the question</li>
    <li>Choose appropriate chart types</li>
    <li>Use color purposefully</li>
    <li>Provide context and labels</li>
    <li>Keep it simple</li>
  </ul>
</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <h3 class="font-bold text-red-700">✗ Don't</h3>
  <ul class="text-sm mt-2">
    <li>Use 3D for 2D data</li>
    <li>Overload with colors</li>
    <li>Hide the baseline</li>
    <li>Use pie charts for many categories</li>
    <li>Forget about accessibility</li>
  </ul>
</div>

</div>

---
layout: section
---

# Tools and Technologies

---

# Tools We'll Use

<div class="grid grid-cols-3 gap-4">

<div class="border border-slate-300 bg-white/60 p-4 text-center">
  <h3 class="font-bold">D3.js</h3>
  <p class="text-xs mt-2">Low-level JavaScript library for custom visualisations</p>
</div>

<div class="border border-slate-300 bg-white/60 p-4 text-center">
  <h3 class="font-bold">Observable</h3>
  <p class="text-xs mt-2">Interactive notebooks for data exploration</p>
</div>

<div class="border border-slate-300 bg-white/60 p-4 text-center">
  <h3 class="font-bold">Tableau</h3>
  <p class="text-xs mt-2">Drag-and-drop tool for rapid prototyping</p>
</div>

</div>

<div class="mt-6 border-l-2 border-sky-700 pl-4 text-sm text-slate-600">
We'll focus on the concepts first, then apply them with these tools.
</div>

---
layout: statement
---

Good visualisation is not about making pretty pictures.

It's about making data understandable.

---
layout: end
---

# Next Week

## Data Types and Visual Encodings

- Understanding data types
- Choosing visual encodings
- Introduction to D3.js

<div class="mt-8 text-sm">
Questions? Contact me after class or via email.
</div>
