defmodule ISBNVerifier do
  @digits ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]

  @doc """
    Checks if a string is a valid ISBN-10 identifier

    ## Examples

      iex> ISBNVerifier.isbn?("3-598-21507-X")
      true

      iex> ISBNVerifier.isbn?("3-598-2K507-0")
      false

  """
  @spec isbn?(String.t()) :: boolean
  def isbn?(
        <<
          i1::binary-size(1),
          "-",
          i2::binary-size(1),
          i3::binary-size(1),
          i4::binary-size(1),
          "-",
          i5::binary-size(1),
          i6::binary-size(1),
          i7::binary-size(1),
          i8::binary-size(1),
          i9::binary-size(1),
          "-",
          last::binary-size(1)
        >> = isbn
      )
      when is_binary(isbn) and
             i1 in @digits and
             i2 in @digits and
             i3 in @digits and
             i4 in @digits and
             i5 in @digits and
             i6 in @digits and
             i7 in @digits and
             i8 in @digits and
             i9 in @digits and
             last in @digits do
    isbn?([i1, i2, i3, i4, i5, i6, i7, i8, i9, last])
  end

  def isbn?(
        <<
          i1::binary-size(1),
          i2::binary-size(1),
          i3::binary-size(1),
          i4::binary-size(1),
          i5::binary-size(1),
          i6::binary-size(1),
          i7::binary-size(1),
          i8::binary-size(1),
          i9::binary-size(1),
          last::binary-size(1)
        >> = isbn
      )
      when is_binary(isbn) and
             i1 in @digits and
             i2 in @digits and
             i3 in @digits and
             i4 in @digits and
             i5 in @digits and
             i6 in @digits and
             i7 in @digits and
             i8 in @digits and
             i9 in @digits and
             last in @digits do
    isbn?([i1, i2, i3, i4, i5, i6, i7, i8, i9, last])
  end

  def isbn?(value) when is_binary(value), do: false

  def isbn?(list) when is_list(list) do
    sum =
      list
      |> Enum.map(fn x ->
        if x == "X" do
          10
        else
          {val, _} = Integer.parse(x)
          val
        end
      end)
      |> Enum.zip(10..1)
      |> Enum.reduce(0, fn {v, ind}, acc ->
        acc + v * ind
      end)

    rem(sum, 11) == 0
  end
end
