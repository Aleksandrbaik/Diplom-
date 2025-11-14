from flask import Flask, request
import pandas as pd
import pickle

# загружаем модель из файла
with open('diplom_pipeline.pkl', 'rb') as pkl_file:
    loaded_pipe = pickle.load(pkl_file)
# создаём приложение
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def get_predict():
    data = request.json
    cols = ['status', 'propertyType', 'baths', 'zipcode', 'target', 'Pool', 'Year built', 'r_sch_mean', 'dist_sch_min', 'target_log']
    req_f = pd.DataFrame([data], columns=cols)
    print(req_f)
    print(loaded_pipe.predict(req_f))
    pred = loaded_pipe.predict(req_f)
    return {'prediction': pred[0]}

if __name__ == '__main__':
    app.run('localhost', 5000)