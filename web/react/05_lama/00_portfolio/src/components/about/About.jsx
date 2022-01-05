import React from "react";

import "./about.css";
import Aimg from "../../img/bird.png";

const About = () => {
  return (
    <div className="about">
      <div className="a-left">
        <div className="a-card a-bg"></div>
        <div className="a-card">
          <img src={Aimg} alt="about-image" className="a-img" />
        </div>
      </div>
      <div className="a-right"></div>
    </div>
  );
};

export default About;
