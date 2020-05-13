defmodule Bob do
  def hey(input) do
    cond do
      silence?(input) -> "Fine. Be that way!"
      shouting_question?(input) -> "Calm down, I know what I'm doing!"
      shouting?(input) -> "Whoa, chill out!"
      question?(input) -> "Sure."
      true -> "Whatever."
    end
  end

  defp shouting?(input) do
    contains_alpha?(input) and (upcase?(input) or (upcase?(input) and String.ends_with?(input, "!")))
  end

  defp shouting_question?(input) do
    contains_alpha?(input) and contains_alpha?(input) and upcase?(input) and String.ends_with?(input, "?")
  end

  defp question?(input) do
    String.ends_with?(input, "?")
  end

  defp silence?(input) do
    String.trim(input) == ""
  end

  defp upcase?(input) do
    # String.match?(input, ~r/^[[:alnum:]]+$/) and
    input == String.upcase(input)
  end

  defp contains_alpha?(input) do
    String.match?(input, ~r/^.*[[:alpha:]]+.*$/)
  end
end
