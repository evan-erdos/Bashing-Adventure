
import yaml

class Player:

    @staticmethod
    def load(filename):
        with open(filename, 'r') as f:
            doc = yaml.load(f)
        return Player(doc)


    def __init__(self, data):
        self.data = data

    def save(self, filename):
        with open(filename, 'w') as f:
            yaml.dump(self.data, f)

    def move(self, room): # room must be a string (for now)
        # need to check if room exists
        data[room] = room
        return True

        #Todo: disallow moving to rooms that are not connected
