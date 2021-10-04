import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from Model import createModel

app = dash.Dash(__name__)
server = app.server

N, run_avg_predictions, z = createModel()

x1, y1 = map(list, zip(*z))
arr = []
for i in range(len(y1)):
    temp = y1.pop(0)
    for num in temp:
        arr.append(num)

print(x1)
y1 = arr
print(y1)
print(len(y1))

app.layout = html.Div([
    html.H1("Stock Price Movement Predictor", style={"textAlign": "center"}),

    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Movement Prediction', children=[
            html.Div([
                dcc.Graph(
                    id="graph1",
                    figure={
                        "data": [
                            go.Scatter(
                                x=x1,
                                y=y1
                            )
                        ],
                        "layout": go.Layout(
                            title='scatter plot',
                            xaxis={'title': 'Date'},
                            yaxis={'title': 'Price'}
                        )
                    }
                )
            ])
        ]),
        dcc.Tab(label='One Step Price Average', children=[
            html.Div([
                dcc.Graph(
                    id="graph2",
                    figure={
                        "data": [
                            go.Scatter(
                                x=list(range(0, N)),
                                y=run_avg_predictions
                            )
                        ],
                        "layout": go.Layout(
                            title='scatter plot',
                            xaxis={'title': 'Date'},
                            yaxis={'title': 'Price'}
                        )
                    }
                )
            ])
        ])
    ]),
])


if __name__ == "__main__":
    # Use reloader stops code from running multiple times
    app.run_server(debug=True, use_reloader=False)
