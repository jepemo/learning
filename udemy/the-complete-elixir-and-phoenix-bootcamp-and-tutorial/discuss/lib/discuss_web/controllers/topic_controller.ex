defmodule DiscussWeb.TopicController do
  use DiscussWeb, :controller

  alias Discuss.Topic

  def new(conn, _params) do
    changeset = Topic.changeset(%Topic{}, %{})

    # IO.inspect changeset
    render(conn, "new.html", changeset: changeset)
  end

  def create(conn, %{"topic" => topic} = params) do
    IO.inspect params

    %{"title" => title} = topic
    IO.puts title
  end
end
