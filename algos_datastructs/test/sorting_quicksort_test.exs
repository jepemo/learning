defmodule AEDTest.Sorting.QuickSort do
  use ExUnit.Case
  import AED.Sorting.QuickSort
  doctest AED.Sorting.QuickSort

  test "Quicksort tests" do
    assert quicksort([]) == []
    assert quicksort([3, 2, 1]) == [1, 2, 3]
    assert quicksort([3, 3, 2, 2, 1]) == [1, 2, 2, 3, 3]
  end
end
