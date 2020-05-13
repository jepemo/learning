defmodule Solution do
    def input do
      IO.stream(:stdio, :line)
      |> Enum.to_list
      |> Enum.map(&String.trim/1)
      |> Enum.map(&String.to_integer/1)
    end
    
    defp show(x, [h | t]) when h < x do
        IO.puts(h)
        show x, t
    end
    defp show(x, [_ | t]) do
        show x, t
    end
    defp show(_, []) do
    end

    def main(list) do
        [head | tail] = list
        show head, tail
    end
end

Solution.input |> Solution.main
