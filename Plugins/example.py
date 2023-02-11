import json
from dataclasses import dataclass
from game.character import GameCharacter
from game import factory, loader

@dataclass
class Sorcerer:
    name: str
    def make_a_noise(self) -> None:
        print("magic aaaahhhhh")

@dataclass
class Wizard:
    name: str
    def make_a_noise(self) -> None:
        print("I'm a wizard, bitch!")

@dataclass
class Witcher:
    name: str
    def make_a_noise(self) -> None:
        print("swinging my sword")


def main() -> None:

    factory.register("sorcerer", Sorcerer)
    factory.register("wizard", Wizard)
    factory.register("witcher", Witcher)
 
    with open("./levels.json") as file:
        data = json.load(file)

    loader.load_plugins(data['plugins'])

    characters: list[GameCharacter] = [factory.create(item) for item in data["characters"]]

    for c in characters:
        print(c.name, end="\t")
        c.make_a_noise()

if __name__ == "__main__":
    main()
    