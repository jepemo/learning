defmodule BankAccount do
  @moduledoc """
  A bank account that supports access from multiple processes.
  """

  @typedoc """
  An account handle.
  """
  @opaque account :: pid

  @doc """
  Open the bank. Makes the account available.
  """
  @spec open_bank() :: account
  def open_bank() do
    {:ok, account_pid} = Agent.start_link(fn -> 0 end)
    account_pid
  end

  @doc """
  Close the bank. Makes the account unavailable.
  """
  @spec close_bank(account) :: none
  def close_bank(account) do
    if Process.alive?(account) do
      Agent.stop(account)
    else
      {:error, :account_closed}
    end
  end

  @doc """
  Get the account's balance.
  """
  @spec balance(account) :: integer
  def balance(account) do
    if Process.alive?(account) do
      Agent.get(account, &(&1))
    else
      {:error, :account_closed}
    end
  end

  @doc """
  Update the account's balance by adding the given amount which may be negative.
  """
  @spec update(account, integer) :: any
  def update(account, amount) do
    if Process.alive?(account) do
      Agent.update(account, fn (state) -> state + amount end)
    else
      {:error, :account_closed}
    end
  end
end
