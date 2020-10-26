const router = require("express").Router();
const Queue = require("bull");
const {response} = require('../utils/util')

const REDIS_URL = process.env.REDIS_URL || "redis://127.0.0.1:6379";
const workQueue = new Queue("work", REDIS_URL);

router.get("/schedule", async (req, res) => {
  try {
    const job = await workQueue.add({ name: "pokemon", status: "Processing" });
    res.sendSuccess(response(true, `Job Successfully created`, { id: job.id }))
  } catch (e) {
    res.sendInternalServerError()
  }
});

router.get("/status/:id", async (req, res) => {
  try {
    const id = req.params.id;
    const job = await workQueue.getJob(id);
  
    if (job) {
      let state = await job.getState();
      let progress = job._progress;
      let reason = job.failedReason;
      return res.sendSuccess({ id, state, progress, reason })
    }
    res.sendSuccess(response(false, `Job with job id ${id} not found. Please check the id and try again.`, null))

  } catch (e) {
    res.sendInternalServerError()
  }
});

router.get("/pause/:id", async (req, res) => {
  try {
    const id = req.params.id;
    const job = await workQueue.getJob(id);
    await job.update({
      ...job.data,
      status: "Paused"
    })
    return res.sendSuccess(response(true, `Job with task id ${id} PAUSED`, null))
  } catch (e) {
    res.sendInternalServerError()
  }
});

router.get("/resume/:id", async (req, res) => {
  try {
    const id = req.params.id;
    const job = await workQueue.getJob(id);
    await job.update({
      ...job.data,
      status: "Processing"
    })
    return res.sendSuccess(response(true, `Job with task id ${id} Resumed`, null))
  } catch (e) {
    res.sendInternalServerError()
  }
});

router.get("/terminate/:id", async (req, res) => {
  try {
    const id = req.params.id;
    const job = await workQueue.getJob(id);

    if (job) {
      await job.discard(); // ensure no more attempts made
      await job.moveToFailed(
        { message: "Job is cancelled by the user request" },
        true
      );
      return res.sendSuccess(response(true, `Job with job id ${id} terminated`, { id }))
    }
    res.sendSuccess(response(false, `Job with job id ${id} not found. Please check the id and try again.`, null))

  } catch (e) {
    res.sendInternalServerError()
  }
});

router.get("/pause-queue", async (req, res) => {
  try {
    await workQueue.pause();
    res.sendSuccess(response(true, "Queue paused", null))
  } catch (e) {
    res.sendInternalServerError()
  }
});

router.get("/resume-queue", async (req, res) => {
  try {
    await workQueue.resume();
    res.sendSuccess(response(true, "Queue resumed", null))
  } catch (e) {
    res.sendInternalServerError()
  }
});


// You can listen to global events to get notified when jobs are processed
workQueue.on("global:completed", (jobId, result) => {
  console.log(`Job ${jobId} completed! Result: ${result}`);
});

module.exports = router;
