defmodule Gigasecond do
  @giga_seconds 1_000_000_000
  @doc """
  Calculate a date one billion seconds after an input date.
  """
  @spec from({{pos_integer, pos_integer, pos_integer}, {pos_integer, pos_integer, pos_integer}}) ::
          :calendar.datetime()

  def from({{year, month, day}, {hours, minutes, seconds}}) do
    {:ok, datetime, 0} =
      DateTime.from_iso8601("#{f(year)}-#{f(month)}-#{f(day)}T#{f(hours)}:#{f(minutes)}:#{f(seconds)}Z")

    future_date = DateTime.add(datetime, @giga_seconds, :second)
    {{future_date.year, future_date.month, future_date.day}, {future_date.hour, future_date.minute, future_date.second}}
  end

  def f(digit) when digit < 10, do: "0#{digit}"
  def f(digit), do: "#{digit}"
end
