defmodule RNATranscription do

  @transcription %{
    "G" => "C",
    "C" => "G",
    "T" => "A",
    "A" => "U"
  }

  @doc """
  Transcribes a character list representing DNA nucleotides to RNA

  ## Examples

  iex> RNATranscription.to_rna('ACTG')
  'UGAC'
  """
  @spec to_rna([char]) :: [char]
  def to_rna(dna) do
    dna
    |> String.Chars.to_string()
    |> String.codepoints()
    |> Enum.map(&(@transcription[&1]))
    |> Enum.join()
    |> String.to_charlist()
  end
end
