import React, { Fragment } from "react";
import { Link } from "react-router-dom";

const NotFound = () => {
  return (
    <Fragment>
      <h1>Page Not Found</h1>
      <h1>--------------------------</h1>
      <p className='lead'>The page you were looking for, was not found!</p>

      <Link to='/'>
        <button className='btn btn-dark'>Go to Home</button>
      </Link>
    </Fragment>
  );
};

export default NotFound;
