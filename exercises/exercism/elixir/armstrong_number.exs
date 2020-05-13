defmodule ArmstrongNumber do
  @moduledoc """
  Provides a way to validate whether or not a number is an Armstrong number
  """

  @spec valid?(integer) :: boolean
  def valid?(number) do
    number_size = String.length(to_string(number))

    number
    |> to_string()
    |> String.codepoints()
    |> Enum.map(fn x ->
      {val, _} = Integer.parse(x)
      :math.pow(val, number_size)
    end)
    |> Enum.sum()
    |> (fn val -> val == number end).()
  end
end
