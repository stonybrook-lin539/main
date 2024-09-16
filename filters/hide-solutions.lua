-- Do not show solutions
function Div(elem)
  cls = elem.classes[1]
  if cls == "solution" then
    return {}
  else
    return elem
  end
end

