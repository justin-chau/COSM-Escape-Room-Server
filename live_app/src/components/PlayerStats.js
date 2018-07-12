import React from "react";
import "./PlayerStats.css"
import Request from "superagent";

class PlayerStats extends React.Component {

    
    constructor(props) {
        super(props);
        this.state = {
            playerId : this.props.playerNum - 1,
            playerName : `Player ${this.props.playerNum}`,
            oxygen : 100,
            health : 100,
            isSpy: false,
            spyKey : false,
            chestKey : false
        }

        setInterval(() => {
            var url = `http://localhost:5000/api/players?player_id=${this.state.playerId}`
            Request.get(url)
            .then((response) => {
                console.log(response)
                this.setState({
                    playerName: response.body[0].name,
                    isSpy: response.body[0].is_spy,
                    oxygen: response.body[0].oxygen,
                    health : response.body[0].health,
                    spyKey : response.body[0].spy_key,
                    chestKey : response.body[0].chest_key
                });
            });
        }, 1000);   
    }
        
        // this.handleChange = this.handleChange.bind(this);
        // this.handleSubmit = this.handleSubmit.bind(this);
    

    render () {
        return (
            <div className="StatContainer">
                <div className="PlayerName">
                    <div className="NameText"> { this.state.playerName } { this.state.isSpy ? '[SPY]' : ''} </div>
                </div>
                <div className="Stats">
                    <div className="StatText">
                        <div className="Value">
                            <strong>OXYGEN</strong> { this.state.oxygen }/100
                        </div>
                        <div className="Value">
                            <strong>HEALTH</strong> { this.state.health }/100
                        </div>
                        <div className="Value">
                            <strong>ITEMS</strong> { this.state.chestKey ? 'CHEST KEY' : ''} { this.state.spyKey ? 'SPY KEY' : ''} { this.state.chestKey ? '' : this.state.spyKey ? '' : 'NONE'}
                        </div>
                    </div>
                </div>
            </div>
        );
    }
};

export default PlayerStats;