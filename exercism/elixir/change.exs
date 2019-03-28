defmodule Change do
  @doc """
    Determine the least number of coins to be given to the user such
    that the sum of the coins' value would equal the correct amount of change.
    It returns {:error, "cannot change"} if it is not possible to compute the
    right amount of coins. Otherwise returns the tuple {:ok, list_of_coins}

    ## Examples

      iex> Change.generate([5, 10, 15], 3)
      {:error, "cannot change"}

      iex> Change.generate([1, 5, 10], 18)
      {:ok, [1, 1, 1, 5, 10]}

  """

  @spec generate(list, integer) :: {:ok, list} | {:error, String.t()}
  def generate(_coins, 0), do: {:ok, []}

  def generate(coins, target) do
    results =
      check(Enum.reverse(coins), target, [], [])
      |> Enum.filter(&(&1 != []))

    if Enum.count(results) > 0 do
      [shortest | _] =
        results
        |> Enum.map(&Enum.count(&1))
        |> Enum.sort()

      {:ok, Enum.find(results, &(Enum.count(&1) == shortest))}
    else
      {:error, "cannot change"}
    end
  end

  def check(_, 0, partial_result, result),
    # do: [Enum.sort(partial_result) | result]
    do: [Enum.sort(partial_result) | result]

  def check([], _remain, _partial_result, result),
    do: result

  def check([coin | rest], remain, partial_result, result) when remain - coin < 0,
    do: check(rest, remain, partial_result, result)

  def check([coin | rest_coins] = coins, remain, partial_result, result)
      when remain - coin >= 0 do
    min_result = get_min_result(result)

    if min_result != nil and Enum.count(partial_result) > min_result do
      result
    else
      result = check(coins, remain - coin, [coin | partial_result], result)
      result = check(rest_coins, remain, partial_result, result)
      result
    end
  end

  defp get_min_result([]), do: nil

  defp get_min_result(lists) do
    lists
    |> Enum.map(&Enum.count(&1))
    |> Enum.sort()
    |> List.to_tuple()
    |> elem(0)
  end
end
