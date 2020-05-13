defmodule AllYourBase do
  @doc """
  Given a number in base a, represented as a sequence of digits, converts it to base b,
  or returns nil if either of the bases are less than 2
  """

  @spec convert(list, integer, integer) :: list
  def convert([], _base_a, _base_b), do: nil
  def convert(_digits, base_a, base_b) when base_a <= 1 or base_b <= 1, do: nil
  def convert(digits, base_a, base_b) do
    with {:ok, normalized} <- from_base(digits, base_a) do
      to_base(normalized, base_b)
    else
      :error -> nil
    end
  end

  def from_base(digits, base) do
    if Enum.any?(digits, &(&1 >= base or &1 < 0)) do
      :error
    else
      indexes = (digits |> Enum.count())-1..0
      v = digits
      |> Enum.zip(indexes)
      |> Enum.reduce(0, fn {v, p}, acc ->
        acc + Kernel.trunc(v * :math.pow(base, p))
      end)

      {:ok, v}
    end
  end


  def to_base(0, _base), do: [0]
  def to_base(value, base) do
    to_base(value, base, [])
  end
  def to_base(0, _base, res), do: res
  def to_base(value, base, res) do
    d = div(value, base)
    r = rem(value, base)

    to_base(d, base, [r | res])
  end
end
