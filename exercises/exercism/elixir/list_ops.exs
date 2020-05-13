defmodule ListOps do
  # Please don't use any external modules (especially List or Enum) in your
  # implementation. The point of this exercise is to create these basic
  # functions yourself. You may use basic Kernel functions (like `Kernel.+/2`
  # for adding numbers), but please do not use Kernel functions for Lists like
  # `++`, `--`, `hd`, `tl`, `in`, and `length`.

  @spec count(list) :: non_neg_integer
  def count(list),
    do: count(list, 0)

  def count([], res),
    do: res

  def count([_e | next], res),
    do: count(next, res + 1)

  @spec reverse(list) :: list
  def reverse(l),
    do: reverse(l, [])

  def reverse([], res),
    do: res

  def reverse([e | next], res),
    do: reverse(next, [e | res])

  @spec map(list, (any -> any)) :: list
  def map(l, f),
    do: map(l, f, [])

  def map([], _f, res),
    do: reverse(res)

  def map([e | rest], f, res),
    do: map(rest, f, [f.(e) | res])

  @spec filter(list, (any -> as_boolean(term))) :: list
  def filter(l, f),
    do: filter(l, f, [])

  def filter([], _f, res),
    do: reverse(res)

  def filter([e | rest], f, res),
    do: filter(rest, f, if(f.(e), do: [e | res], else: res))

  @type acc :: any
  @spec reduce(list, acc, (any, acc -> acc)) :: acc
  def reduce([], acc, _f),
    do: acc

  def reduce([e | rest], acc, f) do
    reduce(rest, f.(e, acc), f)
  end

  @spec append(list, list) :: list
  def append(a, b),
    do: do_append(b, reverse(a))

  defp do_append([], res),
    do: reverse(res)

  defp do_append([e | rest], res),
    do: do_append(rest, [e | res])

  @spec concat([[any]]) :: [any]
  def concat(ll) do
    do_concat(ll, [])
  end

  defp do_concat([], res),
    do: reverse(res)

  defp do_concat([e | rest], res) do
    do_concat(rest, concat_sublist(e, res))
  end

  defp concat_sublist([], res),
    do: res

  defp concat_sublist([e | rest], res),
    do: concat_sublist(rest, [e | res])
end
