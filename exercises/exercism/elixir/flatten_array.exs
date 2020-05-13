defmodule FlattenArray do
  @doc """
    Accept a list and return the list flattened without nil values.

    ## Examples

      iex> FlattenArray.flatten([1, [2], 3, nil])
      [1,2,3]

      iex> FlattenArray.flatten([nil, nil])
      []

  """

  # require IEx

  @spec flatten(list) :: list
  def flatten(list) do
    # IEx.pry()
    do_flatten(list, [])
  end
  
  def do_flatten([], res), do: Enum.reverse(res)
  def do_flatten([nil | rest], res) do
    do_flatten(rest, res)
  end
  def do_flatten([[] | rest], res) do
    do_flatten(rest, res)
  end
  def do_flatten([[nil | r1] | rest], res) do
    do_flatten([r1 | rest], res)
  end
  def do_flatten([[v1 | r1] | rest], res) when is_list(v1) do
    do_flatten([v1 ++ r1 | rest], res)
  end
  def do_flatten([[v1 | r1] | rest], res) when not is_list(v1) do
    do_flatten(r1 ++ rest, [v1 | res])
  end
  def do_flatten([h1 | rest], res) do
    do_flatten(rest, [h1 | res])
  end
end
