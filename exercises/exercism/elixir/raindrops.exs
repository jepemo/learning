defmodule Raindrops do
  @doc """
  Returns a string based on raindrop factors.

  - If the number contains 3 as a prime factor, output 'Pling'.
  - If the number contains 5 as a prime factor, output 'Plang'.
  - If the number contains 7 as a prime factor, output 'Plong'.
  - If the number does not contain 3, 5, or 7 as a prime factor,
    just pass the number's digits straight through.
  """
  @factors %{
    3 => "Pling", 
    5 => "Plang", 
    7 => "Plong"
  }

  @spec convert(pos_integer) :: String.t()
  def convert(number) do
    do_convert(number, Map.keys(@factors), [])
  end

  def do_convert(number, [], []) do
    "#{number}"
  end

  def do_convert(_number, [], res) do
    res |> Enum.reverse() |> Enum.join()
  end

  def do_convert(number, [f | rest], res) do
    if rem(number, f) == 0 do
      do_convert(number, rest, [Map.get(@factors, f) | res])
    else
      do_convert(number, rest, res)
    end
  end 
end
