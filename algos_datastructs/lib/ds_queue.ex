defmodule AED.List.Queue do
  def enqueue(list, value) when is_list(value), do: value ++ list
  def enqueue(list, value), do: [value] ++ list

  defp dequeue(hl, [h|[]]), do: {h, hl}
  defp dequeue(hl, [h|t]), do: dequeue(hl++[h], t)
  def dequeue([]), do: {nil, []}
  def dequeue([h|[]]), do: {h, []}
  def dequeue([h|t]), do: dequeue([h], t)

  def peek([]), do: nil
  def peek([h|[]]), do: h
  def peek([_|t]), do: peek(t)

  def is_empty([]), do: True
  def is_empty([_|_]), do: False
end
