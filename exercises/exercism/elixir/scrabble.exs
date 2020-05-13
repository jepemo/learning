defmodule Scrabble do
  @doc """
  Calculate the scrabble score for the word.
  """
  @scores %{
    "A" => 1,
    "E" => 1,
    "I" => 1,
    "O" => 1,
    "U" => 1,
    "L" => 1,
    "N" => 1,
    "R" => 1,
    "S" => 1,
    "T" => 1,
    "D" => 2,
    "G" => 2,
    "B" => 3,
    "C" => 3,
    "M" => 3,
    "P" => 3,
    "F" => 4,
    "H" => 4,
    "V" => 4,
    "W" => 4,
    "Y" => 4,
    "K" => 5,
    "J" => 8,
    "X" => 8,
    "Q" => 10,
    "Z" => 10
  }

  @spec score(String.t()) :: non_neg_integer
  def score(word) do
    letters =
      word
      |> String.upcase()
      |> String.codepoints()

    do_score(letters, 0)
  end

  defp do_score([], score), do: score

  defp do_score([l | rest], score) do
    do_score(rest, score + Map.get(@scores, l, 0))
  end
end
