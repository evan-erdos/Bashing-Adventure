import yaml

def load(filename):
    with open(filename, 'r') as f:
        doc = yaml.load(f)
    return Player(doc)

class Player:
    def __init__(self,args):
        self.args = args

    def save(self,filename):
        with open(filename,'w') as f:
            yaml.dump(self.args,f)
