# wad2obj

Convert [WAD levels](https://en.wikipedia.org/wiki/Doom_modding) from the [1993 id Software game, Doom](https://en.wikipedia.org/wiki/Doom_(1993_video_game), into [OBJ 3D models](https://en.wikipedia.org/wiki/Wavefront_.obj_file).

Level geometry and textures are converted for the most part, but no attempt is made to support lights, objects, monsters, moving platforms/doors, etc.

## Setup

- Install [uv](https://github.com/astral-sh/uv) for fast Python package management
- run `uvx --from http://github.com/jminor/wad2obj wad2obj -h`

If that produces a helpful message, then you're good to go.

Now run `make shareware` or `make freedoom` to download, unzip, and convert E1M1 from one of those WAD files.

## Manual Setup

- Locate, or install, a recent version of [Python](https://www.python.org/).
- Download `wad2obj.py` (use git, or GitHub's ZIP download button)
- In your terminal, `cd` into the folder where `wad2obj.py` is.
- run `pip3 install Pillow omgifol`
- then run `python3 wad2obj.py -h`

## WAD files

The excellent and freely available [Freedoom](https://freedoom.github.io/) levels can be [found here](https://freedoom.github.io/download.html).

The original [Shareware Doom](https://archive.org/details/DoomsharewareEpisode), or full [Doom](https://archive.org/details/doom-for-dosbox-0.74), Doom 2, Heretic several other games which used a similar engine each contain WAD files.

There are loads of Doom mods out there as well, though many of them are only usable when combined with the original Doom WADs from the commercial game. `wad2obj.py` may or may not work on those.

## Example

First, you'll need to get a listing of which maps are present in your WAD file.

```
% uv run wad2obj /tmp/freedoom1.wad --list
Loading /tmp/freedoom1.wad...
Found 36 maps:
  E1M1
  E1M2
  E1M3
  E1M4
  E1M5
  E1M6
  E1M7
 ...
```

Next, you can extract one, or several, maps like this. Note that `wad2obj.py` will output all the textures as well, so you want to send the output into a folder.

```
% uv run wad2obj /tmp/freedoom1.wad --maps E1M1 --center --output /tmp/freedoom_objs/
Loading /tmp/freedoom1.wad...
ERROR: Cannot find patch named 'TFOGF0' for texture_definition 'SLAD10'
ERROR: Cannot find patch named 'TFOGI0' for texture_definition 'SLAD10'
ERROR: Cannot find patch named 'TFOGF0' for texture_definition 'SLAD11'
ERROR: Cannot find patch named 'TFOGI0' for texture_definition 'SLAD11'
Found 1 maps matching pattern 'E1M1'
Writing E1M1.obj
```

## See Also

This other project may be helpful if you want objects, doors, etc.
https://bitbucket.org/freegodsoul/wad2unity/src/master/
