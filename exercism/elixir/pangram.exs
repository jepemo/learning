defmodule Pangram do
  @doc """
  Determines if a word or sentence is a pangram.
  A pangram is a sentence using every letter of the alphabet at least once.

  Returns a boolean.

    ## Examples

      iex> Pangram.pangram?("the quick brown fox jumps over the lazy dog")
      true

  """

  @letters ?a..?z |> Enum.to_list()

  @spec pangram?(String.t()) :: boolean
  def pangram?(sentence) do
    @letters
    |> Enum.reduce([], fn letter, acc ->
      str_letter = List.to_string([letter])
      case sentence
      |> String.downcase()
      |> String.codepoints()
      |> Enum.member?(str_letter) do
        true -> [str_letter | acc]
        false -> acc
      end
    end)
    |> Enum.count()
    |> (&(&1 == length(@letters))).()
  end
end
