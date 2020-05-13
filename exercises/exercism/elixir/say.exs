defmodule Say do

  @numbers %{
    0 => "zero",
    1 => "one",
    2 => "two",
    3 => "three",
    4 => "four",
    5 => "five",
    6 => "six",
    7 => "seven",
    8 => "eight",
    9 => "nine",
    10 => "ten",
    11 => "eleven",
    12 => "twelve",
    13 => "thirteen",
    14 => "fourteen",
    15 => "fifteen",
    16 => "sixteen",
    17 => "seventeen",
    18 => "eighteen",
    19 => "ninteen",
    20 => "twenty",
    30 => "thirty",
    40 => "forty",
    50 => "fifty",
    60 => "sixty",
    70 => "seventy",
    80 => "eighty",
    90 => "ninety",
  }

  @number_keys Map.keys(@numbers)

  @powers ["", "thousand", "million", "billion"]

  @doc """
  Translate a positive integer into English.
  """
  @spec in_english(integer) :: {atom, String.t()}
  def in_english(number) when number < 0 or number > 999_999_999_999, do: {:error, "number is out of range"}
  def in_english(number) when number in @number_keys, do: {:ok, @numbers[number]}
  def in_english(number) when number > 20 and number < 100 do
    d = div(number, 10)
    r = rem(number, 10)
    {:ok, "#{Map.get(@numbers, d * 10)}-#{Map.get(@numbers, r)}"}
  end
  def in_english(number) when number >= 100 and number < 1000 do
    d = div(number, 100)
    r = rem(number, 100)
    {:ok, String.trim("#{format_english(d)} hundred#{format_english(r)}")}
  end
  def in_english(number) when number >= 1000 do
    chunks = get_number_chunks(number)
    in_english(Enum.reverse(chunks), @powers, [])
  end

  defp in_english([], _, res) do
    formatted =
      res
      # |> Enum.reverse()
      |> Enum.join(" ")
      |> String.trim()

    {:ok, formatted}
  end
  defp in_english([num | next], [power | next_p], res) do
    f = String.trim("#{format_english(num, power)}")
    in_english(next, next_p, [f | res])
  end

  defp get_number_chunks(number) do
    number
    |> to_string()
    |> String.codepoints()
    |> Enum.reverse()
    |> Enum.chunk_every(3)
    |> Enum.map(fn d ->
      Enum.reverse(d)
    end)
    |> Enum.reverse()
    |> Enum.map(fn d ->
      {v, _} = Enum.join(d)
      |> Integer.parse()

      v
    end)
  end

  defp format_english(0), do: ""
  defp format_english(d) do
    {:ok, value} = in_english(d)
    " #{value}"
  end
  defp format_english(0, _), do: ""
  defp format_english(d, power) do
    {:ok, value} = in_english(d)
    " #{value} #{power}"
  end
end
