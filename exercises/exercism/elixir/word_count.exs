defmodule Words do
  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t()) :: map
  def count(sentence) do
    sentence
    |> clean()
    |> String.split()
    |> count_words()
  end

  defp count_words(list_of_words) do
    Enum.reduce(list_of_words, %{}, fn w, acc ->
      case Map.get(acc, w) do 
        nil -> Map.put(acc, w, 1)
        value -> Map.put(acc, w, value+1)
      end
    end)
  end

  defp clean(text) do
    text
    |> String.downcase()
    |> String.replace(~r/[!&@$%^&:,_]/, " ")
  end
end
