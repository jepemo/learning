defmodule Isogram do
  @allowed [" ", "-"]

  @doc """
  Determines if a word or sentence is an isogram
  """
  @spec isogram?(String.t()) :: boolean
  def isogram?(sentence) do
    sentence 
    |> String.codepoints()
    |> Enum.reduce(%{}, fn l, acc ->
      if l not in @allowed do
        Map.update(acc, l, 1, &(&1+1))
      else
        acc
      end
    end)
    |> Map.values()
    |> Enum.all?(&(&1 == 1))
  end
end
