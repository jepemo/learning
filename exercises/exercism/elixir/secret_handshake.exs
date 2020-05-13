defmodule SecretHandshake do
  use Bitwise
  @doc """
  Determine the actions of a secret handshake based on the binary
  representation of the given `code`.

  If the following bits are set, include the corresponding action in your list
  of commands, in order from lowest to highest.

  1 = wink
  10 = double blink
  100 = close your eyes
  1000 = jump

  10000 = Reverse the order of the operations in the secret handshake
  """
  @spec commands(code :: integer) :: list(String.t())
  def commands(code) do
    reverse = (code &&& 16) > 0

    res = []
    res = if (code &&& 1) > 0, do: ["wink" | res], else: res
    res = if (code &&& 2) > 0, do: ["double blink" | res], else: res
    res = if (code &&& 4) > 0, do: ["close your eyes" | res], else: res
    res = if (code &&& 8) > 0, do: ["jump" | res], else: res

    if reverse, do: res, else: Enum.reverse(res)
  end
end
