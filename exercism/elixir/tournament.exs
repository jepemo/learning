defmodule Tournament do
  @doc """
  Given `input` lines representing two teams and whether the first of them won,
  lost, or reached a draw, separated by semicolons, calculate the statistics
  for each team's number of games played, won, drawn, lost, and total points
  for the season, and return a nicely-formatted string table.

  A win earns a team 3 points, a draw earns 1 point, and a loss earns nothing.

  Order the outcome by most total points for the season, and settle ties by
  listing the teams in alphabetical order.
  """
  @spec tally(input :: list(String.t())) :: String.t()
  def tally(input) do
    input
    |> Enum.map(fn line ->
      case List.to_tuple(String.split(line, ";")) do
        {t1, t2, "win"} ->
          [%{team: t1, points: 3, played: 1, won: 1, drawn: 0, lost: 0},
           %{team: t2, points: 0, played: 1, won: 0, drawn: 0, lost: 1}]
        {t1, t2, "loss"} ->
          [%{team: t1, points: 0, played: 1, won: 0, drawn: 0, lost: 1},
           %{team: t2, points: 3, played: 1, won: 1, drawn: 0, lost: 0}]
        {t1, t2, "draw"} ->
          [%{team: t1, points: 1, played: 1, won: 0, drawn: 1, lost: 0},
           %{team: t2, points: 1, played: 1, won: 0, drawn: 1, lost: 0}]
        _
          ->
            []
      end
    end)
    |> List.flatten()
    |> merge()
    |> Enum.sort(&(&1.points >= &2.points))
    |> print()
  end

  defp merge(registers) do
    Enum.reduce(registers, %{}, fn register, acc ->
      if not Map.has_key?(acc, register.team) do
        Map.put(acc, register.team, register)
      else
        elem = acc[register.team]

        elem = %{elem | points: elem.points + register.points}
        elem = %{elem | played: elem.played + register.played}
        elem = %{elem | won: elem.won + register.won}
        elem = %{elem | drawn: elem.drawn + register.drawn}
        elem = %{elem | lost: elem.lost + register.lost}

        Map.put(acc, register.team, elem)
      end
    end)
    |> Map.values()
  end

  defp print(registers) do
    header = "Team                           | MP |  W |  D |  L |  P\n"
    Enum.reduce(registers, header, fn register, acc ->
      acc <>
      String.pad_trailing(register.team, 31) <>
      "|" <>
      String.pad_leading("#{register.played}", 3) <>
      " |" <>
      String.pad_leading("#{register.won}", 3) <>
      " |" <>
      String.pad_leading("#{register.drawn}", 3) <>
      " |" <>
      String.pad_leading("#{register.lost}", 3) <>
      " |" <>
      String.pad_leading("#{register.points}", 3) <>
      "\n"
    end)
    |> String.slice(0..-2)
  end
end
