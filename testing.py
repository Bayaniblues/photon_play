import unittest
from visualize import HandleState, Fruit


class test_methods(unittest.TestCase):
    def test_json(self):
        #print('testing1, checking state')
        state = HandleState()
        state.json_in = "new.json"
        x = state.json_in

        self.assertIsNot(x, 'strawberry_4d.json')

    def test_blossom(self):
        #print('testing2, checking blossom')

        state = HandleState()
        fruit = Fruit()

        # set state
        state.blossom = fruit.set_blossom('data/strawberry_4d.json')

        x = state.blossom
        #print("length is " + str(len(x)))
        nodes = x[0]
        edges = x[1]
        c = x[2]
        #print(a)
        #print(b)
        print(c)


        self.assertGreater(len(x), 2)

    def test_features(self):
        #print("testing3")
        state = HandleState()
        fruit = Fruit()

        state.features = fruit.set_features(search_in='1BrgjqSg9du0lj3TUMLluL')
        x = state.features
        #print(f'features are {x}')
        self.assertIsNot('1BrgjqSg9du0lj3TUMLluL', '51YZAJhOwIC5Gg3jMbAmhZ')

    def test_metadata(self):
        state = HandleState()
        fruit = Fruit()
        state.spotify = fruit.set_metadata()

        data = state.spotify
        #tracks = data['tracks'][0]["album"]["images"][0]['url']

        image = data['tracks'][0]["album"]["images"][0]['url']

        song_name = data['tracks'][0]["name"]
        song_url = data['tracks'][0]['external_urls']['spotify']

        artist_url = data['tracks'][0]['album']['artists'][0]['external_urls']['spotify']
        artist_name = data['tracks'][0]['album']['artists'][0]['name']

        # print(image)
        # print(song_name)
        # print(artist_url)
        # print(artist_name)
        # print(song_url)

        self.assertGreater(len(data), 0)

        #print(image)
        #print(name)
        #print(artist)


if __name__ == "__main__":

    unittest.main()