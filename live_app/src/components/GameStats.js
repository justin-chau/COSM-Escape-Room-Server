import React from "react";
import "./GameStats.css"
import Request from "superagent";

class GameStats extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            puzzle1Finished : false,
            puzzle2Finished : false,
            puzzle3Finished : false,
            puzzle4Finished : false
        }

        setInterval(() => {
            var url = `http://localhost:5000/api/puzzles?puzzle_id=1`
            Request.get(url)
            .then((response) => {
                console.log(response)
                this.setState({
                    puzzle1Finished : response.body[0].is_finished
                });
            });
            var url = `http://localhost:5000/api/puzzles?puzzle_id=2`
            Request.get(url)
            .then((response) => {
                console.log(response)
                this.setState({
                    puzzle2Finished : response.body[0].is_finished
                });
            });
            var url = `http://localhost:5000/api/puzzles?puzzle_id=3`
            Request.get(url)
            .then((response) => {
                console.log(response)
                this.setState({
                    puzzle3Finished : response.body[0].is_finished
                });
            });
            var url = `http://localhost:5000/api/puzzles?puzzle_id=4`
            Request.get(url)
            .then((response) => {
                console.log(response)
                this.setState({
                    puzzle4Finished : response.body[0].is_finished
                });
            });
        }, 1000);   
    }

    render () {
        return (
            <div className='GameStats'>
                <div className='GameStatsText'>
                        { this.state.puzzle4Finished ? 'COMPLETE' : 
                        this.state.puzzle3Finished ? 'PUZZLE 4' :
                        this.state.puzzle2Finished ? 'PUZZLE 3' :
                        this.state.puzzle1Finished ? 'PUZZLE 2' : 'PUZZLE 1' }
                </div>
            </div>
        );
    }
};

export default GameStats;