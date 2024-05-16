// Define function to handle image upload and prediction
async function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    const predictionText = document.getElementById('prediction');

    if (!fileInput.files || fileInput.files.length === 0) {
        predictionText.textContent = 'No file selected';
        return;
    }

    const file = fileInput.files[0];
    const img = document.createElement('img');
    const reader = new FileReader();

    reader.onload = async function(e) {
        img.src = e.target.result;
        predictionText.textContent = 'Predicting...';

        // Load the TensorFlow.js model
        const model = await tf.loadLayersModel('tfjs_model/model.json');

        // Preprocess the image and make a prediction
        const tensor = preprocessImage(img);
        const prediction = model.predict(tensor);
        const predictionValue = prediction.dataSync()[0];
        predictionText.textContent = `Prediction: ${predictionValue.toFixed(2)}`;
    };

    reader.readAsDataURL(file);
}

// Define function to preprocess the image
function preprocessImage(img) {
    return tf.tidy(() => {
        // Convert the image to a tensor
        const tensor = tf.browser.fromPixels(img)
            .resizeNearestNeighbor([150, 150])
            .toFloat();

        // Normalize the pixel values to the range [0, 1]
        return tensor.div(255.0)
            // Expand dimensions to add a batch dimension
            .expandDims();
    });
}


document.getElementById('imageForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission behavior
    uploadImage(); // Call the function to handle image upload and prediction
});

