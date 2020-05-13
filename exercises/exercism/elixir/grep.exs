defmodule Grep do
  @spec grep(String.t(), [String.t()], [String.t()]) :: String.t()
  def grep(pattern, flags, files) do
    regex = get_regex(pattern, flags)

    flags = List.delete(flags, "-x")
    flags = List.delete(flags, "-i")
    flags = List.delete(flags, "-v")
    # Solo queda -l/-n
    grep(regex, flags, files, Enum.count(files) > 1, [])
  end

  defp grep(_regex, _flags, [], _show_filename, res) when length(res) > 0 do
    v = Enum.join(res, "\n")
    if String.ends_with?(v, "\n") do
      v
    else
      v <> "\n"
    end
  end
  defp grep(_regex, _flags, [], _show_filename, _res),
    do: ""

  defp grep(regex, flags, [file | more_files], show_filename, res) do
    file_content = File.read!(file)
    lines = String.split(file_content, "\n")
    lines_with_numbers = Enum.zip(1..Enum.count(lines), lines)

    file_result = grep_file(regex, List.delete(flags, "-l"), lines_with_numbers, [])

    file_result = if show_filename or "-l" in flags do
      file_result
      |> Enum.filter(fn line ->
        line != "\n" and line != ""
      end)
      |> Enum.map(fn line ->
        "#{file}:#{line}"
      end)
    else
      file_result
    end

    file_result = if "-l" in flags do
      file_result
      |> Enum.map(fn line ->
        [filename | _rest] = String.split(line, ":")
        filename
      end)
      |> Enum.uniq()
    else
      file_result
    end

    grep(regex, flags, more_files, show_filename, res ++ file_result)
  end

  defp grep_file(_regex, _flags, [], res), do: res

  defp grep_file(regex, flags, [number_and_line | more_lines], res) do
    line_result = grep_file_flag(regex, flags, number_and_line, "")
    grep_file(regex, flags, more_lines, res ++ line_result)
  end

  defp grep_file_flag(regex, ["-n" | more_flags], {number, line}, _res),
    do: grep_file_flag(regex, more_flags, {number, line}, "#{number}:")

  defp grep_file_flag(regex, [], {_number, line}, res) do
    if Regex.match?(regex, line) do
      ["#{res}#{line}"]
    else
      []
    end
  end

  defp get_regex(pattern, flags) do
    new_pattern = if "-v" in flags, do: "^((?!#{pattern}).)*$", else: pattern
    new_pattern = if "-x" in flags, do: "^#{pattern}$", else: new_pattern

    args = if "-i" in flags, do: "i", else: ""

    Regex.compile!(new_pattern, args)
  end
end
