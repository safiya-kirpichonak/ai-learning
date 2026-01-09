def elementwise_multiplication(vector_a, vector_b):
    assert type(vector_a) == list, "vector_a must be an array"
    assert type(vector_b) == list, "vector_b must be an array"
    assert len(vector_a) == len(vector_b), "vector_a, vector_b must be the same length"
    
    result = []
    for i in range(len(vector_a)):
        result.append(vector_a[i] * vector_b[i])
    
    return result


def elementwise_addition(vector_a, vector_b):
    assert type(vector_a) == list, "vector_a must be an array"
    assert type(vector_b) == list, "vector_b must be an array"
    assert len(vector_a) == len(vector_b), "vector_a, vector_b must be the same length"
    
    result = []
    for i in range(len(vector_a)):
        result.append(vector_a[i] + vector_b[i])
    
    return result


def vector_sum(vector):
    assert type(vector) == list, "vector must be an array"
    
    sum = 0
    for i in range(len(vector)):
        sum += vector[i]

    return sum


def vector_average(vector):
    assert type(vector) == list, "vector must be an array"
    
    sum = vector_sum(vector)

    return sum / len(vector)


def weight_sum(vector_a, vector_b):
    assert type(vector_a) == list, "vector_a must be an array"
    assert type(vector_b) == list, "vector_b must be an array"
    assert len(vector_a) == len(vector_b), "vector_a, vector_b must be the same length"

    result = 0
    for i in range(len(vector_a)):
        result += (vector_a[i] * vector_b[i])

    return result


def number_multiplication(number, vector):
    assert type(vector) == list, "vector must be an array"

    result = []
    for i in range(len(vector)):
        result.append(number * vector[i])
    
    return result


def vector_matrix_multiplication(vector, matrix):
    assert type(vector) == list, "vector must be an array"
    assert type(matrix) == list, "matrix must be an array"
    assert len(vector) == len(matrix), "vector, matrix must be the same length"

    result = []
    for i in range(len(vector)):
        result.append(weight_sum(vector, matrix[i]))

    return result

