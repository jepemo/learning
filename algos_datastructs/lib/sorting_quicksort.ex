defmodule AED.Sorting.QuickSort do
    @doc """
    """
    def quicksort([]), do: []
    def quicksort([h|t]) do
        min = Enum.filter(t, fn x -> x <= h end)
        max = Enum.filter(t, fn x -> x > h end)
        quicksort(min) ++ [h] ++ quicksort(max)
    end
end
