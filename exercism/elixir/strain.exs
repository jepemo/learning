defmodule Strain do
  @doc """
  Given a `list` of items and a function `fun`, return the list of items where
  `fun` returns true.

  Do not use `Enum.filter`.
  """
  @spec keep(list :: list(any), fun :: (any -> boolean)) :: list(any)
  def keep(list, fun) do
    k(list, [], fun)
  end

  defp k([x | tail], acc, fun) do
    case fun.(x) do
      true -> k(tail, acc ++ [x], fun)
      false -> k(tail, acc, fun)
    end
  end
  defp k([], acc, _) do
    acc
  end

  @doc """
  Given a `list` of items and a function `fun`, return the list of items where
  `fun` returns false.

  Do not use `Enum.reject`.
  """
  @spec discard(list :: list(any), fun :: (any -> boolean)) :: list(any)
  def discard(list, fun) do
    keep(list, fn x -> not fun.(x) end)
  end
end
