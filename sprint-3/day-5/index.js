let state = "";
let bgText = document.getElementById("bgtext");
let flashArea = document.getElementById("flashRed");
const canvas = document.getElementById("canvas");
let startButton = document.getElementById("startButton");

const loadingOverlay = document.createElement("div");
loadingOverlay.id = "loading-overlay";

const spinner = document.createElement("div");
spinner.className = "spinner";

const paragraph = document.createElement("p");
paragraph.textContent = "Loading...";

loadingOverlay.appendChild(spinner);
loadingOverlay.appendChild(paragraph);


const URL = "https://teachablemachine.withgoogle.com/models/QOamYEcZQ/";
let model, webcam, ctx, labelContainer, maxPredictions;


async function init() {
  const modelURL = URL + "model.json";
  const metadataURL = URL + "metadata.json";
  document.body.appendChild(loadingOverlay);

  model = await tmPose.load(modelURL, metadataURL);
  maxPredictions = model.getTotalClasses();

  if (model != undefined) {
    startButton.style.display = "none";
    loadingOverlay.style.display='none'
  }

  // Convenience function to setup a webcam
  const size = 300;
  const flip = true; // whether to flip the webcam
  webcam = new tmPose.Webcam(size, size, flip); // width, height, flip
  await webcam.setup(); // request access to the webcam
  await webcam.play();
  window.requestAnimationFrame(loop);

  // append/get elements to the DOM
  canvas.width = size;
  canvas.height = size;
  ctx = canvas.getContext("2d");
  labelContainer = document.getElementById("label-container");
  for (let i = 0; i < maxPredictions; i++) {
    // and class labels
    labelContainer.appendChild(document.createElement("div"));
  }
}

async function loop(timestamp) {
  webcam.update(); // update the webcam frame
  await predict();
  window.requestAnimationFrame(loop);
}

async function predict() {
  // Prediction #1: run input through posenet
  // estimatePose can take in an image, video or canvas html element
  const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
  // Prediction 2: run input through teachable machine classification model
  const prediction = await model.predict(posenetOutput);

  for (let i = 0; i < maxPredictions; i++) {
    const classPrediction =
      prediction[i].className + ": " + prediction[i].probability.toFixed(2);
    labelContainer.childNodes[i].innerHTML = classPrediction;
    if (prediction[i].probability.toFixed(2) > 0.5) {
      if (prediction[i].className == "Normal") {
        state = "Looking Straight";
        flashArea.setAttribute("class", "");
      } else {
        state = prediction[i].className;
        flashArea.setAttribute("class", "flash-red");
      }
    }
    bgText.innerText = state;
  }
  drawPose(pose);
}

function drawPose(pose) {
  if (webcam.canvas) {
    ctx.drawImage(webcam.canvas, 0, 0);
    // draw the keypoints and skeleton
    if (pose) {
      const minPartConfidence = 0.5;
      tmPose.drawKeypoints(pose.keypoints, minPartConfidence, ctx);
      tmPose.drawSkeleton(pose.keypoints, minPartConfidence, ctx);
    }
  }
}
