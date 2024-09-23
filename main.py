from flask import Flask, render_template, request
from multi_processing import matrix_multiplication, matrix_multiplication_optimized

app = Flask(__name__)


#home represents default home page with the route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            iteration = int(request.form['iterations'])
        except:
            iteration = 1000 #this will be the default value for i if the user makes an invalid request

        X, y, result, time_taken = matrix_multiplication(iteration)

        X2, y2, result2, time_taken2 = matrix_multiplication_optimized(iteration)


        return render_template('index.html', X=X, y=y, result=result, time_taken=time_taken
                               , X2=X2, y2=y2, result2=result2, time_taken2=time_taken2)
    else:
         return render_template('index.html', X=None, y=None, result=None, time_taken=None
                                , X2=None, y2=None, result2=None, time_taken2=None)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)