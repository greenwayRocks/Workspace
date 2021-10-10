import React from 'react';

function Avatar(props) {
    return (
    <div className="imgBx">
        <img src={props.img} alt="no source" />
    </div>
    );
}

export default Avatar;