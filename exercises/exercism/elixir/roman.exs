defmodule Roman do
  @numerals %{
    1 => "I",
    4 => "IV",
    5 => "V",
    9 => "IX",
    10 => "X",
    40 => "XL",
    50 => "L",
    90 => "XC",
    100 => "C",
    400 => "CD",
    500 => "D",
    900 => "CM",
    1000 => "M"
  }

  @multiples [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

  @doc """
  Convert the number to a roman number.
  """
  @spec numerals(pos_integer) :: String.t()
  def numerals(number) do
    numerals(number, @multiples, [])
  end

  def numerals(0, _multiples, result) do
    result |> Enum.reverse() |> Enum.join()
  end
  def numerals(number, [mult | other_mults] = mults, result) do
    rest = number - mult
    if rest >= 0 do
      if rest >= mult do
        numerals(rest, mults, [@numerals[mult] | result])
      else
        numerals(rest, other_mults, [@numerals[mult] | result])
      end
    else
      numerals(number, other_mults, result)
    end
  end
end
