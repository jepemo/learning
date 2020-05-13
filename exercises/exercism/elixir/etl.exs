defmodule ETL do
  @doc """
  Transform an index into an inverted index.

  ## Examples

  iex> ETL.transform(%{"a" => ["ABILITY", "AARDVARK"], "b" => ["BALLAST", "BEAUTY"]})
  %{"ability" => "a", "aardvark" => "a", "ballast" => "b", "beauty" =>"b"}
  """
  @spec transform(map) :: map
  def transform(input) do
    Enum.reduce(input, %{}, fn {letter, word_list}, result ->
      Enum.reduce(word_list, result, fn word, acc ->
        Map.put(acc, String.downcase(word), letter)
      end)
    end)
  end
end
