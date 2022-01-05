import React from "react";
import EditableTimer from "./EditableTimer";

class TimerList extends React.Component {
  render() {
    const timers = this.props.timers.map((timer) => (
      <EditableTimer
        key={timer.id}
        id={timer.id}
        title={timer.title}
        project={timer.project}
        timeElapsed={timer.timeElapsed}
        runningSince={timer.runningSince}
        onUpdate={this.props.onUpdate}
      />
    ));

    return <div>{timers}</div>;
  }
}

export default TimerList;
