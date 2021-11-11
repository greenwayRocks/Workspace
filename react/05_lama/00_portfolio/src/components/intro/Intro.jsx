import React from "react";

import Me from "../../img/nice.png";
import "./intro.css";

const Intro = () => {
  return (
    <div className="intro">
      <div className="i-left">
        <div className="l-wrap">
          <h2 className="i-intro">Hello, My Name is</h2>
          <h1 className="i-name">Satish Adhikari</h1>
          <div className="i-title">
            <div className="i-title-wrapper">
              <div className="i-title-item">Web Developer</div>
              <div className="i-title-item">UI/UX Designer</div>
              <div className="i-title-item">Shell Programmer</div>
              <div className="i-title-item">Content Creator</div>
              <div className="i-title-item">Linux Engineer</div>
            </div>
          </div>
          <div className="i-desc">
            I do this and this. More than that, I even do this. Do I really? I
            don't know. Maybe I'm bluffing, but I gotta do sth, right? What the
            hell am I even doing right now?
          </div>
        </div>
      </div>
      <div className="i-right">
        <div className="i-bg">abc</div>
        <img src={Me} alt="Thats me" className="i-img" />
      </div>
    </div>
  );
};

export default Intro;
