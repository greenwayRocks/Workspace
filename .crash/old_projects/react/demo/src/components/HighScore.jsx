import React, {Component} from 'react';

class HighScore extends Component {

    render(){

        if(this.props.myBool) {
            return (
                <h3>You beat my HIGH SCORE!
                <button className="my-button" onClick={this.props.onReset}>Reset</button>
                </h3>
            );
        } else {
            return null;
        }
    }
}

export default HighScore;