import React from 'react';
import HighScore from './HighScore';
import '../css/styles.css';
import App from './App';
import Form from './Form';

class Application extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            count: 0,
            isOverTen: false
        };
    }

    handleClick = () => {
        this.setState({
            count: this.state.count + 1
        });
    }

    componentDidUpdate(props, state) {
        if(this.state.count > 10 && this.state.count !== state.count && !this.state.isOverTen) {
            this.setState({
                isOverTen: true
            });
        }
    }

    handleReset = () => {
        this.setState({
            count: 0,
            isOverTen: false
        });
    }

    render(){

        let {count, isOverTen} = this.state;

        return (
            <div className="pContainer">
                <div className="my-container">
                    <h1>You clicked me <span>{count}</span> times!</h1>
                    <HighScore myBool={isOverTen} onReset={this.handleReset} />
                    <button className="my-button" onClick={this.handleClick}>Click ME</button>
                    <hr />
                    <App />
                </div>
                <div class="myForm">
                <Form />
                </div>
            </div>
        );
    }
}

export default Application;