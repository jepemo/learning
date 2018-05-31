defmodule AEDTest.Math.Fibonacci do
  use ExUnit.Case
  import AED.Math.Fibonacci
  doctest AED.Math.Fibonacci

  test "Fibonacci tests" do
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
  end
end
