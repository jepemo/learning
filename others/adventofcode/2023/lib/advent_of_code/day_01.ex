defmodule AdventOfCode.Day01 do
  def part1(args) do
    args
    |> String.split("\n")
    |> Enum.filter(&(&1 != ""))
    |> Enum.map(&get_calibration_value/1)
    |> Enum.sum()
  end

  defp get_calibration_value(line) do
    line
    |> String.graphemes()
    |> Enum.filter(fn val ->
      Integer.parse(val) != :error
    end)
    |> (fn values ->
          if length(values) > 1 do
            "#{Enum.at(values, 0)}#{Enum.at(values, length(values) - 1)}"
          else
            "#{Enum.at(values, 0)}#{Enum.at(values, 0)}"
          end
        end).()
    |> Integer.parse()
    |> elem(0)
  end

  def part2(args) do
    args
    |> String.split("\n")
    |> Enum.filter(&(&1 != ""))
    |> Enum.map(&get_calibration_value_with_letters/1)
    |> IO.inspect()
    |> Enum.sum()
  end

  @text_numbers %{
    "one" => 1,
    "two" => 2,
    "three" => 3,
    "four" => 4,
    "five" => 5,
    "six" => 6,
    "seven" => 7,
    "eight" => 8,
    "nine" => 9,
    "1" => 1,
    "2" => 2,
    "3" => 3,
    "4" => 4,
    "5" => 5,
    "6" => 6,
    "7" => 7,
    "8" => 8,
    "9" => 9
  }

  defp get_calibration_value_with_letters(line) do
    IO.inspect(line)

    positions =
      get_positions(line, 0, %{})

    min = Enum.min(Map.keys(positions))
    max = Enum.max(Map.keys(positions))

    "#{positions[min]}#{positions[max]}" |> Integer.parse() |> elem(0) |> IO.inspect()
  end

  defp get_positions("", _current_pos, positions), do: positions

  defp get_positions(current_string, current_pos, positions) do
    digit = find_match(current_string)

    case digit do
      nil ->
        get_positions(
          String.slice(current_string, 1, String.length(current_string)),
          current_pos + 1,
          positions
        )

      value ->
        get_positions(
          String.slice(current_string, String.length(value), String.length(current_string)),
          current_pos + String.length(value),
          Map.put(positions, current_pos, @text_numbers[value])
        )
    end
  end

  defp find_match(string) do
    Map.keys(@text_numbers)
    |> Enum.reduce_while(nil, fn digit, _acc ->
      if String.starts_with?(string, digit) do
        {:halt, digit}
      else
        {:cont, nil}
      end
    end)
  end
end
