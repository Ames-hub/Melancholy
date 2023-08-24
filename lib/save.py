from .jmod import jmod
import os

save_file_dt = {
    "player": {
        "name": None,
        "location": None,
        "progress": 0, # The chapter the player is on
        "inventory": {
            "money": 50,
            "items": {}
        }
    },
}

class load():
    def __init__(self) -> None:
        self.player_name = jmod.getvalue("player.name", "lib/data/save.json", dt=save_file_dt, default="Aria")

def get(key):
    return jmod.getvalue(key, "lib/data/save.json", dt=save_file_dt, default=None)

class save():
    def __init__(self) -> None:
        self.load = load()

    def save(player_name, player_location, player_inventory: dict, chapter=0):
        '''Saves the game'''
        save_file_dt["player"]["name"] = str(player_name)
        save_file_dt["player"]["location"] = str(player_location)
        save_file_dt["player"]["inventory"] = player_inventory

        jmod.setvalue(
            key="player.name",
            json_dir="lib/data/save.json",
            dt=save_file_dt,
            value=player_name
        )

    def exists():
        '''Checks if a save file exists'''
        if os.path.exists("lib/data/save.json"):
            return True
        else:
            return False