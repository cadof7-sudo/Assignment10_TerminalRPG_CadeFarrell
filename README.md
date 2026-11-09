# The Shattered Crown — Terminal RPG

## Requirements
- Python 3.10+
- `uv`

## Setup
From this folder, run:

```bash
uv init
uv add tinydb colorama
uv run python main.py
```

If the folder already contains a `pyproject.toml`, just run `uv add tinydb colorama`.

## Controls
- `W A S D`: move
- `T`: talk/interact with the person or feature on your tile
- `B`: travel between the village and Whispering Woods (entering the woods starts an encounter)
- `I`: inventory
- `C`: character status
- `Q`: quest journal
- `F`: learn Heal
- `SAVE`: save progress
- `X`: save and log out

Create an account, log in, and your progress is stored in `rpg_data.json`.

## Project modules
`main.py` starts the program; `auth.py` handles accounts; `database.py` handles TinyDB; `game.py` runs the game loop; `player.py` stores character state; `world_map.py` handles map layouts and movement; `monster.py` and `skill.py` demonstrate inheritance; `combat.py` runs battles; `item.py` and `inventory.py` handle items; `quest.py` tracks quest progress; `npc.py` defines NPC dialogue; `shop.py` handles purchases.
