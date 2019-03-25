defmodule BeerSong do
  @doc """
  Get a single verse of the beer song
  """
  @spec verse(integer) :: String.t()
  def verse(number) do
    """
#{verse_number(number, true)} of beer on the wall, #{verse_number(number, false)} of beer.
#{verse_phrase(number)}, #{verse_rest_number(number)} of beer on the wall.
"""
  end

  def verse_number(0, true), do: "No more bottles"
  def verse_number(0, false), do: "no more bottles"
  def verse_number(1, _), do: "1 bottle"
  def verse_number(number, _), do: "#{number} bottles"

  def verse_rest_number(0), do: "99 bottles"
  def verse_rest_number(1), do: "no more bottles"
  def verse_rest_number(2), do: "1 bottle"
  def verse_rest_number(number), do: "#{number-1} bottles"

  def verse_phrase(0), do: "Go to the store and buy some more"
  def verse_phrase(1), do: "Take it down and pass it around"
  def verse_phrase(_), do: "Take one down and pass it around"

  @doc """
  Get the entire beer song for a given range of numbers of bottles.
  """
  @spec lyrics(Range.t()) :: String.t()
  def lyrics(), do: lyrics(99..0)
  def lyrics(range) do
    range
    |> Enum.map(&(verse(&1)))
    |> Enum.join("\n")
  end
end
