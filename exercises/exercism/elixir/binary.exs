defmodule Binary do
  @doc """
  Convert a string containing a binary number to an integer.

  On errors returns 0.
  """
  @spec to_decimal(String.t()) :: non_neg_integer
  def to_decimal(string) do
    case parse_digits(string) do
      {:ok, digits} ->
        to_decimal(digits, 0, 0)

      :error ->
        0
    end
  end

  defp to_decimal([], _, result),
    do: result

  defp to_decimal([digit | rest], it, result),
    do: to_decimal(rest, it + 1, result + digit * :math.pow(2, it))

  defp parse_digits(string) do
    res =
      string
      |> String.codepoints()
      |> Enum.reverse()
      |> Enum.map(fn x ->
        case Integer.parse(x) do
          :error ->
            nil

          {val, _} ->
            if val > 1 or val < 0 do
              nil
            else
              val
            end
        end
      end)

    if Enum.member?(res, nil) or Enum.count(String.codepoints(string)) != Enum.count(res) do
      :error
    else
      {:ok, res}
    end
  end
end
