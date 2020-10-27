import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from app import app

layout = html.Div([
        dbc.Card(
            dbc.CardBody(html.H3('App 1'),),
            className="mb-3",
        ),
        dbc.Card("This is also within a body", body=True),
    #dcc.Link('Go to App 2', href='/apps/app2')
])


@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
