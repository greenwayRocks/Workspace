import React from "react";

class Timer extends React.Component {
  render() {
    return (
      <div className="card">
        <h3>{this.props.title}</h3>
        <h5>{this.props.project}</h5>
        <h4>{this.props.timeElapsed}</h4>
        <div className="flexy">
          <button className="btn">Start</button>
          <button onClick={this.props.onUpdate} className="btn">
            Edit
          </button>
          <button className="btn">Delete</button>
        </div>
      </div>
    );
  }
}

export default Timer;
