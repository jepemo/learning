defmodule Matrix do
  defstruct matrix: nil

  @doc """
  Convert an `input` string, with rows separated by newlines and values
  separated by single spaces, into a `Matrix` struct.
  """
  @spec from_string(input :: String.t()) :: %Matrix{}
  def from_string(input) do
    matrix = input
    |> String.split("\n")
    |> Enum.map(fn row ->
      row
      |> String.split()
      |> Enum.map(fn value ->
        {int, _} = Integer.parse(value)
        int
      end)
    end)

    %Matrix{matrix: matrix}
  end

  @doc """
  Write the `matrix` out as a string, with rows separated by newlines and
  values separated by single spaces.
  """
  @spec to_string(matrix :: %Matrix{}) :: String.t()
  def to_string(%Matrix{matrix: matrix}) do
    matrix
    |> Enum.map(fn row -> 
      Enum.join(row, " ") <> "\n"
    end)
    |> Enum.join()
    |> String.slice(0..-2)
  end

  @doc """
  Given a `matrix`, return its rows as a list of lists of integers.
  """
  @spec rows(matrix :: %Matrix{}) :: list(list(integer))
  def rows(matrix) do
    matrix.matrix
  end

  @doc """
  Given a `matrix` and `index`, return the row at `index`.
  """
  @spec row(matrix :: %Matrix{}, index :: integer) :: list(integer)
  def row(matrix, index) do
    Enum.at(rows(matrix), index)
  end

  @doc """
  Given a `matrix`, return its columns as a list of lists of integers.
  """
  @spec columns(matrix :: %Matrix{}) :: list(list(integer))
  def columns(matrix) do
    traspose(matrix.matrix)
  end

  @doc """
  Given a `matrix` and `index`, return the column at `index`.
  """
  @spec column(matrix :: %Matrix{}, index :: integer) :: list(integer)
  def column(matrix, index) do
    Enum.at(columns(matrix), index)
  end

  defp traspose(matrix) do
    matrix
    |> Enum.zip()
    |> Enum.map(&(Tuple.to_list(&1)))
  end
end
