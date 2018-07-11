import React from "react";
import Logo from "./components/Logo";
import Log from "./components/Log";
import Badge from "./components/Badge";
import Request from "superagent";

class App extends React.Component {
  state = {
    current_code: null,
    current_coordinates: null,
    code_verified: null,
    coordinates_verified : null
  }

  sendCode = (e) => {
    e.preventDefault();
    var code_input = e.target.elements.code_field.value;
    var url = "http://localhost:5000/api/puzzles/update?puzzle_id=1";
    Request.put(url).set('Content-Type', 'application/x-www-form-urlencoded')
    .send({ "current_code" : code_input })
    .then((response) => {
      const current_code = response.body[0].current_code;
      const code_verified = response.body[0].is_correct;
      console.log(current_code);
      this.setState({
        current_code : current_code
      });
      console.log(this.state);
    });
    Request.put(url).set('Content-Type', 'application/x-www-form-urlencoded')
    .send({ "current_code" : code_input })
    .then((response) => {
      const current_code = response.body[0].current_code;
      const code_verified = response.body[0].is_correct;
      console.log(current_code);
      this.setState({
        current_code : current_code,
        code_verified : code_verified
      });
      console.log(this.state);
    });
  }

  sendCoordinates = (e) => {
    e.preventDefault();
    var coord_input = e.target.elements.coordinate_field.value;
    var url = "http://localhost:5000/api/puzzles/update?puzzle_id=2";
    Request.put(url).set('Content-Type', 'application/x-www-form-urlencoded')
    .send({ "current_coordinates" : coord_input })
    .then((response) => {
      const current_coordinates = response.body[0].current_coordinates;
      const coordinates_verified = response.body[0].is_correct;
      console.log(current_coordinates);
      this.setState({
        current_coordinates : current_coordinates
      });
      console.log(this.state);
    });
    Request.put(url).set('Content-Type', 'application/x-www-form-urlencoded')
    .send({ "current_coordinates" : coord_input })
    .then((response) => {
      const current_coordinates = response.body[0].current_coordinates;
      const coordinates_verified = response.body[0].is_correct;
      console.log(current_coordinates);
      this.setState({
        current_coordinates : current_coordinates,
        coordinates_verified : coordinates_verified
      });
      console.log(this.state);
    });
  }

  render() {
    return (
      <div>
        <Logo />
        <Log sendCode = { this.sendCode }
        code_verified = { this.state.code_verified}
        sendCoordinates = { this.sendCoordinates }
        coordinates_verified = { this.state.coordinates_verified }
        current_code = { this.state.current_code }
        current_coordinates = { this.state.current_coordinates }/>
        <Badge />
      </div>
    );
  }
};

export default App;