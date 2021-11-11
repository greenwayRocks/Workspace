import React from "react";
import TimerForm from "./TimerForm";

class ToggleableTimerForm extends React.Component {
  state = {
    isOpen: false,
  };

  onClick = (event) => {
    this.setState({ isOpen: true });
    console.log(event);
  };

  onClose = (event) => {
    this.setState({ isOpen: false });
    console.log(event);
  };

  render() {
    if (this.state.isOpen) {
      return (
        <div>
          <TimerForm onClose={this.onClose} />
        </div>
      );
    } else {
      return (
        <div>
          <button onClick={this.onClick} className="btn">
            +
          </button>
        </div>
      );
    }
  }
}

export default ToggleableTimerForm;
