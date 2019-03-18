defmodule Phone do
  @doc """
  Remove formatting from a phone number.

  Returns "0000000000" if phone number is not valid
  (10 digits or "1" followed by 10 digits)

  ## Examples

  iex> Phone.number("212-555-0100")
  "2125550100"

  iex> Phone.number("+1 (212) 555-0100")
  "2125550100"

  iex> Phone.number("+1 (212) 055-0100")
  "0000000000"

  iex> Phone.number("(212) 555-0100")
  "2125550100"

  iex> Phone.number("867.5309")
  "0000000000"
  """
  @spec number(String.t()) :: String.t()
  def number(
        <<"+1 (", area_code::bytes-size(3), ") ", exchange_code::bytes-size(3), "-",
          rest::bytes-size(4)>>
      ) do
    number(area_code, exchange_code, rest)
  end

  def number(
        <<"(", area_code::bytes-size(3), ") ", exchange_code::bytes-size(3), "-",
          rest::bytes-size(4)>>
      ) do
    number(area_code, exchange_code, rest)
  end

  def number(
        <<area_code::bytes-size(3), ".", exchange_code::bytes-size(3), ".", rest::bytes-size(4)>>
      ) do
    number(area_code, exchange_code, rest)
  end

  def number(<<"1", area_code::bytes-size(3), exchange_code::bytes-size(3), rest::bytes-size(4)>>) do
    number(area_code, exchange_code, rest)
  end

  def number(<<area_code::bytes-size(3), exchange_code::bytes-size(3), rest::bytes-size(4)>>) do
    number(area_code, exchange_code, rest)
  end

  def number(_raw) do
    "0000000000"
  end

  def number(area_code, exchange_code, rest) do
    with {ac, _} <- Integer.parse(area_code),
         {ec, _} <- Integer.parse(exchange_code),
         {r, _} <- Integer.parse(rest) do
      if ac > 200 and ec > 200 do
        "#{area_code}#{exchange_code}#{rest}"
      else
        "0000000000"
      end
    else
      _ -> "0000000000"
    end
  end

  @doc """
  Extract the area code from a phone number

  Returns the first three digits from a phone number,
  ignoring long distance indicator

  ## Examples

  iex> Phone.area_code("212-555-0100")
  "212"

  iex> Phone.area_code("+1 (212) 555-0100")
  "212"

  iex> Phone.area_code("+1 (012) 555-0100")
  "000"

  iex> Phone.area_code("867.5309")
  "000"
  """
  @spec area_code(String.t()) :: String.t()
  def area_code(raw) do
    raw
    |> number()
    |> String.slice(0, 3)
  end

  @doc """
  Pretty print a phone number

  Wraps the area code in parentheses and separates
  exchange and subscriber number with a dash.

  ## Examples

  iex> Phone.pretty("212-555-0100")
  "(212) 555-0100"

  iex> Phone.pretty("212-155-0100")
  "(000) 000-0000"

  iex> Phone.pretty("+1 (303) 555-1212")
  "(303) 555-1212"

  iex> Phone.pretty("867.5309")
  "(000) 000-0000"
  """
  @spec pretty(String.t()) :: String.t()
  def pretty(raw) do
    <<area_code::bytes-size(3), exchange_code::bytes-size(3), rest::bytes-size(4)>> = number(raw)
    "(#{area_code}) #{exchange_code}-#{rest}"
  end
end
