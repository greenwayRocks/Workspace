const express = require("express");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const config = require("config");
const User = require("../models/User");
const { check, validationResult } = require("express-validator");

const router = express.Router();

// @route    POST /api/users
// @desc     Register a user
// @access   Public
router.post(
  "/",
  [
    check("name", "Please include a name!").not().isEmpty(),
    check("email", "Please include a valid email address!").isEmail(),
    check(
      "password",
      "Please include a password at least six chars long!"
    ).isLength({ min: 6 }),
  ],
  async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      res.status(400).json({ errors: errors.array() });
    }

    let { name, email, password } = req.body;

    try {
      let user = await User.findOne({ email });

      if (user) {
        res.send(400).json({ msg: "User already exists!" });
      }

      user = new User({
        name,
        email,
        password,
      });

      const salt = await bcrypt.genSalt(10);
      user.password = await bcrypt.hash(password, salt);

      await user.save();

      const payload = {
        user: {
          id: user.id,
        },
      };

      jwt.sign(
        payload,
        config.get("jwtSecret"),
        {
          expiresIn: 360000,
        },
        (err, token) => {
          if (err) throw err;
          res.json({ token });
        }
      );
    } catch (err) {
      console.error(err.message);
      res.status(500).send("Server ERROR...");
    }
  }
);

module.exports = router;
