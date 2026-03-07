---
theme: default
title: Built-in-First Monash Slide Template
layout: cover
info: |
  ## FIT2179 Slide Template
  Built-in layouts first, local styling second, new layouts last
highlighter: shiki
drawings:
  persist: false
transition: slide-left
---

# Built-in-First Monash Slide Template

Minimal brand defaults, flexible local composition, and no dependency on custom layouts.

---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Design rules</p>

# What This Template Optimizes For

This template is designed to be:

- broad enough to cover most teaching scenarios
- thin enough that AI can still invent page-specific compositions
- stable enough that default decks still look consistent


<div class="mt-6 border border-slate-300 bg-white/55 p-4 text-sm">
Rule: if a visual decision only helps one deck, keep it in markdown or local HTML instead of pushing it into global CSS.
</div>

<div class="mt-4 border-l-2 border-slate-400 pl-4 text-sm text-slate-600">
Default recommendation: start with a built-in layout, then use utility classes or local <code>&lt;style&gt;</code> before creating any new layout file.
</div>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Scenario chooser</p>

# Which Built-in Layout Should Start From?

| Scenario | Start from | Typical local tweak |
|----------|------------|---------------------|
| opening or closing | `cover`, `intro`, `end` | add local spacing or a quiet subtitle block |
| lecture notes and explanation | `default`, `center` | wrap content in `max-w-*` or add a callout box |
| screenshot, chart, or diagram | `image-right`, `image-left`, `image` | adjust image fit and scale text block |
| comparison | `two-cols` | tighten gap, style one side as a panel |
| section divider | `section`, `statement` | add one short supporting line |
| quote or big message | `quote`, `fact`, `statement` | tune typography locally |
| total custom art direction | `none`, `full` | build the whole slide in HTML |

<div class="mt-6 border-l-2 border-sky-700 pl-4 text-sm text-slate-600">
Keep layout choice simple. Most teaching slides still start from <code>default</code>, <code>two-cols</code>, or an image layout.
</div>

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Deck map</p>

# Template Map

::right::

<div class="border border-slate-300 bg-white/60 p-4 text-sm">
  <Toc maxDepth="1" listClass="text-sm leading-snug" />
</div>

---
layout: section
---

# Cover Or Section Break

Use a built-in section slide when the job is just to reset attention and mark a new phase.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Scenario 1 - lecture content</p>

# Standard Lecture Page

This is the default pattern for most teaching slides.

- explain a concept
- give a short list
- add one key takeaway

## Why it works

The page is calm, readable, and easy for AI to extend with HTML blocks or utility classes.

<div class="mt-6 border border-slate-300 bg-white/60 p-4">
    <p class="mt-2">Use one strong title, one secondary heading, then a small number of bullets or short paragraphs.</p>
</div>

---
layout: two-cols
---

# Scenario 2 - Comparison

When the page is really about comparing two ideas, the built-in `two-cols` layout is usually enough.

- left: concept A
- right: concept B
- simple slot syntax
- no custom layout file needed

::right::

<div class="border border-slate-300 bg-white/60 p-5 text-sm">
  <p class="text-xs uppercase tracking-[0.18em] text-slate-500">Comparison block</p>
  <p class="mt-3">This slide is only using a built-in layout plus a local class for tighter spacing.</p>
</div>

---
layout: image-right
image: /images/viz-25.png
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Scenario 3 - image walkthrough</p>

# Image-First Explanation

Use this when the visual is part of the teaching logic:

- software interface walkthrough
- chart critique
- diagram explanation
- before and after comparison

<div class="mt-6 border border-slate-300 bg-white/55 p-4 text-sm">
If the image is secondary, switch back to <code>default</code> and place the image manually inside a local grid.
</div>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Scenario 4 - data or rubric</p>

# Table, Checklist, or Rubric Page

The built-in `default` layout works fine for tables if you tighten the table locally instead of inventing a new global component.

| Item | Purpose | Weight |
|------|---------|--------|
| Forum post | critique practice | 2% |
| Studio task | in-class application | 3% |
| Project work | deeper synthesis | 25% |

## Practical use cases

- assessment breakdown

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Scenario 5 - interactive explanation</p>

# Built-in Components Still Fit

<div class="grid grid-cols-2 gap-6 items-start">

<div>

  <VClicks>

  - reveal steps one by one
  - control pacing in class
  - reduce clutter on dense slides

  </VClicks>

  <div class="mt-6 border border-slate-300 bg-white/60 p-4 text-sm">
    <VSwitch>
      <template #1>State 1: introduce the concept</template>
      <template #2>State 2: compare alternatives</template>
      <template #3>State 3: land the takeaway</template>
    </VSwitch>
  </div>

</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <Transform :scale="0.82" origin="top left">
    <table>
      <thead>
        <tr>
          <th>Component</th>
          <th>Use</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>`Toc`</td>
          <td>agenda and overview</td>
        </tr>
        <tr>
          <td>`VClicks`</td>
          <td>progressive reveal</td>
        </tr>
        <tr>
          <td>`VSwitch`</td>
          <td>show states</td>
        </tr>
        <tr>
          <td>`Transform`</td>
          <td>shrink large content</td>
        </tr>
      </tbody>
    </table>
  </Transform>
</div>

</div>

---
layout: statement
---

Use built-in layouts for emphasis when they are already the fastest way to express the slide.

This is `statement`: one clear teaching takeaway, minimal supporting text.

---
layout: fact
---

# 75%

of layout problems in teaching decks are density problems, not styling problems.

---
layout: quote
---

“The point of the theme is consistency, not decoration.”

Theme rule: use `quote` for attributed lines, reflection prompts, or a single voice you want students to pause on.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Built-in compatibility</p>

# Built-in Layouts That Still Work Well

<div class="grid grid-cols-2 gap-6 text-sm">

<div>

## Recommended built-ins

- `default`
- `center`
- `two-cols`
- `statement`,`quote`,`fact`
- `image-left`,`image-right`

</div>

<div>

## Use with care

- `iframe`, `iframe-left`, `iframe-right`
- `Youtube`
- `Tweet`
- `SlidevVideo`


</div>

</div>

<div class="mt-6 border border-slate-300 bg-white/55 p-4 text-sm">
The template does not try to restyle every built-in layout. It only keeps the visual baseline calm enough that built-ins remain usable.
</div>

<div class="mt-4 border-l-2 border-slate-400 pl-4 text-sm text-slate-600">
Difference: `statement` is for a strong takeaway, `fact` is for one number or datum, `quote` is for a line you want to attribute or let resonate.
</div>

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Prompting AI</p>

# What To Tell AI In The Deck

Put art direction in the markdown itself.

Good instructions:

- avoid large rounded corners
- prefer thin borders and flat blocks
- keep the palette restrained
- use asymmetry and whitespace
- make charts and screenshots functional, not decorative
- favor editorial composition over dashboard clutter

::right::

Bad instructions:

- invent a new global helper class for every page
- add a new layout file for every variation
- encode one lesson's styling choices into the theme

---
layout: end
---

# Template Ready

Built-in layouts first, local styling second, new layouts last.
