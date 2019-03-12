defmodule Sublist do
  @doc """
  Returns whether the first list is a sublist or a superlist of the second list
  and if not whether it is equal or unequal to the second list.
  """
  def compare(a, b) when b == a, do: :equal
  def compare(_, []), do: :superlist
  def compare([], _), do: :sublist
  def compare(a, b) do
    if is_sublist(a, b) do
      :sublist
    else
      if is_sublist(b, a) do
        :superlist
      else
        :unequal
      end
    end
  end

  defp is_sublist(_a, []), do: false
  defp is_sublist(a, b) when length(a) > length(b), do: false
  defp is_sublist(a, [_h | t] = b) when length(a) <= length(b) do
    case a === Enum.slice(b, 0, length(a)) do
      true -> true
      false -> is_sublist(a, t)
    end
  end
end
