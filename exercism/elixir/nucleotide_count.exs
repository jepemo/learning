defmodule NucleotideCount do
  @nucleotides [?A, ?C, ?G, ?T]

  @doc """
  Counts individual nucleotides in a DNA strand.

  ## Examples

  iex> NucleotideCount.count('AATAA', ?A)
  4

  iex> NucleotideCount.count('AATAA', ?T)
  1
  """
  @spec count([char], char) :: non_neg_integer
  def count(strand, nucleotide) do
    strand |> Enum.filter(&(&1 == nucleotide)) |> Enum.count
  end

  @doc """
  Returns a summary of counts by nucleotide.

  ## Examples

  iex> NucleotideCount.histogram('AATAA')
  %{?A => 4, ?T => 1, ?C => 0, ?G => 0}
  """
  @spec histogram([char]) :: map
  def histogram(strand) do
    strand
    |> Enum.group_by(fn x -> x end) 
    |> Enum.map(fn {k,v} -> {k, Enum.count(v)} end) 
    |> Enum.into(%{})
    |> Enum.map(&(fill(&1, @nucleotides)))
  end

  def fill(histo, []), do: histo
  def fill(histo, [h | t]) do
    case Map.fetch(histo, h) do
      :error -> 
        fill(Map.put(histo, h, 0), t)
      _ ->
        fill(histo, t)
    end
  end
end
