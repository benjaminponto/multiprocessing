from flask import Flask, render_template, request
from multiprocessing import matrix_multiplication

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
        return render_template('index.html', X=X, y=y, result=result, time_taken=time_taken)
    else:
         return render_template('index.html', X=None, y=None, result=None, time_taken=None)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)