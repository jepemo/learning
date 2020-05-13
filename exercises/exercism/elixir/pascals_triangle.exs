defmodule PascalsTriangle do
  @doc """
  Calculates the rows of a pascal triangle
  with the given height
  """
  @spec rows(integer) :: [[integer]]
  def rows(num) do
    get_rows(num, 1, [[1]])
  end

  defp get_rows(num, num, res), do: res
  defp get_rows(n, counter, res) do
    last_row = [0] ++ List.last(res) ++ [0]
    get_rows(n, counter+1, res ++ [sum_row(last_row, [])])
  end

  defp sum_row([v, 0 | _], res), do: res ++ [v]
  defp sum_row([v1, v2 | rest], res) do
    sum_row([v2 | rest], res ++ [v1 + v2])
  end
end
