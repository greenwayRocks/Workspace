import React from "react";
import { v4 as uuid } from "uuid";

import TimerList from "./TimerList";
import ToggleableTimerForm from "./ToggleableTimerForm";

class TimersDashboard extends React.Component {
  state = {
    timers: [
      {
        title: "Finish what you started!",
        project: "Timers App",
        id: uuid(),
        runningSince: Date.now(),
        timeElapsed: 504099,
      },
      {
        title: "Learn Shell Programming",
        project: "Robust Scripting",
        id: uuid(),
        runningSince: null,
        timeElapsed: 291023,
      },
      {
        title: "Learn CSS/JS?",
        project: "Web fundamentals",
        id: uuid(),
        runningSince: null,
        timeElapsed: 3820289,
      },
    ],
  };

  onUpdate = () => {
    this.updateTimer();
  };

  updateTimer = () => {
    console.log("hello, do this logic!");
    // open up timerform with title and project passed as props to it
    // no?
  };

  render() {
    return (
      <div className="layout">
        <TimerList timers={this.state.timers} onUpdate={this.onUpdate} />
        <ToggleableTimerForm />
      </div>
    );
  }
}

export default TimersDashboard;
