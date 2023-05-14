from flask import Flask, render_template
import random,json
import pandas as pd

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def login():

    with open('hackupc2023_restbai__dataset_sample.json', encoding="utf8") as json_file:
        data = json.load(json_file)

    dataset = [data[i] for i in data]
    df = pd.DataFrame(dataset)

    urls = []
    for i in df['images']: 
        urls.append(i[0])

    summary = []
    for j in df['summary']: 
        summary.append(j)

    selected_urls = random.sample(urls,10)
    
    with app.app_context(): 
        return render_template('index.html', urls=selected_urls)






