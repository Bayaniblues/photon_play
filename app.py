import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc


app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True)
server = app.server