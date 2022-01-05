import React from "react";

// createStore() function ---
function createStore(reducer, initial_state) {
  let state = initial_state;
  const listeners = [];

  const subscribe = (listener) => listeners.push(listener);

  const getState = () => state;

  const dispatch = (action) => {
    state = reducer(state, action);
    listeners.forEach((l) => l());
  };

  return {
    subscribe,
    getState,
    dispatch,
  };
}

// Reducer function ---
function reducer(state, action) {
  if (action.type === "ADD_MESSAGE") {
    return {
      messages: state.messages.concat(action.message),
    };
  } else if (action.type === "DELETE_MESSAGE") {
    return {
      messages: [
        ...state.messages.slice(0, action.index),
        ...state.messages.slice(action.index + 1, state.messages.length),
      ],
    };
  } else {
    return state;
  }
}

// Initializing state and store ---
const initialState = { messages: [] };

const store = createStore(reducer, initialState);

// React Components ---

class App extends React.Component {
  componentDidMount() {
    store.subscribe(() => this.forceUpdate());
  }
  render() {
    const messages = store.getState().messages;
    return (
      <div className="ui segment">
        <MessageView messages={messages} />
        <MessageInput />
      </div>
    );
  }
}

class MessageInput extends React.Component {
  state = {
    value: "",
  };

  onChange = (evt) => this.setState({ value: evt.target.value });

  handleSubmit = () => {
    store.dispatch({ type: "ADD_MESSAGE", message: this.state.value });
    this.setState({ value: "" });
  };

  render() {
    return (
      <div className="ui input">
        <input onChange={this.onChange} value={this.state.value} type="text" />
        <button className="ui primary button" onClick={this.handleSubmit}>
          Send
        </button>
      </div>
    );
  }
}

class MessageView extends React.Component {
  handleClick = (index) => {
    store.dispatch({ type: "DELETE_MESSAGE", index: index });
  };

  render() {
    const messages = this.props.messages.map((msg, i) => (
      <div className="comment" key={i} onClick={() => this.handleClick(i)}>
        {msg}
      </div>
    ));

    return <div className="ui comments">{messages}</div>;
  }
}

export default App;
