import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import flask

server = flask.Flask(__name__)
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True,
                server=server)
