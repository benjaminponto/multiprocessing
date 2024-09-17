import time
import random


#THIOS IS THE START OF A NEW BRANCH

def matrix_multiplication(interations):
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
    for l in range(1,interations):
        #interate through the rows of first matrix, x
        for i in range(len(X)):
            #interate through the columns of second matrix, y
            for j in range(len(y[0])):
                #interate through the rows of second matrix, y
                for k in range(len(y)):
                    result[i][j] += X[i][k] * y[k][j]

    time_taken = time.time() - start

    return X, y, result, time_taken
        

    #output the amount of time the program ran 
    print("Time taken in seconds: ", end-start)


   

    