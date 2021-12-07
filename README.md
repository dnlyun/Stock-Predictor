# Stock-Predictor

## About
A program that can predict future stock price movement using Long short-term memory (LSTM) model.

## Data
Data is downloaded from Yahoo Finance and the ticker 'SPY' was used for training.
<img width="1280" alt="Screen Shot 2021-09-13 at 4 37 08 PM" src="https://user-images.githubusercontent.com/43867196/133154932-dc5e2d92-5347-4559-85f7-d2daeae1dd51.png">

## Averaging
Before LSTM model is trained, the data is tested through two algorithms: the standard average and the exponential moving average.

### Standard Averaging
<img width="1280" alt="Screen Shot 2021-09-13 at 4 38 34 PM" src="https://user-images.githubusercontent.com/43867196/133154961-d8602e9b-6dc3-44ff-ad94-f16e25e73671.png">

### Exponential Moving Averaging
<img width="1280" alt="Screen Shot 2021-09-13 at 4 38 43 PM" src="https://user-images.githubusercontent.com/43867196/133154972-83153c0c-0e81-4149-90e4-de004e848a5a.png">

### Conclusion
While exponential follows the line very closely, its accuracy drastically becomes worse the further in time you calculate the price. That is where the LSTM model comes in.

## Long Short-Term Memory
LSTM model is a time series model used to forecast data based on historical data.

The RNN API provided by TensorFlow is used to implement the LSTM model.

![Screen Shot 2021-09-13 at 5 37 53 PM](https://user-images.githubusercontent.com/43867196/133160076-ae833f14-3434-4dc4-92f3-f8ba4102281c.png)

## What I've Learned
* Math and logic behind recurrent neural networks and LSTM models.
* Generating data and optimizing model for higher accuracy.

## Software and Libraries
* Python 3.6
* TensorFlow 1.6
* Scikit-learn
* Pandas
* Matplotlib
* Numpy
