defmodule AED.List.LinkedList do
    defstruct value: nil, next: nil
    """
    def insert(%{next: nil}, value) do

    end
    def insert(list, value)  do
        insert(list.next, value)
    end
    """
end
