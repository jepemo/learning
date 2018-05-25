defmodule AED.Math do
    def factorial(number) when number <= 0 do
        1
    end
    def factorial(number) do
        number * factorial(number-1)
    end
end
