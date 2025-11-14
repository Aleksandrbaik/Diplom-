import requests

if __name__ == '__main__':

    r = requests.post('http://localhost:5000/predict', json=['foreclosure', 'condo','3', 1780, '46250', False, '1989',  3.7, 1.71])
    print(r.json()['prediction'])
