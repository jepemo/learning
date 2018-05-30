defmodule AED.Math.Factorial do
    @doc """
    The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n

    Example:
      factorial(3) == 6
    """
    def factorial(number) when number <= 0, do: 1
    def factorial(number) do
        number * factorial(number-1)
    end
end
