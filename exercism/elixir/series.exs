defmodule StringSeries do
  @doc """
  Given a string `s` and a positive integer `size`, return all substrings
  of that size. If `size` is greater than the length of `s`, or less than 1,
  return an empty list.
  """
  @spec slices(s :: String.t(), size :: integer) :: list(String.t())
  def slices(s, size) when size <= 0 do
    []
  end
  def slices(s, size) do
    do_slices(s, [], size)
  end

  def do_slices("", result, _size) do
    result |> Enum.reverse
  end
  def do_slices(s, result, size) do
    if String.length(s) == size do
      do_slices("", [s | result], size)
    else
      if String.length(s) < size do
        do_slices("", [], size)
      else
        do_slices(
          String.slice(s, 1, String.length(s)), 
          [String.slice(s, 0, size) | result], 
          size)
      end
    end
  end
end
