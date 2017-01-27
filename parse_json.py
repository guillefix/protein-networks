import json
from pprint import pprint

with open('domain_net.cyjs') as data_file:
    data = json.load(data_file)

style = {"a": "rgb(0,0,255)", "b": "rgb(255,0,0)", "c": "rgb(0,255,0)", "d": "rgb(255,255,0)", "e": "rgb(0,153,153)", "f": "rgb(0,153,153)", "g": "rgb(1,1,1)", "h": "rgb(0,153,153)", "i": "rgb(10,10,10)"}

new_data = data["elements"]

nodes = new_data["nodes"]
edges = new_data["edges"]

new_data["nodes"] = [{"id": node["data"]["id"], "label": node["data"]["name"],"x": node["position"]["x"], "y": node["position"]["y"], "size": 0.1, "color": style[node["data"]["Column_2"]]} for node in nodes]
new_data["edges"] = [{"id": edge["data"]["id"], "source": edge["data"]["source"], "target": edge["data"]["target"]} for edge in edges]


f = open('domain_net.json', 'w')
f.write(json.dumps(new_data))
