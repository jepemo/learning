defmodule Acronym do
  @doc """
  Generate an acronym from a string.
  "This is a string" => "TIAS"
  """
  @spec abbreviate(String.t()) :: String.t()
  def abbreviate(string) do
    do_abbreviate(String.codepoints(string), [], false)
  end

  def do_abbreviate([ c | rest], result, true) do
    do_abbreviate(rest, [String.upcase(c) | result], false)
  end
  def do_abbreviate([ c | rest], result, _next_acronim) do
    if c in ignored_characters() do
      do_abbreviate(rest, result, false)
    else
      if c == " " do
        do_abbreviate(rest, result, true)
      else
          if String.upcase(c) == c do
              do_abbreviate(rest, [c | result], false)
          else
              do_abbreviate(rest, result, false)
          end
      end
    end
  end
  def do_abbreviate([], result, _) do
    result
    |> Enum.reverse()
    |> Enum.join("")
  end

  def ignored_characters do
    ["-", ","]
  end
end
