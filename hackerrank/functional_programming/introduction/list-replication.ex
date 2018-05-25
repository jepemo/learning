defmodule Solution do
    defmodule F do
        def p(1, x), do: IO.puts(x)
        def p(rep, x) do
            IO.puts(x)
            p(rep-1, x)
        end
    end

    [s | tail] = String.split(IO.read(:stdio, :all), [" ", "\n"])
    {k, _} = Integer.parse(s)
    Enum.map(tail, fn x ->
        F.p(k, x)
    end)
end
