
import React from 'react';
import axios from 'axios';

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: ''
    };
  }

  submitFunc = async (e) => {
    e.preventDefault();
    const resp = await axios.get(`https://api.github.com/users/${this.state.username}`)
    this.props.addProfiles(resp.data);
    this.setState({username: ''});
  }

  render() {
    return (
      <form action="#" onSubmit={this.submitFunc}>
        <input type="text"
          value={this.state.username}
           onChange={event => this.setState({username: event.target.value})}
            placeholder="Github username" />
        <button>Submit</button>
      </form>
    );
  }
}

export default Form;
