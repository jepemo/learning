defmodule AEDTest.Math.Factorial do
  use ExUnit.Case
  import AED.Math.Factorial
  doctest AED.Math.Fibonacci

  test "Factorial tests" do
    assert factorial(-1000) == 1
    assert factorial(-1) == 1
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(8) == 40320
    assert factorial(10) == 3628800
  end
end
