defmodule SumOfMultiples do
  @doc """
  Adds up all numbers from 1 to a given end number that are multiples of the factors provided.
  """
  @spec to(non_neg_integer, [non_neg_integer]) :: non_neg_integer
  def to(limit, factors) do
    factors
    |> Enum.reduce([], fn num, acc ->
      uniq = multiples(num, limit) -- acc
      Enum.concat(uniq, acc)
    end)
    |> Enum.sum()
  end

  defp multiples(value, limit) do
    do_multiples(value, limit, value, [])
  end
  defp do_multiples(_value, limit, current_value, result) when current_value >= limit do
    result
  end
  defp do_multiples(value, limit, current_value, result) do
    do_multiples(value, limit, current_value+value, [current_value | result])
  end
end
