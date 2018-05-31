defmodule AED.List.Stack do
    def push(list, v) when is_list(v), do: v ++ list
    def push(list, v), do: [v] ++ list

    def pop([]), do: {nil, []}
    def pop([v|t]), do: {v, t}

    def peek([]), do: nil
    def peek([v|_]), do: v

    def is_empty([]), do: True
    def is_empty([_|_]), do: False
end
