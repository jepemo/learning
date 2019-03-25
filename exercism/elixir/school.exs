defmodule School do
  @moduledoc """
  Simulate students in a school.

  Each student is in a grade.
  """

  @doc """
  Add a student to a particular grade in school.
  """
  @spec add(map, String.t(), integer) :: map
  def add(db, name, grade) do
    {_, updated_db} = Map.get_and_update(db, grade, fn current_value ->
      case current_value do
        nil -> {current_value, [name]}
        _ -> {current_value, [name | current_value]}
      end
    end)

    updated_db
  end

  @doc """
  Return the names of the students in a particular grade.
  """
  @spec grade(map, integer) :: [String.t()]
  def grade(db, grade) do
    case Map.has_key?(db, grade) do
      true -> db[grade]
      false -> []
    end
  end

  @doc """
  Sorts the school by grade and name.
  """
  @spec sort(map) :: [{integer, [String.t()]}]
  def sort(db) do
    db 
    |> Map.keys() 
    |> Enum.sort()
    |> Enum.map(fn grade ->
      {grade, Enum.sort(db[grade])}
    end)
  end
end
