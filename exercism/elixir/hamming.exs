defmodule Hamming do
  @doc """
  Returns number of differences between two strands of DNA, known as the Hamming Distance.

  ## Examples

  iex> Hamming.hamming_distance('AAGTCATA', 'TAGCGATC')
  {:ok, 4}
  """
  @spec hamming_distance([char], [char]) :: {:ok, non_neg_integer} | {:error, String.t()}
  def hamming_distance(strand1, strand2) do
    hamming_distance(to_list(strand1), to_list(strand2), 0)
  end
  
  def hamming_distance(l1, l2, _count) when length(l1) != length(l2), 
    do: {:error, "Lists must be the same length"}
  def hamming_distance([], [], count), 
    do: {:ok, count}
  def hamming_distance([v1 | r1], [v1 | r2], count),
    do: hamming_distance(r1, r2, count)
  def hamming_distance([_v1 | r1], [_v2 | r2], count),
    do: hamming_distance(r1, r2, count+1)

  def to_list(charlist) do
    charlist |> String.Chars.to_string() |> String.codepoints()
  end
end
