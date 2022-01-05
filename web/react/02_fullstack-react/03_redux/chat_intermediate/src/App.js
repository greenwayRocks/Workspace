import React from "react";
import uuid from "uuid";
import { createStore } from "redux";

function reducer(state, action) {
  if (action.type === "ADD_MESSAGE") {
    const newMessage = {
      text: action.text,
      id: uuid.v4(),
      timestamp: Date.now(),
    };
    return {
      messages: state.thread.messages.concat(newMessage),
    };
  } else if (action.type === "DELETE_MESSAGE") {
    return {
      messages: state.messages.filter((m) => m.id !== action.id),
    };
  } else {
    return state;
  }
}

const initialState = {
  activeThreadId: "1-fca2",
  threads: [
    {
      id: "1-fca2",
      title: "Buzz Aldrin",
      messages: [
        {
          text: "Twelve minutes to ignition.",
          timestamp: Date.now(),
          id: uuid.v4(),
        },
      ],
    },
    {
      id: "2-be91",
      title: "Michael Collins",
      messages: [],
    },
  ],
};

const store = createStore(reducer, initialState);

class App extends React.Component {
  componentDidMount() {
    store.subscribe(() => this.forceUpdate());
  }

  render() {
    // getting state
    const state = store.getState();
    // getting state's data -> threads && activeThreadId
    const activeThreadId = state.activeThreadId;
    const threads = state.threads;
    const activeThread = threads.find((t) => t.id === activeThreadId);
    // # DELETE ME
    console.log(activeThreadId, threads, activeThread);

    // const messages = store.getState().messages;

    return (
      <div className="ui segment">
        <Thread thread={activeThread} />
      </div>
    );
  }
}

class MessageInput extends React.Component {
  state = {
    value: "",
  };

  onChange = (e) => {
    this.setState({
      value: e.target.value,
    });
  };

  handleSubmit = () => {
    store.dispatch({
      type: "ADD_MESSAGE",
      text: this.state.value,
    });
    this.setState({
      value: "",
    });
  };

  render() {
    return (
      <div className="ui input">
        <input onChange={this.onChange} value={this.state.value} type="text" />
        <button
          onClick={this.handleSubmit}
          className="ui primary button"
          type="submit"
        >
          Submit
        </button>
      </div>
    );
  }
}

class Thread extends React.Component {
  handleClick = (id) => {
    store.dispatch({
      type: "DELETE_MESSAGE",
      id: id,
    });
  };

  render() {
    const messages = this.props.thread.messages.map((message, index) => (
      <div
        className="comment"
        key={index}
        onClick={() => this.handleClick(message.id)}
      >
        <div className="text">
          {message.text}
          <span className="metadata">@{message.timestamp}</span>
        </div>
      </div>
    ));
    return (
      <div className="ui center aligned basic segment">
        <div className="ui comments">{messages}</div>
        <MessageInput />
      </div>
    );
  }
}

export default App;
