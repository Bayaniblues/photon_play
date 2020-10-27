from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

import pandas as pd
import json
import os
import plotly.graph_objects as go
import dash_core_components as dcc

from os.path import join, dirname
from dotenv import load_dotenv

# Global states to load env
load_dotenv(verbose=True)
client_id = os.getenv("CLIENT_ID")
secret_id = os.getenv("SECRET_ID")
credentials = SpotifyClientCredentials(client_id=client_id,
                                               client_secret=secret_id)
sp = spotipy.Spotify(client_credentials_manager=credentials)


class HandleState(object):
    def __init__(self):
        # Preloaded states
        self.csv_in = 'spotify3.csv'
        self.json_in = 'strawberry_4d.json'
        # additional states
        self.blossom = []
        self.features = []
        self.spotify = []
        self.nodes = []
        self.edges = []

    # json state
    @property
    def state(self):
        print(self.json_in)
        return self.json_in

    @state.setter
    def state(self, value):
        print("changing state", value)
        self.json_in = value

    # blossom state
    @property
    def set_blossom(self):
        return self.blossom

    @set_blossom.setter
    def set_blossom(self, value):
        self.blossom = value

    # feature state
    @property
    def set_features(self):
        return self.features

    @set_features.setter
    def set_features(self, value):
        self.features = value

    # spotify_data
    @property
    def set_spotify(self):
        return self.spotify

    @set_spotify.setter
    def set_spotify(self, value):
        self.spotify = value


# Get fruitful returns
class Fruit(object):
    @staticmethod
    def set_blossom(value='strawberry_4d.json'):
        with open(value, 'r') as openfile:
            # Reading from json file
            x = json.load(openfile)
        return x

    @staticmethod
    def set_features(csv_in='spotify3.csv', search_in='51YZAJhOwIC5Gg3jMbAmhZ'):
        data = pd.read_csv(os.path.realpath(csv_in))
        search = data[data.eq(search_in).any(1)].values.tolist()
        return search

    @staticmethod
    def set_metadata(list_values=lambda: ['51YZAJhOwIC5Gg3jMbAmhZ', '1BrgjqSg9du0lj3TUMLluL']):
        b = sp.tracks(list_values())
        return b


class Component(object):
    @staticmethod
    def polar(features, nodes, songs):
        fig = go.Figure()
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
            name=f'{songs[0]}'
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visable=True,
                    range=[0, 1]
                )
            ),
        )
        return dcc.Graph(figure=fig)


if __name__ == "__main__":
    print('hello')
