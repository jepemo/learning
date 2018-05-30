defmodule AEDTest.List.Queue do
  use ExUnit.Case
  import AED.List.Queue
  doctest AED.List.Queue

  test "Queue, enqueue elements" do
    queue = []
      |> enqueue(1)
      |> enqueue([2, 3, 4])

    #IO.inspect queue
    assert queue == [2, 3, 4, 1]
  end

  test "Queue, testing peek" do
    queue = []
      |> enqueue([3, 2, 1])

    assert peek(queue) == 1

    queue = []
    assert peek(queue) == nil

    queue = []
      |> enqueue(2)
    assert peek(queue) == 2
  end

  test "Queue, is empty" do
    queue = []
    assert is_empty(queue) == True

    queue = []
      |> enqueue([1, 2, 3])
    assert is_empty(queue) == False
  end

  test "Queue, Dequeue" do
    {val, rest} = []
      |> dequeue()

    assert val == nil
    assert rest == []

    {val, rest} = []
      |> enqueue(1)
      |> dequeue()

    assert val == 1
    assert rest == []

    {val, rest} = []
      |> enqueue([1, 2])
      |> dequeue()

    assert val == 2
    assert rest == [1]

    {val, rest} = []
      |> enqueue([1, 2, 3])
      |> dequeue()

    assert val == 3
    assert rest == [1, 2]
  end
end
