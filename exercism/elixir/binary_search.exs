defmodule BinarySearch do
  @doc """
    Searches for a key in the tuple using the binary search algorithm.
    It returns :not_found if the key is not in the tuple.
    Otherwise returns {:ok, index}.

    ## Examples

      iex> BinarySearch.search({}, 2)
      :not_found

      iex> BinarySearch.search({1, 3, 5}, 2)
      :not_found

      iex> BinarySearch.search({1, 3, 5}, 5)
      {:ok, 2}

  """

  @spec search(tuple, integer) :: {:ok, integer} | :not_found
  def search(numbers, key) do
    search(Tuple.to_list(numbers), key, 0, tuple_size(numbers) - 1)
  end

  def search(_arr, _x, left, right) when right < left, do: :not_found

  def search(arr, x, left, right) do
    mid_index = left + div(right - left, 2)
    mid_elem = Enum.at(arr, mid_index)
    search_m(arr, x, left, right, mid_index, mid_elem)
  end

  defp search_m(_arr, x, _left, _right, mid, elem) when elem == x,
    do: {:ok, mid}

  defp search_m(arr, x, left, _right, mid, elem) when elem > x,
    do: search(arr, x, left, mid - 1)

  defp search_m(arr, x, _left, right, mid, _elem),
    do: search(arr, x, mid + 1, right)
end
