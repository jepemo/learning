import React from 'react'
import ReactDOM from 'react-dom'
import Pet from './Pet'

const App = () => {
  return React.createElement("div", {}, [
    React.createElement("h1", { id: "my-brand" }, "Adopt Me!"),
    React.createElement(Pet, {
      name: "Luna",
      animal: "dog",
      breed: "Havanese",
    }),
    React.createElement(Pet, {
      name: "Machete",
      animal: "bird",
      breed: "Crown",
    }),
    React.createElement(Pet, { name: "Aixa", animal: "Cat", breed: "Siames" }),
  ]);
};

ReactDOM.render(React.createElement(App), document.getElementById("root"));
