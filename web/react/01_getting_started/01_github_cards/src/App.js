import React from 'react';

import Cardlist from './Cards/Cardlist';
import Form from './Form/Form';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      profiles: []
    };
  }

  handleProfiles = (newProfile) => {
    this.setState(prevState => ({
      profiles: [...prevState.profiles, newProfile]
    }));
  };

  render() {
      return (
        <div className="App">
          <header className="App-header">Github Finder</header>
          <Form addProfiles={this.handleProfiles} />
          <Cardlist profiles={this.state.profiles}/>
        </div>
      );
    }
}

export default App;
