defmodule AED.List.SingleLinkedList do
    def append(list, value) when is_list(value), do: list ++ value
    def append(list, value), do: list ++ [value]

    def prepend(list, value) when is_list(value), do: value ++ list
    def prepend(list, value), do: [value] ++ list

    defp delete(hl, [], _), do: hl ++ []
    defp delete(hl, [value | t], value), do: delete(hl, t, value)
    defp delete(hl, [h | t], value), do: delete(hl ++ [h], t, value)
    #def delete([], value), do: []
    #def delete([value | t], value), do: delete([], t, value)
    #def delete([h | t], value), do:  delete([h], t, value)
    def delete(list, value) do
      case list do
        [] -> []
        [^value | t] -> delete([], t, value)
        [h | t] -> delete([h], t, value)
      end
    end
end
