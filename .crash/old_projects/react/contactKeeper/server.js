const express = require("express");
const connectDB = require("./config/db");

const app = express();

// Connect MongoDB
connectDB();

// Allow body parsing
app.use(express.json({ extended: false }));

app.get("/", (req, res) => res.json({ obj: "myObject" }));

// Define routes
app.use("/api/users", require("./routes/users"));
app.use("/api/auth", require("./routes/auth"));
// app.use("/api/contacts", require("./routes/contacts"));

app.get("/", (req, res) => res.json({ msg: "Hello there!" }));

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
