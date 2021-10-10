import React from 'react';

function Detail(props) {
    return (
    <div className="details">
        <h2>{props.text}<br /><span>{props.job}</span></h2>
    </div>
    );
}

export default Detail;