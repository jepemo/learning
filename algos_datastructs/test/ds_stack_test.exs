defmodule AEDTest.List.Stack do
  use ExUnit.Case
  import AED.List.Stack
  doctest AED.List.Stack

  test "Stack, push elements" do
    stack = []
      |> push(1)
      |> push([2, 3, 4])

    #IO.inspect queue
    assert stack == [2, 3, 4, 1]
  end

  test "Stack, pop elements" do
      {value, stack} = []
        |> pop()

      assert stack == []
      assert value == nil

      {value, stack} = []
        |> push([3, 2, 1])
        |> pop()

      assert stack == [2, 1]
      assert value == 3
  end

  test "Stack, peek" do
      value = []
        |> peek()

      assert value == nil

      value = []
        |> push([3, 2, 1])
        |> peek()

      assert value == 3
  end

  test "Stack is empty" do
      empty? = []
        |> is_empty()

      assert empty? == True

      empty? = []
        |> push([1, 2, 3])
        |> is_empty()

      assert empty? == False
  end
end
