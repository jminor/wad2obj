help:
	@echo "Available targets:"
	@echo "  shareware - Download and process Doom shareware WAD"
	@echo "  freedoom  - Download and process Freedoom WAD"

dls/doom-shareware.zip:
	mkdir -p dls
	curl -L -o $@ https://archive.org/download/DoomsharewareEpisode/doom.ZIP

dls/DOOM1.WAD: dls/doom-shareware.zip
	(cd dls; unzip -o doom-shareware.zip DOOM1.WAD)

shareware: dls/DOOM1.WAD
	uv run wad2obj $< --list
	mkdir -p out
	uv run wad2obj $< -m E1M1 -o out

dls/freedoom.zip:
	curl -L -o $@ https://github.com/freedoom/freedoom/releases/download/v0.13.0/freedoom-0.13.0.zip

dls/freedoom1.wad: dls/freedoom.zip
	(cd dls; unzip -o -j freedoom.zip freedoom-0.13.0/freedoom1.wad)

freedoom: dls/freedoom1.wad
	uv run wad2obj $< --list
	mkdir -p out
	uv run wad2obj $< -m E1M1 -o out
