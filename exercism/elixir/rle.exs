defmodule RunLengthEncoder do
  @digits ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

  @doc """
  Generates a string where consecutive elements are represented as a data value and count.
  "AABBBCCCC" => "2A3B4C"
  For this example, assume all input are strings, that are all uppercase letters.
  It should also be able to reconstruct the data into its original form.
  "2A3B4C" => "AABBBCCCC"
  """
  @spec encode(String.t()) :: String.t()
  def encode(string) do
    string
    |> String.codepoints()
    |> Enum.chunk_while([], fn item, acc ->
      case acc do
        [h | _t] when h == item ->
          {:cont, [item | acc]}
        [h | _t] when h != item ->
          {:cont, acc, [item]}
        [] -> {:cont, [item]}
      end
    end, fn 
      [] -> {:cont, []}
      acc -> {:cont, acc, []}
    end)
    |> Enum.map(fn chars ->
      [c | _] = chars
      case Enum.count(chars) do
        1 -> c
        _ -> "#{Enum.count(chars)}#{c}"
      end
    end)
    |> Enum.join()
  end

  @spec decode(String.t()) :: String.t()
  def decode(string) do
    string
    |> String.codepoints()
    |> decompose()
    |> Enum.map(fn {num, letter} -> 
      String.duplicate(letter, num)
    end)
    |> Enum.join()
  end

  defp decompose(letters) do
    do_decompose(letters, [], nil)
  end
  defp do_decompose([], res, _) do
    res
  end
  defp do_decompose([h | t], res, nil) when h in @digits do
    do_decompose(t, res, [h])
  end
  defp do_decompose([h | t], res, digits) when h in @digits do
    do_decompose(t, res, digits ++ [h])
  end
  defp do_decompose([h | t], res, digits) do
    if digits == nil do
      do_decompose(t, res ++ [{1, h}], nil)
    else
      {num, _} = digits |> Enum.join() |> Integer.parse()
      do_decompose(t, res ++ [{num, h}], nil)
    end
  end
end
