defmodule PrimeFactors do
  @doc """
  Compute the prime factors for 'number'.

  The prime factors are prime numbers that when multiplied give the desired
  number.

  The prime factors of 'number' will be ordered lowest to highest.
  """
  @spec factors_for(pos_integer) :: [pos_integer]
  def factors_for(number) do
    factors_for(number, 2, [])
  end

  def factors_for(1, _val, result),
    do: Enum.reverse(result)

  def factors_for(number, val, result) when rem(number, val) == 0 do
    if is_prime?(val) do
      factors_for(div(number, val), val, [val | result])
    else
      factors_for(number, val + 1, result)
    end
  end

  def factors_for(number, val, result),
    do: factors_for(number, val + 1, result)

  defp is_prime?(n),
    do: is_prime?(n, 2)

  defp is_prime?(n, n),
    do: true

  defp is_prime?(n, it) when rem(n, it) == 0,
    do: false

  defp is_prime?(n, it),
    do: is_prime?(n, it + 1)
end
