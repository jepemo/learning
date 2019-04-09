defmodule RobotSimulator do
  defstruct direction: nil, position: nil

  @valid_directions [:north, :south, :east, :west]
  @valid_instructions ["A", "L", "R"]
  @default_direction :north
  @default_position {0, 0}
  @doc """
  Create a Robot Simulator given an initial direction and position.

  Valid directions are: `:north`, `:east`, `:south`, `:west`
  """
  @spec create(direction :: atom, position :: {integer, integer}) :: any
  def create(),
    do: create(@default_direction, @default_position)

  def create(direction, {p1, p2} = position)
      when direction in @valid_directions and is_integer(p1) and is_integer(p2),
      do: %__MODULE__{direction: direction, position: position}

  def create(direction, _) when direction not in @valid_directions,
    do: {:error, "invalid direction"}

  def create(_, _),
    do: {:error, "invalid position"}

  @doc """
  Simulate the robot's movement given a string of instructions.

  Valid instructions are: "R" (turn right), "L", (turn left), and "A" (advance)
  """
  @spec simulate(robot :: any, instructions :: String.t()) :: any
  def simulate(robot, instructions) when is_binary(instructions) do
    steps = instructions
    |> String.codepoints()

    if valid_instructions?(steps) do
      simulate(robot, steps)
    else
      {:error, "invalid instruction"}
    end
  end
  def simulate(robot, instructions) when is_list(instructions) do
    instructions
    |> Enum.reduce(robot, fn step, acc ->
      update_robot(step, acc)
    end)
  end

  defp update_robot("A", %{direction: :north, position: {x, y}} = robot),
    do: %{robot | position: {x, y + 1}}

  defp update_robot("L", %{direction: :north} = robot),
    do: %{robot | direction: :west}

  defp update_robot("R", %{direction: :north} = robot),
    do: %{robot | direction: :east}

  defp update_robot("A", %{direction: :south, position: {x, y}} = robot),
    do: %{robot | position: {x, y - 1}}

  defp update_robot("L", %{direction: :south} = robot),
    do: %{robot | direction: :east}

  defp update_robot("R", %{direction: :south} = robot),
    do: %{robot | direction: :west}

  defp update_robot("A", %{direction: :west, position: {x, y}} = robot),
    do: %{robot | position: {x - 1, y}}

  defp update_robot("L", %{direction: :west} = robot),
    do: %{robot | direction: :south}

  defp update_robot("R", %{direction: :west} = robot),
    do: %{robot | direction: :north}

  defp update_robot("A", %{direction: :east, position: {x, y}} = robot),
    do: %{robot | position: {x + 1, y}}

  defp update_robot("L", %{direction: :east} = robot),
    do: %{robot | direction: :north}

  defp update_robot("R", %{direction: :east} = robot),
    do: %{robot | direction: :south}

  defp valid_instructions?(instructions) do
    Enum.all?(instructions, &(&1 in @valid_instructions))
  end

  @doc """
  Return the robot's direction.

  Valid directions are: `:north`, `:east`, `:south`, `:west`
  """
  @spec direction(robot :: any) :: atom
  def direction(robot) do
    robot.direction
  end

  @doc """
  Return the robot's position.
  """
  @spec position(robot :: any) :: {integer, integer}
  def position(robot) do
    robot.position
  end
end
