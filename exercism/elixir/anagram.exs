defmodule Anagram do
  @doc """
  Returns all candidates that are anagrams of, but not equal to, 'base'.
  """
  @spec match(String.t(), [String.t()]) :: [String.t()]
  def match(base, candidates) do
    candidates
    |> Enum.filter(fn candidate ->
      same_letters(base, candidate)
    end)
  end

  defp same_letters(word1, word2) do
    normalize(word1) == normalize(word2) and String.downcase(word1) != String.downcase(word2)
  end

  defp normalize(word) do
    word
    |> String.downcase()
    |> String.codepoints()
    |> Enum.sort()
  end
end
