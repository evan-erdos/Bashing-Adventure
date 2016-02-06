import yaml

def load(filename):
    with open(filename, 'r') as f:
        doc = yaml.load(f)
    return Player(doc)

class Player():
    def __init__(self,d):
        self.d = d

    def __getattr__(self,name):
        if (name in self.d.keys()):
            return self.d[name]
        else:
            raise AttributeError

    def __setattr__(self,name,value):
        self.d[name]=value


    def save(self,filename):
        with open(filename,'w') as f:
            yaml.dump(self.d,f)
