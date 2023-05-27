# Stock Prediction Program with Python for AMZN

This is a Python program that predicts the stock prices of AMZN (Amazon.com Inc.) using Linear Regression model. The program uses historical data of AMZN from a CSV file and trains a Linear Regression model to predict the future prices. 

## Installation

1. Install [Python](https://www.python.org/downloads/)
2. Install required packages using pip by running the following command:

```
pip install pandas numpy scikit-learn
```

3. Clone the repository

```
git clone https://github.com/CireWire/musical-broccoli.git
```

## Usage

1. Navigate to the cloned repository directory.

```
cd <repository>
```

2. Run the program using the following command.

```
python predict.py
```

3. The program will output the confidence of the model and the predicted prices of the next 'n' days.

## Docker

This program is also available as a Docker container. To build and run the Docker container, follow these steps:

1. Navigate to the cloned repository directory.

```
cd <repository>
```

2. Build the Docker image.

```
docker build -t <image-name> .
```

3. Run the Docker container.

```
docker run <image-name>
```

4. The program will output the confidence of the model and the predicted prices of the next 'n' days.

## Contributing

Contributions to this project are always welcome. To contribute, please follow these steps:

1. Fork the project.
2. Create a new branch.
3. Implement your changes.
4. Test your changes.
5. Submit a pull request.

## Credits

This program is developed by [Your Name] and is based on the tutorials by [tutorial author]. 

## License

This program is released under the [MIT License](https://opensource.org/licenses/MIT).
