import json


print(
"""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------

"""
)
with open("./sample-data.json") as file:
    data = json.load(file)

    for item in data["imdata"]:
        l1 = item["l1PhysIf"]
        print(f"{l1["attributes"]["dn"]}\t\t{l1["attributes"]["descr"]} \t\t {l1["attributes"]["speed"]} {l1["attributes"]["mtu"]}")

