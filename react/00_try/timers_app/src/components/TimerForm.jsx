import React from "react";

class TimerForm extends React.Component {
  state = {
    title: this.props.title || "",
    project: this.props.project || "",
  };

  handleTitleChange = (event) => {
    this.setState({ title: event.target.value });
  };

  handleProjectChange = (event) => {
    this.setState({ project: event.target.value });
  };

  render() {
    const submitText = this.props.title ? "Update" : "Create";
    return (
      <div className="card">
        <input
          type="text"
          placeholder="Title"
          value={this.state.title}
          onChange={this.handleTitleChange}
        />
        <input
          type="text"
          placeholder="Project"
          value={this.state.project}
          onChange={this.handleProjectChange}
        />
        <div className="flexy">
          <button className="btn">{submitText}</button>
          <button className="btn" onClick={this.props.onClose}>
            Close
          </button>
        </div>
      </div>
    );
  }
}

export default TimerForm;
