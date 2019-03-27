defmodule Garden do
  @doc """
    Accepts a string representing the arrangement of cups on a windowsill and a
    list with names of students in the class. The student names list does not
    have to be in alphabetical order.

    It decodes that string into the various gardens for each student and returns
    that information in a map.
  """

  @plants %{
    "G" => :grass,
    "C" => :clover,
    "R" => :radishes,
    "V" => :violets
  }

  @default_students [
    :alice,
    :bob,
    :charlie,
    :david,
    :eve,
    :fred,
    :ginny,
    :harriet,
    :ileana,
    :joseph,
    :kincaid,
    :larry
  ]

  @max_plants_student_row 2

  @spec info(String.t(), list) :: map
  def info(info_string, student_names \\ @default_students) do
    initial_state = student_names |> Enum.map(&({&1, {}})) |> Enum.into(%{})

    info_string
    |> String.split("\n")
    |> Enum.reduce(initial_state, fn r, past_state ->
      assign_plants(String.codepoints(r), Enum.sort(student_names), 1, past_state)
    end)
  end

  def assign_plants([], _student_names, _num_it, result),
    do: result
  def assign_plants([p1 | r1], [student | rest_students] = students, num_it, result) do
    new_assigned_plants = {@plants[p1]}
    new_result = Map.update(result, student, new_assigned_plants, &(concat(&1, new_assigned_plants)))

    if num_it == @max_plants_student_row do
      assign_plants(r1, rest_students, 1, new_result)
    else
      assign_plants(r1, students, num_it+1, new_result)
    end
  end

  defp concat(t1, t2) do
    List.to_tuple(
      Tuple.to_list(t1) ++ Tuple.to_list(t2)
    )
  end
end
