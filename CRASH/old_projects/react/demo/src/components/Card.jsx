import React from 'react';
import Avatar from './Avatar';
import Detail from './Detail';

function Card(props) {
    return (
        <div className="card">
            <div className="imgBx">
                <Avatar img={props.img} />
            </div>
            <div className="details">
                <Detail text={props.text} job={props.job} />
             </div>
        </div>
    );
}

export default Card;