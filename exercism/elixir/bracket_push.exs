defmodule BracketPush do
  @doc """
  Checks that all the brackets and braces in the string are matched correctly, and nested correctly
  """
  @spec check_brackets(String.t()) :: boolean
  def check_brackets(""), do: true
  def check_brackets(str) do
    str
    |> String.replace(~r/[^(){}\[\]]/, "")
    |> String.codepoints()
    |> do_check_brackets([])
  end

  def do_check_brackets([], []), do: true
  def do_check_brackets([], res) when length(res) > 0, do: false
  def do_check_brackets([h | _], []) when h in ["}", "]", ")"], do: false
  def do_check_brackets(["(" | t], res) do
    do_check_brackets(t, [")" | res])
  end
  def do_check_brackets(["{" | t], res) do
    do_check_brackets(t, ["}" | res])
  end
  def do_check_brackets(["[" | t], res) do
    do_check_brackets(t, ["]" | res])
  end
  def do_check_brackets(["]" | t], ["]" | r]) do
    do_check_brackets(t, r)
  end
  def do_check_brackets(["}" | t], ["}" | r]) do
    do_check_brackets(t, r)
  end
  def do_check_brackets([")" | t], [")" | r]) do
    do_check_brackets(t, r)
  end

  def do_check_brackets([_ | _], [_ | _]), do: false
end
