console.log('>> run~!!');

// Define a model for linear regression.
const model = tf.sequential();
console.log('>> after model create');

model.add(tf.layers.dense({units: 1, inputShape: [1]}));
console.log('>> after add layer');

model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});
console.log('>> after compile');

// Generate some synthetic data for training.
// tf.tensor ( values , shape? , dtype? )
// https://js.tensorflow.org/api/latest/
const xs = tf.tensor2d( ____________, _________);
const ys = tf.tensor2d( ____________, _________);

// Train the model using the data.
model.fit(xs, ys, {
  epochs: 100,
  callbacks: {
    onEpochEnd: (epoch, log) => console.log(`Epoch ${epoch}: loss = ${log.loss}`)
    }
  }).then(() => {
  // Use the model to do inference on a data point the model hasn't seen before:
  console.log('>> after fit');
  
  model.predict(tf.tensor2d( __________, _________).print();
  console.log('>> after predict');
  // Open the browser devtools to see the output
});
