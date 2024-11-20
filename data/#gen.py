"""
Combines all items, blocks, and entites fies into one file for each type.type
"""

import json
import os
import glob

PATH = os.path.dirname(os.path.realpath(__file__))


def merge(dir: str, name: str):
    obj = {
        "$schema": f"https://raw.githubusercontent.com/legopitstop/Assets_Plus/v1.3.0/data/schemas/{name}.json",
        "$id": f"https://raw.githubusercontent.com/legopitstop/Assets_Plus/v1.3.0/data/{name}.json",
        "format_version": None,
    }
    obj["minecraft:" + name] = {}
    for fp in glob.glob(PATH + f"/{dir}/**", recursive=True):
        print(fp)
        if os.path.isfile(fp):
            with open(fp, "r") as r:
                dat = json.load(r)
                # set format_version
                if obj["format_version"] is None:
                    obj["format_version"] = dat["format_version"]

                id = dat["minecraft:" + name]["description"]["identifier"]
                obj["minecraft:" + name][id] = dat["minecraft:" + name]

    with open(os.path.join(PATH, name + ".json"), "w") as w:
        w.write(json.dumps(obj))


if __name__ == "__main__":
    merge("blocks", "block")
    merge("entities", "entity")
    merge("items", "item")

    print("Calculating contents...")

    contents = []
    for path in glob.glob(PATH + "/**", recursive=True):
        if os.path.isfile(path) and str(path).endswith(".json"):
            contents.append({"path": path.replace(PATH + "\\", "").replace("\\", "/")})

    with open(os.path.join(PATH, "contents.json"), "w") as wc:
        wc.write(json.dumps({"content": contents}))

    print("Done!")
