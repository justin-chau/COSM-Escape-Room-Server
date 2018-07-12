import React, { Component } from 'react';
import './App.css';
import PlayerStats from './components/PlayerStats';
import GameStats from './components/GameStats';
import Logo from './assets/Asset 1Meta.png';

class App extends Component {
  render() {
    return (
      <div className="App">
        <img src={Logo} alt="Logo" className="logo"/>
        <iframe
          src="http://player.twitch.tv/?channel=justinchau&muted=false&allowfullscreen=false"
          autoPlay="true"
          frameborder="0"
          scrolling="no"
          allowfullscreen="false">
        </iframe>
        <PlayerStats playerNum = '1'/>
        <PlayerStats playerNum = '2'/>
        <PlayerStats playerNum = '3'/>
        <GameStats />
      </div>
    );
  }
}

export default App;
