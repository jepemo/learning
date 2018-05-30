defmodule AED.Math.Fibonacci do
    @doc """
    The Fibonacci numbers are the numbers in the following integer sequence,
    called the Fibonacci sequence, and characterized by the fact that every
    number after the first two is the sum of the two preceding ones

    f(n) = { 0  if n = 0 }
         = { 1  if n = 1 }
         = { f(n-1) + f(n-2) if n > 1}

    Example:
      factorial(1) == 1
      factorial(2) == 1
      factorial(3) == 2
    """
    def fibonacci(number) when number < 2, do: number
    def fibonacci(number) do
        fibonacci(number-1)+fibonacci(number-2)
    end
end
