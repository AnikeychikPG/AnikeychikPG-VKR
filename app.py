from flask import Flask, request, render_template
from model import predict, get_model
import numpy as np

app = Flask(__name__)


def get_prediction(data):
    prediction = predict(data)
    text = 'Соотношение матрица наполнитель:'
    matrix = ('Соотношение матрица наполнитель:', prediction[0][0])
    return matrix

@app.route('/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        p_1 = request.form.get('username')
        p_2 = request.form.get('username2')
        p_3 = request.form.get('username3')
        p_4 = request.form.get('username4')
        p_5 = request.form.get('username5')
        p_6 = request.form.get('username6')
        p_7 = request.form.get('username7')
        p_8 = request.form.get('username8')
        p_9 = request.form.get('username9')
        p_10 = request.form.get('username10')
        p_11 = request.form.get('username11')
        p_12 = request.form.get('username12')
        data_params = [p_1, p_2, p_3, p_4, p_5, p_6,
                       p_7, p_8, p_9, p_10, p_11, p_12]
        data = [float(i) for i in data_params]
        data = np.array([data])
        message = get_prediction(data)

    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run()