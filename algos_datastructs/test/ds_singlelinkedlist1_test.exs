defmodule AEDTest.List.SingleLinkedList do
  use ExUnit.Case
  import AED.List.SingleLinkedList
  doctest AED.List.SingleLinkedList

  test "Single linked list-1, Append a simple element and a list" do
    list = []
      |> append(1)
      |> append([2, 3])

    assert list == [1, 2, 3]
    # IO.inspect list, label: ""
  end

  test "Single linked list-1, prepend a simple element and a list" do
    list = []
      |> append([3, 4])
      |> prepend(2)
      |> prepend([1])

    assert list == [1, 2, 3, 4]
    #IO.inspect list, label: ""
  end

  test "Single linked list-1, delete elements" do
    list = []
      |> append([1, 2, 3, 1, 5, 1, 2])
      |> delete(2)

    assert list == [1, 3, 1, 5, 1]
    # IO.inspect list

    list = []
      |> append([1, 2, 3, 1, 5, 1, 2])
      |> delete(1)
      |> delete(2)

    assert list == [3, 5]
  end

  test "Single linked list-1, delete empty list" do
    list = []
      |> delete(2)

    assert list == []
    # IO.inspect list
  end
end
