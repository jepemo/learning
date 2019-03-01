defmodule PigLatin do

  # @vowels [?a, ?e, ?i, ?o, ?u]
  @vowels ["a", "e", "i", "o", "u"]
  @consonants ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

  @doc """
  Given a `phrase`, translate it a word at a time to Pig Latin.

  Words beginning with consonants should have the consonant moved to the end of
  the word, followed by "ay".

  Words beginning with vowels (aeiou) should have "ay" added to the end of the
  word.

  Some groups of letters are treated like consonants, including "ch", "qu",
  "squ", "th", "thr", and "sch".

  Some groups are treated like vowels, including "yt" and "xr".
  """
  @spec translate(phrase :: String.t()) :: String.t()
  def translate(phrase) do
    phrase
    |> String.split()
    |> Enum.map(&(translate2(&1)))
    |> Enum.join(" ")
  end
  def translate2(<<first_letter::bytes-size(1)>> <> _ = phrase) when first_letter in @vowels do
    phrase <> "ay"
  end
  def translate2(<<first_letter::bytes-size(1)>> <> <<qu::bytes-size(2)>> <> _ = phrase) when first_letter in @vowels and qu == "qu" do
    phrase <> "ay"
  end
  def translate2("qu" <> rest) do
    rest <> "quay"
  end
  def translate2(<<first_letter::bytes-size(1)>> <> "qu" <> rest) when first_letter in @consonants do
    rest <> "squay"
  end
  def translate2("x" <> <<sl::bytes-size(1)>> <> _ = phrase) when sl in @consonants do
    phrase <> "ay"
  end
  def translate2("y" <> <<sl::bytes-size(1)>> <> _ = phrase) when sl in @consonants do
    phrase <> "ay"
  end
  def translate2(<<first_letter::bytes-size(1)>> <> _ = phrase) when first_letter in @consonants do
    {prefix, sufix} = get_consonant_prefix(phrase)
    sufix <> prefix <> "ay"
  end
  def translate2(phrase) do
    phrase
  end

  def get_consonant_prefix(phrase) do
    phrase
    |> String.codepoints
    |> Enum.reduce({"", ""}, fn x, {prefix, suffix} ->
      case x do
        x when x in @consonants and suffix == "" ->
          {prefix <> x, suffix}
        _ ->
          {prefix, suffix <> x}
      end
    end)
  end
end
