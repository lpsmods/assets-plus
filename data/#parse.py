"""
Removes comments in all JSON files
"""

import commentjson
import json
import glob
import os
import multiprocessing

PATH = os.path.dirname(os.path.realpath(__file__))


def parse(dir: str):
    for fp in glob.glob(PATH + f"/{dir}/**", recursive=True):
        print(fp)
        if os.path.isfile(fp):
            try:
                with open(fp, "r") as r:
                    dat = commentjson.load(r)
            except Exception as e:
                print(e)
                return 0

            with open(fp, "w") as w:
                w.write(json.dumps(dat, indent=2))


if __name__ == "__main__":
    values = [
        "biomes",
        "blocks",
        "cameras",
        "entities",
        "feature_rules",
        "features",
        "items",
        "loot_tables",
        "recipes",
        "spawn_rules",
        "trading",
    ]

    with multiprocessing.Pool() as pool:
        results = pool.map(parse, values)
    print("Done!")
