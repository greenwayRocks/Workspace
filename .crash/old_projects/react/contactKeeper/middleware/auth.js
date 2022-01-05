const jwt = require("jsonwebtoken");
const config = require("config");

module.exports = function(req, res, next) {
  let token = req.header("x-auth-token");

  if (!token) {
    res.status(401).json({ msg: "Token not found.. Authorization denied!" });
  }

  try {
    const decoded = jwt.verify(token, config.get("jwtSecret"));
    req.user = decoded.user;
    next();
  } catch (err) {
    res.status(401).json({ msg: "Token is not valid!" });
  }
};
