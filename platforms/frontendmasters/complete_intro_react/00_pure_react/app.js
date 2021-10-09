const Pet = (props) => {
    return React.createElement("div", {}, [
        React.createElement("h2", {}, props.name),
        React.createElement("h3", {}, props.animal),
        React.createElement("h3", {}, props.breed),
    ])
}

const App = () => {
    return React.createElement(
      "div",
      {},
      [
          React.createElement("h1", { id: "my-brand" }, "Adopt Me!"),
        //   ...[1, 2, 3, 4].map((i => React.createElement("h3", {}, i))),
          React.createElement(Pet, {name: "Luna", animal: "dog", "breed": "Havanese"} ),
          React.createElement(Pet, {name: "Machete", animal: "bird", "breed": "Crown"}),
          React.createElement(Pet, {name: "Aixa", animal: "Cat", "breed": "Siames"}),
      ]
    );
  }

ReactDOM.render(React.createElement(App), document.getElementById("root"));
// ReactDOM.render(App(), document.getElementById("root"));