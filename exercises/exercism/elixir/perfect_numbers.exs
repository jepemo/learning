defmodule PerfectNumbers do
  @doc """
  Determine the aliquot sum of the given `number`, by summing all the factors
  of `number`, aside from `number` itself.

  Based on this sum, classify the number as:

  :perfect if the aliquot sum is equal to `number`
  :abundant if the aliquot sum is greater than `number`
  :deficient if the aliquot sum is less than `number`
  """
  @spec classify(number :: integer) :: {:ok, atom} | {:error, String.t()}
  def classify(number) when number <= 0,
    do: {:error, "Classification is only possible for natural numbers."}

  def classify(number),
    do: {:ok, classify(number, Enum.sum(factors_for(number)))}

  defp classify(number, aliquot_sum) when aliquot_sum == number,
    do: :perfect

  defp classify(number, aliquot_sum) when aliquot_sum > number,
    do: :abundant

  defp classify(number, aliquot_sum) when aliquot_sum < number,
    do: :deficient

  def factors_for(number) do
    factors_for(number, number - 1, [])
  end

  def factors_for(_number, 0, res), do: res

  def factors_for(number, it, res) when rem(number, it) == 0,
    do: factors_for(number, it - 1, [it | res])

  def factors_for(number, it, res),
    do: factors_for(number, it - 1, res)
end
