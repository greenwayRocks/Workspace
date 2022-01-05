import React from 'react';
import Card from './Card';
import cardInfo from '../details';

function createCard(myCard) {
  return (
    <Card 
      key={myCard.id} 
      img={myCard.imgURL} 
      job={myCard.job} 
      text={myCard.text}     
    />
    );
}

function App() {
  return (
    <div>
      <h1 className="heading">Check out my cards!</h1>
      {cardInfo.map(createCard)}
    </div>
  );
}

export default App;
