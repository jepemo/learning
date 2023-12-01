defmodule AdventOfCode.Day01Test do
  use ExUnit.Case

  import AdventOfCode.Day01

  @tag :skip
  test "part1" do
    input = """
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """

    result = part1(input)

    assert result == 142
  end

  # @tag :skip
  test "part2" do
    input = """
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    """

    # input = """
    # sevendjsfjzhpcs7
    # 35vgsndjpcpfourmzzbbonejfvdtb
    # jqvxrhrljclhmtlfjr4nine4
    # zctcbf5twosevenhzt
    # 2six886nine2four
    # 1vmlheightgn8cbdqfznl
    # sixfivexmbgfourthreeone3fourtwo
    # sixseven3bxdncvhpdsevensqbmzthreeseven
    # four5sixeight6
    # 9nine29gcgklf
    # five833three59seven
    # """

    result = part2(input)

    assert result == 281
  end
end
