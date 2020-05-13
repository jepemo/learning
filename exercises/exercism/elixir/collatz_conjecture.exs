defmodule CollatzConjecture do
  defguard is_positive(num) when num >= 1
  defguard is_even(num) when rem(num, 2) == 0
  defguard is_odd(num) when rem(num, 2) != 0

  @doc """
  calc/1 takes an integer and returns the number of steps required to get the
  number to 1 when following the rules:
    - if number is odd, multiply with 3 and add 1
    - if number is even, divide by 2
  """
  @spec calc(number :: pos_integer) :: pos_integer
  def calc(input) when is_positive(input),
    do: calc(input, 0)

  def calc(1, counter),
    do: counter

  def calc(input, counter) when is_even(input),
    do: calc(div(input, 2), counter + 1)

  def calc(input, counter) when is_odd(input),
    do: calc(3 * input + 1, counter + 1)
end
