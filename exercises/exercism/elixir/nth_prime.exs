defmodule Prime do
  @doc """
  Generates the nth prime.
  """
  @spec nth(non_neg_integer) :: non_neg_integer
  def nth(count) when count < 1, do: raise ArgumentError, message: "count must be equal/greater than 0"
  def nth(count) do
    do_nth(count, [], 2)
  end
  defp do_nth(0, [p | _], _last_pn), do: p
  defp do_nth(count, res, last_pn) do
    if is_prime(last_pn) do
      do_nth(count-1, [last_pn | res], last_pn+1)
    else
      do_nth(count, res, last_pn+1)
    end
  end

  defp is_prime(n) when n <= 1, do: false
  defp is_prime(n) do
    do_is_prime(2, n)
  end
  defp do_is_prime(n, n), do: true
  defp do_is_prime(it, n) do
    if rem(n, it) == 0 do
      false
    else
      do_is_prime(it+1, n)
    end
  end
end
