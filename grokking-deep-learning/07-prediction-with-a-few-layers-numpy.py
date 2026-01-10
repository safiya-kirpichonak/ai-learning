import numpy


def neural_network(input):
    HIDDEN_LAYER_WEIGHTS = numpy.array([[0.1, 0.2, -0.1], [-0.1, 0.1, 0.9], [0.1, 0.4, 0.1]])
    PREDICTION_WEIGHTS = numpy.array([[0.3, 1.1, -0.3], [0.1, 0.2, 0.0], [0.0, 1.3, 0.1]])
    
    hidden_layer_results = input.dot(HIDDEN_LAYER_WEIGHTS)
    
    return input.dot(PREDICTION_WEIGHTS)


NUMBER_OF_TOES = numpy.array([8.5, 9.5, 9.9, 9.0])
WIN_PERCENTAGE = numpy.array([0.65, 0.8, 0.8, 0.9])
NUMBER_OF_FANS = numpy.array([1.2, 1.3, 0.5, 1.0])

for i in range(len(NUMBER_OF_TOES)):
    input = numpy.array([NUMBER_OF_TOES[i], WIN_PERCENTAGE[i], NUMBER_OF_FANS[i]])
    prediction = neural_network(input)
    print(prediction)