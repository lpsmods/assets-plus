"""Generate the .mcdefinitions file"""
import glob
import commentjson

version = 'unset'
lines = set()
RP = "resource_packs/assets_plus"

with open(f"{RP}/manifest.json") as fd:
    data = commentjson.load(fd)
    version = data['header']['version']


# Textures
for fp in glob.glob(f"{RP}/textures/**/*.png", recursive=True):
    print(fp)
    lines.add(f"texture={fp}")

# Models
for fp in glob.glob(f"{RP}/models/**/*.json", recursive=True):
    print(fp)
    with open(fp) as fd:
        data = commentjson.load(fd)
    if 'minecraft:geometry' in data:
        for geo in data['minecraft:geometry']:
            id = geo['description']['identifier']
            lines.add(f"model={id}")


# Materials
for fp in glob.glob(f"{RP}/materials/**/*.material", recursive=True):
    print(fp)
    with open(fp) as fd:
        data = commentjson.load(fd)
        if 'materials' in data:
            for k in data['materials'].keys():
                if k == 'version':
                    continue
                id = k.split(":")[0]
                lines.add(f"material={id}")

# Block Textures
# with open(f"{RP}/textures/terrain_texture.json") as fd:
#     data = commentjson.load(fd)
#     if 'texture_data' in data:
#         for id in data['texture_data'].keys():
#             lines.add(f"block_texture={id}")
            
# Item Texture
# with open(f"{RP}/textures/item_texture.json") as fd:
#     data = commentjson.load(fd)
#     if 'texture_data' in data:
#         for id in data['texture_data'].keys():
#             lines.add(f"item_texture={id}")

with open(".mcdefinitions", 'w') as fd:
    fd.write(f"## Assets+ v{version}\n{"\n".join(sorted(lines))}\n")
