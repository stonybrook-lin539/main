---
title: Style and Feature Test
indent: false
---

This document is for testing formatting in web (HTML/CSS) and PDF (LaTeX) output.

Note: this file uses paragraph spacing (\\parskip) for clarity.

## Sections

Text in section.

### Subsection

Text in subsection.

#### Subsubsection

Text in subsubsection.

## Text formatting

Start of section.

New paragraph.

- List item
- List item
- List item
    - List subitem
    - List subitem

Paragraph after list.

1. Numbered list item
2. Numbered list item
3. Numbered list item

Here is a quote block.

> This is a quote block.

Here is a code block.

```
This is a code block.
```

Before horizontal rule

---

After horizontal rule


## Math

Here is some inline math: $y = mx + b$.

And some display math:

$$y = mx + b$$

Special symbols:

$$\alpha\beta\gamma\ltimes\rtimes\cdot$$

Now for some math using custom macros.

$\tuple{a, b, c}$

$\setof{a, b, c}$


## Tables, images

Here is a table.

| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|   12  |  12  |    12   |    12  |
|  123  |  123 |   123   |   123  |
|    1  |    1 |     1   |     1  |


PNG image at natural size, followed by same image with width of 1 inch.

![test image](sbuling-logo.png)
![small image](sbuling-logo.png){width=1in}


## Custom blocks

Text before block.

::: example
This is an example.
:::

Text between blocks.

::: example
This is an example.

This is a new paragraph.
:::

::: advice
- list
- in
- a
- box
:::

Text after blocks.

- Block in a list:

  ::: example
  This is an example.
  :::

## More blocks

::: advice
This is an advice block.
:::

::: theorem
This is a theorem.
:::

::: lemma
This is a lemma.
:::

::: corollary
This is a corollary.
:::

::: proposition
This is a proposition.
:::

::: definition
This is a definition.
:::

::: proof
This is a proof.
:::

::: example
This is an example.
:::

::: exercise
This is an exercise.
:::

::: exercise
This is an exercise with an answer. The answer will appear at the bottom of the document.

::: exranswer
This is the answer to an exercise.
:::
:::

## Custom includes

Simple included .tikz file.

~~~ include-tikz
abaa.tikz
~~~

Custom size. (Not yet implemented.)

~~~ {.include-tikz width=2in}
abaa.tikz
~~~
