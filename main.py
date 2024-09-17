from flask import Flask, render_template
from multiprocessing import matrix_multiplication

app = Flask(__name__)


#home represents default home page with the route
@app.route('/')
def index():
    X, y, result, time_taken = matrix_multiplication()
    return render_template('index.html', X=X, y=y, result=result, time_taken=time_taken)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)