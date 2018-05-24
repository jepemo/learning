defmodule AEDTest.Math do
  use ExUnit.Case
  doctest AED.Math

  test "greets the world" do
    assert AED.Math.factorial(0) == 1
    assert AED.Math.factorial(1) == 1
    assert AED.Math.factorial(5) == 120
    assert AED.Math.factorial(8) == 40320
    assert AED.Math.factorial(10) == 3628800
  end
end
