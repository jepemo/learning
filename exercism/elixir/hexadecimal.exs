defmodule Hexadecimal do
  @doc """
    Accept a string representing a hexadecimal value and returns the
    corresponding decimal value.
    It returns the integer 0 if the hexadecimal is invalid.
    Otherwise returns an integer representing the decimal value.

    ## Examples

      iex> Hexadecimal.to_decimal("invalid")
      0

      iex> Hexadecimal.to_decimal("af")
      175

  """

  @trad_table %{
    "0" => 0,
    "1" => 1,
    "2" => 2,
    "3" => 3,
    "4" => 4,
    "5" => 5,
    "6" => 6,
    "7" => 7,
    "8" => 8,
    "9" => 9,
    "a" => 10,
    "b" => 11,
    "c" => 12,
    "d" => 13,
    "e" => 14,
    "f" => 15
  }

  @spec to_decimal(binary) :: integer
  def to_decimal(hex) do
    hex
    |> String.downcase()
    |> String.codepoints()
    |> Enum.reverse()
    |> Enum.zip(0..String.length(hex)-1)
    |> Enum.reduce_while(0, fn {digit, counter}, acc ->
      if Enum.member?(Map.keys(@trad_table), digit) do
        {:cont, acc + @trad_table[digit] * :math.pow(16, counter)}
      else
        {:halt, 0}
      end
    end)
  end
end
