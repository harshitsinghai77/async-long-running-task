const router = require("express").Router();
const Queue = require("bull");

const REDIS_URL = process.env.REDIS_URL || "redis://127.0.0.1:6379";
let workQueue = new Queue("work", REDIS_URL);

router.get("/", (req, res) => {
  res.sendSuccess({ message: "Hello World" });
});

router.get("/schedule", async (req, res) => {
  let job = await workQueue.add({ name: "pokemon" });
  res.json({ id: job.id });
});

router.get("/status/:id", async (req, res) => {
  let id = req.params.id;
  let job = await workQueue.getJob(iconst router = require("express").Router();
const Queue = require("bull");

const REDIS_URL = process.env.REDIS_URL || "redis://127.0.0.1:6379";
let workQueue = new Queue("work", REDIS_URL);

router.get("/", (req, res) => {
  res.sendSuccess({ message: "Hello World" });
});

router.get("/schedule", async (req, res) => {
  let job = await workQueue.add({ name: "pokemon" });
  res.json({ id: job.id });
});

router.get("/status/:id", async (req, res) => {
  let id = req.params.id;
  let job = await workQueue.getJob(id);

  if (job) {
    let state = await job.getState();
    let progress = job._progress;
    let reason = job.failedReason;
    res.json({ id, state, progress, reason });
  }
  res.status(404).end();
});

router.get("/terminate/:id", async (req, res) => {
  let id = req.params.id;

  try {
    let job = await workQueue.getJob(id);
    if (job) {
      await job.discard(); // ensure no more attempts made
      await job.moveToFailed(
        { message: "Job is cancelled by the user request" },
        true
      );
      return res.json({ message: `Job with job id ${id} terminated` });
    }
    res.json({ message: `No running job with job id ${id} found` });
  } catch (e) {
    console.log(e);
    res.json({ message: "Some error occured" });
  }
});

router.get("/pause", async (req, res) => {
  try {
    await workQueue.pause();
    res.json({ message: "Queue paused" });
  } catch (e) {
    console.log(e);
    res.json({ message: "Some error occured" });
  }
});

router.get("/resume", async (req, res) => {
  try {
    await workQueue.resume();
    res.json({ message: "Queue resumed" });
  } catch (e) {
    console.log(e);
    res.json({ message: "Some error occured" });
  }
});

// You can listen to global events to get notified when jobs are processed
workQueue.on("global:completed", (jobId, result) => {
  console.log(`Job ${jobId} completed! Result: ${result}`);
});

module.exports = router;
