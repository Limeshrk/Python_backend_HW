import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


from flask import Flask
from flask import send_file
app = Flask(__name__)

# prevent matplotlib from opening a gui
plt.ioff()
mpl.use('Agg')


@app.route('/')
def hello_world():
    #data_source = np.random.randint(1, 6, 40).reshape(10, 4)
    # your code goes here....
    with open('income.txt', 'r') as file:
        lines = file.readlines()
    #oszlopnevek kiolvasása
    columns = lines[0].strip().split(',')
    columns = [item.strip() for item in columns]
    
    #adatok beolvasása és formázása
    data_source = []
    for line in lines[1:]: #első sor kimarad, az a fejléc
        data = line.strip().split(',') #elem elválasztása a vesszőnél -nél, újsor levágása
        data = [int(item.replace(' ', '')) for item in data] #int-é alakítés és szóközök kivétele
        data_source.append(data) #listához adja a listákat
    df = pd.DataFrame(data_source, columns=columns) #kiolvasott oszlopnevek használata
    #df.columns = ['Class A', 'Class B', 'Class C', 'Class D']
    sns_plot = sns.barplot(palette="ch:.25", data=df, ci=None)
    sns_plot.figure.savefig("output.png")
    plt.close()
    return send_file('output.png', mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)