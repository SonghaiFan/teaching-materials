---
theme: default
title: FIT5196 - Week 4
layout: cover
info: |
  ## FIT5196 Week 4
  Exploratory Data Analysis (EDA)
highlighter: shiki
drawings:
  persist: false
transition: slide-left
---

# FIT5196 Data Wrangling

## Week 4: Exploratory Data Analysis (EDA)

---

# Agenda

1. What is EDA?
2. Understanding Data Types
3. Statistical Summaries
4. Data Visualization
5. Identifying Data Quality Issues

---
layout: section
---

# Introduction to EDA

---

# What is EDA?

> "Exploratory Data Analysis is an approach to analyzing data sets to summarize their main characteristics, often using visual methods."

<div class="mt-6 border-l-2 border-sky-700 pl-4 text-sm text-slate-600">
EDA helps you:<br>
• Understand data structure<br>
• Discover patterns and relationships<br>
• Detect anomalies and outliers<br>
• Form hypotheses for further analysis
</div>

---

# EDA Workflow

<div class="grid grid-cols-4 gap-4 text-center">

<div class="border border-slate-300 bg-white/60 p-4">
  <div class="text-2xl mb-2">1️⃣</div>
  <h3 class="font-bold">Load</h3>
  <p class="text-xs">Import data</p>
</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <div class="text-2xl mb-2">2️⃣</div>
  <h3 class="font-bold">Inspect</h3>
  <p class="text-xs">Check structure</p>
</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <div class="text-2xl mb-2">3️⃣</div>
  <h3 class="font-bold">Summarize</h3>
  <p class="text-xs">Statistics</p>
</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <div class="text-2xl mb-2">4️⃣</div>
  <h3 class="font-bold">Visualize</h3>
  <p class="text-xs">Charts & plots</p>
</div>

</div>

---
layout: section
---

# Understanding Data

---

# Data Types

| Type | Description | Examples |
|------|-------------|----------|
| **Numeric** | Continuous or discrete | Age, Salary, Temperature |
| **Categorical** | Limited set of values | Gender, Country, Status |
| **Ordinal** | Ordered categories | Rating (1-5), Education level |
| **Text** | Free-form strings | Names, Descriptions |
| **Datetime** | Temporal data | Dates, Timestamps |
| **Boolean** | True/False values | Is_active, Has_subscription |

---

# Pandas for EDA

```python
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Basic info
df.info()
df.describe()
df.shape

# Check missing values
df.isnull().sum()

# View sample
df.head(10)
df.tail(5)

# Value counts
df['column'].value_counts()
```

---
layout: section
---

# Visualization

---

# Common EDA Plots

<div class="grid grid-cols-3 gap-4">

<div class="border border-slate-300 bg-white/60 p-4">
  <h3 class="font-bold">Univariate</h3>
  <ul class="text-xs mt-2">
    <li>Histogram</li>
    <li>Box plot</li>
    <li>Bar chart</li>
    <li>Density plot</li>
  </ul>
</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <h3 class="font-bold">Bivariate</h3>
  <ul class="text-xs mt-2">
    <li>Scatter plot</li>
    <li>Line plot</li>
    <li>Grouped bar chart</li>
    <li>Correlation heatmap</li>
  </ul>
</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <h3 class="font-bold">Multivariate</h3>
  <ul class="text-xs mt-2">
    <li>Pair plot</li>
    <li>3D scatter</li>
    <li>Facet grid</li>
    <li>Parallel coordinates</li>
  </ul>
</div>

</div>

---

# Python Visualization Libraries

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram
plt.hist(df['age'], bins=20)

# Box plot
sns.boxplot(x=df['category'], y=df['value'])

# Scatter plot
plt.scatter(df['x'], df['y'])

# Correlation heatmap
sns.heatmap(df.corr(), annot=True)

# Pair plot
sns.pairplot(df)
```

---
layout: section
---

# Data Quality Issues

---

# Common Issues to Identify

| Issue | Detection | Action |
|-------|-----------|--------|
| **Missing values** | `isnull().sum()` | Impute or remove |
| **Outliers** | Box plots, Z-score | Investigate, cap, or remove |
| **Duplicates** | `duplicated()` | Remove or investigate |
| **Inconsistencies** | Value counts | Standardize formats |
| **Wrong types** | `dtypes` | Convert types |
| **Invalid values** | Range checks | Clean or flag |

---
layout: statement
---

EDA is not a one-time task.

Revisit it throughout your analysis.

---
layout: end
---

# Next Week

## Data Discovery & Collection

- Finding data sources
- Web scraping basics
- API integration
