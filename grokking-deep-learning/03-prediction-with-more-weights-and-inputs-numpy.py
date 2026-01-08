import numpy

def neural_network(input):
    WEIGHTS = numpy.array([0.1, 0.2, 0])
    return input.dot(WEIGHTS)

number_of_toes  = numpy.array([8.5, 9.5, 9.9, 9.0])
win_percentage = numpy.array([0.65, 0.8, 0.8, 0.9])
number_of_fans = numpy.array([1.2, 1.3, 0.5, 1.0])

for i in range(4):
    input = numpy.array([number_of_toes[i], win_percentage[i], number_of_fans[i]])
    prediction = neural_network(input)
    print(prediction)