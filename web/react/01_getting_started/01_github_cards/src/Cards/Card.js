import React from 'react';

class Card extends React.Component {

  render() {
    return (
      <div className="github-profile" style={{display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '1rem', background: '#f4f4f4'}}>
            <img src={this.props.avatar_url} style={{width: '120px'}} alt="nth"/>
            <div className="info" style={{marginLeft: '2rem', fontWeight: 'bold', fontSize: '1.5rem'}}>
                <p className="name" style={{color: Math.random() < 0.5 ? 'red' : 'green'}}> {this.props.login} </p>
                <p className="name"> {this.props.bio} </p>
            </div>
      </div>
    );
  }
}

export default Card;
