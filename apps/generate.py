import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from visualize import HandleState, Fruit, Component


def manage_state(file_in, name):
    # get blossom state
    # init classes
    state = HandleState()
    fruit = Fruit()
    comp = Component()

    # load blossom list
    state.blossom = fruit.set_blossom(file_in)
    blos = state.blossom

    nodes = blos[0]
    edges = blos[1]

    fruit.set_features()

    # load spotify api
    state.spotify = fruit.set_metadata(lambda: nodes[:25])

    data = state.spotify

    print(len(data['tracks']))
    deck = []
    songs = []
    for i, x in enumerate(data['tracks']):
        Ximage = data['tracks'][i]["album"]["images"][0]['url']

        Xsong_name = data['tracks'][i]["name"]
        songs.append(Xsong_name)

        Xsong_url = data['tracks'][i]['external_urls']['spotify']

        Xartist_url = data['tracks'][i]['album']['artists'][0]['external_urls']['spotify']
        Xartist_name = data['tracks'][i]['album']['artists'][0]['name']

        a = dbc.Card([
                dbc.CardBody([
                    html.A(dbc.Button(html.Img(style={"height": "100px", "width": "100px"}, src=Ximage), color="link"), href=Xsong_url),
                    html.A(dbc.Button(html.H5(Xsong_name), color="link"), href=Xsong_url),
                    html.A(dbc.Button(html.P(Xartist_name), color="link"), href=Xartist_url)
                ])
            ])
        deck.append(a)
    layout = html.Div([
        dbc.Card([
            dbc.CardBody([
                html.H3(name)]),
            html.Div(
                deck
            )
        ],
            className="mb-3",
        ),
    ]
    )
    return layout


