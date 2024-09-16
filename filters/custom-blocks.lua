-- Convert custom div blocks for LaTeX
if FORMAT:match "latex" then
  function Div(elem)
    cls = elem.classes[1]
    if cls == "solution" then
        return {
            pandoc.RawBlock("latex", "\\solution{"),
            elem,
            pandoc.RawBlock("latex", "}")
        }
    else
      table.insert(elem.content, 1,
        pandoc.RawBlock("latex", "\\begin{" .. cls .. "}"))
      table.insert(elem.content,
        pandoc.RawBlock("latex", "\\end{" .. cls .. "}"))
      return elem
    end
  end
end

-- Convert "exr-answer" div blocks for HTML.
-- Format using details/summary tags.
-- Leave div blocks with other classes unchanged.
if FORMAT:match "html" then
  function Div(elem)
    cls = elem.classes[1]
    if cls == "exranswer" then
      table.insert(elem.content, 1,
        pandoc.RawBlock("html", "<details class=\"exr-answer\">"))
      table.insert(elem.content, 2,
        pandoc.RawBlock("html", "<summary>Show Answer</summary>"))
      table.insert(elem.content,
        pandoc.RawBlock("html", "</details>"))
      return elem.content
    else
      return elem
    end
  end
end

-- Remove "jupyterpython" code blocks.
function CodeBlock(elem)
  cls = elem.classes[1]
  if cls == "jupyterpython" then
    elem.classes[1] = "python"
    return {}
  else
    return elem
  end
end
