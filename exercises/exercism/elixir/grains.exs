defmodule Grains do
  @doc """
  Calculate two to the power of the input minus one.
  """
  @spec square(pos_integer) :: pos_integer
  def square(number) when number > 64 or number < 1,
    do: {:error, "The requested square must be between 1 and 64 (inclusive)"}
  def square(number) do
    {:ok, do_square(1, number, 1)}
  end
  defp do_square(max, max, result), do: result
  defp do_square(actual, max, result) do
    do_square(actual+1, max, result * 2)
  end

  @doc """
  Adds square of each number from 1 to 64.
  """
  @spec total :: pos_integer
  def total do
    val = 1..64 
    |> Enum.map(&(elem(square(&1), 1))) 
    |> Enum.sum()
    {:ok, val}
  end
end
