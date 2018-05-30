defmodule AEDTest.List.SingleLinkedList do
  use ExUnit.Case
  alias AED.List.SingleLinkedList, as: SLL
  doctest AED.List.SingleLinkedList

  test "Single linked list-1, Append a simple element and a list" do
    list = []
      |> SLL.append(1)
      |> SLL.append([2, 3])

    assert list == [1, 2, 3]
    # IO.inspect list, label: ""
  end

  test "Single linked list-1, prepend a simple element and a list" do
    list = []
      |> SLL.append([3, 4])
      |> SLL.prepend(2)
      |> SLL.prepend([1])

    assert list == [1, 2, 3, 4]
    #IO.inspect list, label: ""
  end

  test "Single linked list-1, delete elements" do
    list = []
      |> SLL.append([1, 2, 3, 1, 5, 1, 2])
      |> SLL.delete(2)

    assert list == [1, 3, 1, 5, 1]
    # IO.inspect list

    list = []
      |> SLL.append([1, 2, 3, 1, 5, 1, 2])
      |> SLL.delete(1)
      |> SLL.delete(2)

    assert list == [3, 5]
  end

  test "Single linked list-1, delete empty list" do
    list = []
      |> SLL.delete(2)

    assert list == []
    # IO.inspect list
  end
end
