defmodule RotationalCipher do
  @doc """
  Given a plaintext and amount to shift by, return a rotated string.

  Example:
  iex> RotationalCipher.rotate("Attack at dawn", 13)
  "Nggnpx ng qnja"
  """

  # @spec rotate(text :: String.t(), shift :: integer) :: String.t()
  def rotate(text, shift) do
    text
    |> String.to_charlist()
    |> Enum.map(fn x -> 
      case x do
        x when x in ?a..?z -> rem(x + shift - ?a, Enum.count(?a..?z)) + ?a
        x when x in ?A..?Z -> rem(x + shift - ?A, Enum.count(?A..?Z)) + ?A
        _ -> x
      end
    end)
    |> to_string()
  end
end
