import React, { Component } from 'react';
import Form from './components/Form';
import './App.css';
import Logo from './assets/Asset 1Meta.png'

class App extends Component {
  render() {
    return (
      <div className="App">
        <img src={Logo} alt="Metalliance" className="logo"/>
        <div className="Forms">
          <Form playerNum = '1'/>
          <Form playerNum = '2'/>
          <Form playerNum = '3'/>
        </div>
      </div>
    );
  }
}

export default App;
