# Assets Plus

This is a resource pack library that makes all the vanilla Minecraft block ids use better IDs. To use just add the `minecraft` namespace before the texture for example `minecraft:lime_concrete` to use the lime concrete texture. This resource pack also adds a few new textures like Java Edition's debug textures

## Note

> This resource pack library does not contain the vanilla minecraft assets. It will use vanilla minecraft, or the highest tier resource pack, textures.

## Downloads

You can download any version via [legopitstop.weebly.com](https://legopitstop.weebly.com/assets-plus.html)

- [1.20.12 - v1.5.0 (Latest)](https://github.com/legopitstop/Assets_Plus/releases/tag/v1.5.0)
- [1.19.80 - v1.4.0](https://github.com/legopitstop/Assets_Plus/releases/tag/v1.4.0)
- [1.19 - v1.3.0](https://github.com/legopitstop/Assets_Plus/releases/tag/v1.3.0)
- [1.19 - v1.2.0](https://www.mediafire.com/file/xhk2r1zioi9ref2/Assets_Plus_RP_v1.2.0.mcpack/file)
- [1.18 - v1.1.0](https://www.mediafire.com/file/te3v8k4ri0msk71/Assets_Plus_RP_v1.1.0.mcpack/file)
- [1.17.3 - v1.0.0](https://www.mediafire.com/file/13j38byhg522sow/Assets_Plus_RP_v1.0.0.mcpack/file)

## How to add to your pack

In your Behavior packs dependencies append the following code:

```json
{
    "uuid": "c86dd7d9-e84e-456f-a84f-1993e353da4c",
    "version": [1, 7, 0]
}
```

## FAQ

### Why a separate resource pack?

My last few add-ons use vanilla Minecraft assets, but the default texture id isn't the best, for example, It is impossible to use the White Concrete texture because it is inside an array of textures and thus not able to use the texture in a data-driven block. So making this a separate pack means less copy-pasting of the same block textures.

### How do I get this to work with my behavior pack?

You can find information on how to add this library to yours via the [Documentation Page](https://docs.lpsmods.dev/assetsplus/)

### What IDs are supported?

You can find a list of all texture IDs via the [Documentation Page](https://docs.lpsmods.dev/assetsplus/)

### What do I do if I found an issue with the library?

You can submit all issues and suggestions via [GitHub](https://github.com/lpsmods/Assets_Plus/issues)

### Where are the texture files inside the resource pack?

The resource pack reads Minecraft's built-in textures so there is no need to add all the vanilla textures, however, this does add both debug textures from Java Edition.
