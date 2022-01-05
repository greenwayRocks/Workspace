import React from "react";
import TimerForm from "./TimerForm";
import Timer from "./Timer";

class EditableTimer extends React.Component {
  render() {
    if (this.props.isOpen) {
      return (
        <TimerForm title={this.props.title} project={this.props.project} />
      );
    } else {
      return (
        <div>
          <Timer
            id={this.props.id}
            title={this.props.title}
            project={this.props.project}
            timeElapsed={this.props.timeElapsed}
            runningSince={this.props.runningSince}
            onUpdate={this.props.onUpdate}
          />
        </div>
      );
    }
  }
}

export default EditableTimer;
