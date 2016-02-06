
import yaml

with open('tree.yml', 'r') as f:
    doc = yaml.load(f)

txt = doc["treeroot"]["branch1"]
print(txt)
"branch1 text"

