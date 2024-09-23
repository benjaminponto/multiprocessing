import time
import random
import numpy as np 



def matrix_multiplication(interation):
    #start of the program 
    start = time.time()

    # 3x3 matrix that selects a random number between 0 and 9
    X = [[random.randint(0,9),random.randint(0,9),random.randint(0,9)],
        [random.randint(0,9) ,random.randint(0,9),random.randint(0,9)],
        [random.randint(0,9) ,random.randint(0,9),random.randint(0,9)]]

    # 3x3 matrix that selects a random number between 0 and 9
    y = [[random.randint(0,9),random.randint(0,9),random.randint(0,9)],
        [random.randint(0,9) ,random.randint(0,9),random.randint(0,9)],
        [random.randint(0,9) ,random.randint(0,9),random.randint(0,9)]]

    #here is where we will store the result of each calucaltion and the end.
    result = [[0,0,0],
            [0,0,0],
            [0,0,0]]


    #anything more or less than a million iternations is kinda a waste of time.
    for l in range(1,interation):
        #interate through the rows of first matrix, x
        for i in range(len(X)):
            #interate through the columns of second matrix, y
            for j in range(len(y[0])):
                #interate through the rows of second matrix, y
                for k in range(len(y)):
                    result[i][j] += X[i][k] * y[k][j]

    time_taken = time.time() - start

    return X, y, result, time_taken
        

  



def matrix_multiplication_optimized(interation):
    start = time.time()

    X = np.random.randint(0, 10, (3, 3))
    y = np.random.randint(0, 10, (3, 3))

    result = np.zeros((3, 3), dtype=int)

    for i in range(interation):
        result += np.dot(X,y)
        
    time_taken = time.time() - start

    return X, y, result, time_taken

        


