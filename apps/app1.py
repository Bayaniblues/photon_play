import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from app import app
import json
import plotly.graph_objects as go

from strawberryfields.apps import data, plot, sample, clique
import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

import numpy as np
import networkx as nx
import plotly
import pandas as pd
import re
import requests


data_in = ['51YZAJhOwIC5Gg3jMbAmhZ',
           '1BrgjqSg9du0lj3TUMLluL',
           '58ge6dfP91o9oXMzq3XkIS',
           '06T10fEzN8ZCcqzQZYA184',
           '0uybt73QFXaLCoxuVf6fhm',
           '2ldAdghnrO34HPcZ0IWfTu',
           '4rsW3WCZBGwhHfJWuHRwyT',
           '7E390nZTMqEbrNC1TmHd42',
           '0CwYG1UnRmOx8Q1EzElCIL',
           '17rf2oZYDVymJeYI9ftDXc']


# run with get_songs('strawberry_4d.json')
def get_songs(input_val):
    with open(input_val, 'r') as openfile:
        # Reading from json file
        blos = json.load(openfile)
    # nodes
    u = blos[0]
    # edges
    e = blos[1]
    # first generation
    gen1 = blos[2]
    # second generation
    gen2 = blos[3]
    client_id = "ac249f8bfc274671a2b90cd8fcc4c4ca"
    secret_id = "fe6dae5f957f4a47bc6657113af3e236"
    credentials = SpotifyClientCredentials(client_id=client_id,
                                           client_secret=secret_id)
    sp = spotipy.Spotify(client_credentials_manager=credentials)

    test1 = sp.tracks(u)

    return test1


def get_music_features(values):
    data = pd.read_csv('spotify3.csv')
    search = data[data.eq(values).any(1)].values.tolist()
    return search


def curry_music(music_in):
    """
    Enter List of values
    :param music_in:
    :return:
    """
    a = music_in
    state = []
    for i, x in enumerate(a):
        c = get_music_features(a[i])
        state.append(c)
    return state


def compare_this2(track_id):
    """
    Enter a list of Track_id's
    :param track_id:
    :return:
    """
    fig = go.Figure()
    data = curry_music(track_id)

    for i,x in enumerate(data):
      features = data[i][0][:10]
      id = data[i][0][-1]
      artist = data[i][0][-2]


      items_feature = ['acousticness',
                  'danceability',
                  'duration_ms',
                  'energy',
                  'instrumentalness',
                  'liveness',
                  'loudness',
                  'speechiness',
                  'valence',
                  'tempo']

      fig.add_trace(go.Scatterpolar(
          theta=items_feature,
          r=features,
          fill='toself',
          name=f'{id} : {artist}'
      ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )),
        showlegend=False
    )

    return dcc.Graph(figure=fig)


def visualization_pipe(file_in):
    with open(file_in, 'r') as openfile:
        # Reading from json file
        blos = json.load(openfile)
        # declare nodes, and edges
    u = blos[0]
    e = blos[1]
    # Extract generation data to plot our secondary graph
    gen1 = blos[2]
    gen2 = blos[3]

    def visualize(u, e, g):
        G = nx.Graph()
        G.add_nodes_from(u)
        G.add_edges_from(e)

        dens = nx.density(G)
        maximal_clique = u[:25]

        aplot = plot.graph(G,
                           maximal_clique,
                           subgraph_node_colour='#1DB954',
                           subgraph_edge_colour='#1DB954',
                           graph_node_colour='#ffffff',
                           graph_edge_colour='#ffffff',
                           background_color='#191414',
                           graph_node_size=0)

        bplot = plot.subgraph(G.subgraph(maximal_clique))

        return dcc.Graph(figure=bplot)

    return visualize(u, e, gen1)


def card_component():
    output = dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardImg(src="https://i.scdn.co/image/ab67616d0000b273692d9189b2bd75525893f0c1")
#
                #            style={"position":"relative",
                #                   "height": "200px",
                #                   "width": "200px"}),

                #html.Div(compare_this('6KbQ3uYMLKb5jDxLF7wYDD'),
               #          style={"position": "absolute"})
            ],
                         outline=True,
                         color="light"), width=3),

        dbc.Col(
        dbc.Card([
            dbc.CardBody([
                html.H3('Artist Name'),
                html.H4('Song Name')], style={"min-height": "200px"}

            )],
        ), width=9)])
    return output


def iterate_cards(list_in):
    state = []
    for i, x in enumerate(list_in):

        state.append(card_component())

    return state


layout = html.Div([
        dbc.Card([
            dbc.CardBody([
                html.H1('Genre')]),
            ],
            className="mb-3",
        ),
        dbc.Card([
            dbc.CardBody([
                html.H3('Polar Comparison'),
                html.P("Feature similarity of the top 25 songs"),
                html.Div(compare_this2(data_in))]),
            ],
            className="mb-3",
        ),
        dbc.Card(
            dbc.CardBody([html.H3("Stargraph"),
                          html.P("All music is connected, hover over constellation to explore"),
                          html.Center(visualization_pipe('strawberry_4d.json')), ]),
                 body=True,
                 className="mb-3"),
        card_component()
    #dcc.Link('Go to App 2', href='/apps/app2')
])


@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
