import {useState} from 'react';

function Button (props) {
  const {handleClick, increment} = props;
  const onClickFunction = () => handleClick(increment);

  return <button onClick={onClickFunction}>{increment}</button>;
}

function Display(props) {
  return <div>{props.message}</div>
}


function App () {
  const [counter, setCounter] = useState(0);
  const incCounter = (incValue) => setCounter(counter + incValue);

  return (
    <div ClassName="container">
      <Button handleClick={incCounter} increment={1}/>
      <Button handleClick={incCounter} increment={5}/>
      <Button handleClick={incCounter} increment={10}/>
      <Button handleClick={incCounter} increment={15}/>
      <Display message={counter}/>
    </div>
  );
}


export default App;
