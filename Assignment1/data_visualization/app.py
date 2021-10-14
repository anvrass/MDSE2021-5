from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/data_visualization/housing', methods=['POST'])
def print_graph():
    db_api = os.environ['DB_API']
    # Make a GET request to training db service to retrieve the training data/features.
    r = requests.get(db_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    df = df[['Taxes', 'SoldPrice', 'Prop_Type_num']]
    fig = px.bar(df, x=”Taxes”, y=”SoldPrice”, color=”Prop_Type_num”, barmode=”group”)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template(‘notdash.html’, graphJSON=graphJSON)


app.run(host='0.0.0.0', port=5000)
