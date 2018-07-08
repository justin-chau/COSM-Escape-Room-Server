import React from "react";
import Logo from "./components/Logo";
import Log from "./components/Log";
import Badge from "./components/Badge";

class App extends React.Component {
  render() {
    return (
      <div>
        <Logo />
        <Log />
        <Badge />
      </div>
    );
  }
};

export default App;