import dash_core_components as dcc
import dash_html_components as html
from app import app
from apps import generate
# Rock
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc



app.layout = html.Div([
    dcc.Store(id='memory', storage_type='session'),

    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])


nav = html.Div([
    dbc.Card([
        html.H3("Search by Genre")
    ]),
    dbc.Card([
        html.A(dbc.Button(html.H4("Pop"), color="link"), href='/pop'),
    ]),
    dbc.Card([
        html.A(dbc.Button(html.H4("Rock"), color="link"), href='/rock'),
    ]),
    dbc.Card([
        html.A(dbc.Button(html.H4("Jazz"), color="link"), href='/jazz'),
    ]),
    dbc.Card([
        html.A(dbc.Button(html.H4("Country"), color="link"), href='/country'),
    ]),
    dbc.Card([
        html.A(dbc.Button(html.H4("Metal"), color="link"), href='/metal'),
    ]),
    dbc.Card([
        html.A(dbc.Button(html.H4("Strawberryfields"), color="link"), href='/strawberryfields'),
    ]),
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return nav
    if pathname == '/strawberryfields':
        return generate.manage_state("data/strawberry_4d.json", "Strawberryfields")
    if pathname == '/rock':
        return generate.manage_state("data/Rock.json", "Rock")
    if pathname == '/jazz':
        return generate.manage_state("data/jazz.json", "Jazz")
    if pathname == '/country':
        return generate.manage_state("data/Country.json", "Country")
    if pathname == '/metal':
        return generate.manage_state("data/Metal.json", "Metal")
    if pathname == '/pop':
        return generate.manage_state("data/Pop.json", "Pop")
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
