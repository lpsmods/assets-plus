"""
Generate texture and model reports
"""
import os, json

LOCAL = os.path.dirname(os.path.realpath(__file__))

report = {
    "minecraft:model": {},
    "minecraft:terrain_texture": {},
    "minecraft:item_texture": {},
}


def uniqueItem(list, value):
    """Returns true if that item is already added in the list"""
    for i in list:
        if i == value:
            return True
    return False


def convertList(list):
    return (
        str(list)
        .replace("[", "")
        .replace("]", "")
        .replace("'", "`")
        .replace(",", "<br>")
    )


def addReport(type, path, key, value):
    cat = report[type]
    if path in cat:
        if key in cat[path]:
            if uniqueItem(cat[path][key], value) == False:
                cat[path][key].append(value)
        else:
            cat[path][key] = []
            addReport(type, path, key, value)

    else:
        cat[path] = {}
        addReport(type, path, key, value)


# terrain_texture
opn = open(os.path.join(LOCAL, "textures", "terrain_texture.json"), "r")
terrain_texture = json.load(opn)
opn.close()

texture_data = terrain_texture["texture_data"]
for texture in texture_data:
    path = texture_data[texture]["textures"]
    if type(path) == str:
        addReport("minecraft:terrain_texture", path, "atlas", texture)
    elif type(path) == dict:
        addReport("minecraft:terrain_texture", path["path"], "atlas", texture)

# item_texture
opn = open(os.path.join(LOCAL, "textures", "item_texture.json"), "r")
item_texture = json.load(opn)
opn.close()

texture_data = item_texture["texture_data"]
for texture in texture_data:
    path = texture_data[texture]["textures"]
    if type(path) == str:
        addReport("minecraft:item_texture", path, "atlas", texture)
    elif type(path) == dict:
        addReport("minecraft:item_texture", path["path"], "atlas", texture)

# model
model_path = os.path.join(LOCAL, "models", "blocks")

for filename in os.listdir(model_path):
    model_file = os.path.join(model_path, filename)
    if filename.endswith(".json") and os.path.isfile(model_file):

        opn = open(model_file, "r")
        model = json.load(opn)
        opn.close()

        path = "models/blocks/" + filename.replace(".json", "")

        for submodel in model["minecraft:geometry"]:
            material_instances = []

            addReport(
                "minecraft:model", submodel["description"]["identifier"], "path", path
            )

            # for each material_instance
            for bone in submodel["bones"]:
                if "name" in bone:
                    addReport(
                        "minecraft:model",
                        submodel["description"]["identifier"],
                        "bones",
                        bone["name"],
                    )

                if "cubes" in bone:
                    for cube in bone["cubes"]:
                        if isinstance(cube["uv"], dict):
                            for k, uv in cube["uv"].items():
                                if "material_instance" in uv:
                                    mi = uv["material_instance"]
                                    addReport(
                                        "minecraft:model",
                                        submodel["description"]["identifier"],
                                        "material_instance",
                                        mi,
                                    )
                                else:
                                    addReport(
                                        "minecraft:model",
                                        submodel["description"]["identifier"],
                                        "material_instance",
                                        k,
                                    )


# create report
wrt = open(os.path.join(LOCAL, "report.json"), "w")
wrt.write(json.dumps(report, indent=4))
wrt.close()

wrt = open(os.path.join(LOCAL, "data_table.md"), "w")

# Block Textures
block_textures_table = "| Name(s) | Path |\n|--|--|\n"
for path in report["minecraft:terrain_texture"]:
    names = convertList(report["minecraft:terrain_texture"][path]["atlas"])
    block_textures_table = block_textures_table + "| %s | `%s` |" % (names, path) + "\n"

with open(os.path.join(LOCAL, "docs", "__Block Textures.md"), "r") as temp:
    template = temp.read()

with open(os.path.join(LOCAL, "docs", "Block Textures.md"), "w") as w:
    w.write(template.replace("{Block Textures}", block_textures_table))

# Item Textures
item_textures_table = "| Name(s) | Path |\n|--|--|\n"
for path in report["minecraft:item_texture"]:
    names = convertList(report["minecraft:item_texture"][path]["atlas"])
    item_textures_table = item_textures_table + "| %s | `%s` |" % (names, path) + "\n"

with open(os.path.join(LOCAL, "docs", "__Item Textures.md"), "r") as temp:
    template = temp.read()

with open(os.path.join(LOCAL, "docs", "Item Textures.md"), "w") as w:
    w.write(template.replace("{Item Textures}", item_textures_table))

# Models
models_table = "| Name | Material Instances | Bones | Path |\n|--|--|--|--|\n"
for name in report["minecraft:model"]:
    path = convertList(report["minecraft:model"][name]["path"])

    if "bones" in report["minecraft:model"][name]:
        bones = convertList(report["minecraft:model"][name]["bones"])
    else:
        bones = ""

    if "material_instance" in report["minecraft:model"][name]:
        mi = convertList(report["minecraft:model"][name]["material_instance"])
    else:
        mi = ""
    models_table = (
        models_table + "| `%s` | %s | %s | %s |" % (name, mi, bones, path) + "\n"
    )

with open(os.path.join(LOCAL, "docs", "__Models.md"), "r") as temp:
    template = temp.read()

with open(os.path.join(LOCAL, "docs", "Models.md"), "w") as w:
    w.write(template.replace("{Models}", models_table))
