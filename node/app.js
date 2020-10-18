const express = require("express");
const morgan = require("morgan");
const cors = require("cors");

const app = express();
const JobRoutes = require("./routes/jobs");
const serverResponseHandler = require("./middleware/serverResponseHandler");

require("dotenv").config();

//middlewares
app.use(morgan("dev"));
app.use(cors());

// Custome middleware
app.use(serverResponseHandler());

// Routes
app.use("/job", JobRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Listening to port ${PORT}`);
});
