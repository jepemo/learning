defmodule SimpleCipher do
  @alphabet ?a..?z |> Enum.map(&to_string(List.to_charlist([&1])))

  @doc """
  Given a `plaintext` and `key`, encode each character of the `plaintext` by
  shifting it by the corresponding letter in the alphabet shifted by the number
  of letters represented by the `key` character, repeating the `key` if it is
  shorter than the `plaintext`.

  For example, for the letter 'd', the alphabet is rotated to become:

  defghijklmnopqrstuvwxyzabc

  You would encode the `plaintext` by taking the current letter and mapping it
  to the letter in the same position in this rotated alphabet.

  abcdefghijklmnopqrstuvwxyz
  defghijklmnopqrstuvwxyzabc

  "a" becomes "d", "t" becomes "w", etc...

  Each letter in the `plaintext` will be encoded with the alphabet of the `key`
  character in the same position. If the `key` is shorter than the `plaintext`,
  repeat the `key`.

  Example:

  plaintext = "testing"
  key = "abc"

  The key should repeat to become the same length as the text, becoming
  "abcabca". If the key is longer than the text, only use as many letters of it
  as are necessary.
  """
  def encode(plaintext, key) do
    new_key = get_key(key, String.length(plaintext))
    encode(String.codepoints(plaintext), String.codepoints(new_key), [])
  end

  defp get_key(key, size),
    do: String.duplicate(key, div(size, String.length(key)) + 1) |> String.slice(0, size)

  defp encode([], [], res),
    do: res |> Enum.reverse() |> Enum.join()

  defp encode([p | rest], [k | rest_k], res),
    do: encode(rest, rest_k, [encode_char(p, k) | res])

  defp encode_char(c, k) do
    index_c = Enum.find_index(@alphabet, fn x -> x == c end)
    index_k = Enum.find_index(@alphabet, fn x -> x == k end)

    if index_c do
      Enum.at(@alphabet, rem(index_k + index_c, Enum.count(@alphabet)))
    else
      c
    end
  end

  @doc """
  Given a `ciphertext` and `key`, decode each character of the `ciphertext` by
  finding the corresponding letter in the alphabet shifted by the number of
  letters represented by the `key` character, repeating the `key` if it is
  shorter than the `ciphertext`.

  The same rules for key length and shifted alphabets apply as in `encode/2`,
  but you will go the opposite way, so "d" becomes "a", "w" becomes "t",
  etc..., depending on how much you shift the alphabet.
  """
  def decode(ciphertext, key) do
    new_key = get_key(key, String.length(ciphertext))
    decode(String.codepoints(ciphertext), String.codepoints(new_key), [])
  end

  defp decode([], [], res),
    do: res |> Enum.reverse() |> Enum.join()

  defp decode([p | rest], [k | rest_k], res),
    do: decode(rest, rest_k, [decode_char(p, k) | res])

  defp decode_char(c, k) do
    index_c = Enum.find_index(@alphabet, fn x -> x == c end)
    index_k = Enum.find_index(@alphabet, fn x -> x == k end)

    if index_c do
      Enum.at(@alphabet, rem(index_c-index_k, Enum.count(@alphabet)))
    else
      c
    end
  end
end
