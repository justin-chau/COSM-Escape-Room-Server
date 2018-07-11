import React from "react";
import './Form.css'
import Request from "superagent";
import Anime from "react-anime";

class Form extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fieldValue : '',
            placeholder : 'NAME',
            buttonMargin : '-20px',
            submitted : false,
            playerID : this.props.playerNum - 1 
        }

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({
            fieldValue : event.target.value
        });
    }

    handleSubmit(event) {
        event.preventDefault();
        var url = `http://localhost:5000/api/players/update?player_id=${this.state.playerID}`;
        Request.put(url).set('Content-Type', 'application/x-www-form-urlencoded')
        .send({"name" : this.state.fieldValue})
        .then((response) => {
            console.log(response)
        });

        this.setState({
            fieldValue : '',
            placeholder : `SAVED ON BAND ${this.props.playerNum}`,
            submitted : true,
            buttonMargin : '-80px'
        });
    }

    ButtonAnime(props) {
        if(props.submitted) {
            return (
                <Anime easing="easeOutElastic"
                duration={3000}
                autoplay={true}
                margin-left='-80px'
                backgroundColor='#74b27d'> 
                    <button>
                        <div className="text">
                            SUBMIT
                        </div>
                    </button>
                </Anime>
            );
        } else {
            return (
                <button>
                    <div className="text">
                        SUBMIT
                    </div>
                </button>
            );
        }
    }

    render () {
        return(
            <div className='PlayerForm'>
                PLAYER {this.props.playerNum}
                <form onSubmit={this.handleSubmit}>
                    <input type="text" placeholder={this.state.placeholder} value={this.state.fieldValue} onChange={this.handleChange} disabled={this.state.submitted}/>
                    <div className="container">
                        <this.ButtonAnime submitted={this.state.submitted}/>
                    </div>
                    
                </form>
            </div>  
        );
    }
};

export default Form;