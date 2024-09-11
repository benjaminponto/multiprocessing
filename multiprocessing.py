import time
import random

#start of the program 
start = time.time()

# 3x3 matrix
X = [[random.randint(0,9),random.randint(0,9),random.randint(0,9)],
    [random.randint(0,9) ,random.randint(0,9),random.randint(0,9)],
    [random.randint(0,9) ,random.randint(0,9),random.randint(0,9)]]

# 3x3 matrix
y = [[random.randint(0,9),random.randint(0,9),random.randint(0,9)],
    [random.randint(0,9) ,random.randint(0,9),random.randint(0,9)],
    [random.randint(0,9) ,random.randint(0,9),random.randint(0,9)]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


#anything more or less than a million iternations is kinda a waste of time.
for l in range(1,1000000):
    #interate through the rows of first matrix, x
    for i in range(len(X)):
        #interate through the columns of second matrix, y
        for j in range(len(y[0])):
            #interate through the rows of second matrix, y
            for k in range(len(y)):
                result[i][j] += X[i][k] * y[k][j]
            
for r in result:
   print(r)




#end of the program
end = time.time()


#output the amount of time the program ran
print("Time taken in seconds: ", end-start)