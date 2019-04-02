defmodule Atbash do
  @alphabet ?a..?z |> Enum.map(&List.to_string([&1]))
  @numbers ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

  @doc """
  Encode a given plaintext to the corresponding ciphertext

  ## Examples

  iex> Atbash.encode("completely insecure")
  "xlnko vgvob rmhvx fiv"
  """
  @spec encode(String.t()) :: String.t()
  def encode(plaintext) do
    plaintext
    |> String.downcase()
    |> String.codepoints()
    |> Enum.reduce([], fn c, acc ->
      new_char = encode_char(c)

      if new_char do
        acc ++ [new_char]
      else
        acc
      end
    end)
    |> Enum.chunk_every(5)
    |> Enum.map(&Enum.join(&1, ""))
    |> Enum.join(" ")
  end

  defp encode_char(c) when c in @numbers,
    do: c

  defp encode_char(c) when c in @alphabet,
    do: List.to_string([?z - Enum.find_index(@alphabet, fn x -> x == c end)])

  defp encode_char(_c),
    do: nil

  @spec decode(String.t()) :: String.t()
  def decode(cipher) do
    cipher
    |> String.split()
    |> Enum.join()
    |> String.codepoints()
    |> Enum.reduce([], fn c, acc ->
      acc ++ [decode_char(c)]
    end)
    |> Enum.join()
  end

  defp decode_char(c) when c in @numbers,
    do: c

  defp decode_char(c),
    do: List.to_string([?z - Enum.find_index(@alphabet, fn x -> x == c end)])
end
