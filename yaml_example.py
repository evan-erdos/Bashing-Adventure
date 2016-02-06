
import yaml

with open('rooms.yml', 'r') as f:
    doc = yaml.load(f)

txt = doc["room_0"]["desc"]
print(txt)
"branch1 text"

