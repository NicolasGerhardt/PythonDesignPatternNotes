from dataclasses import dataclass
from game import factory
from random import randint

@dataclass
class Bard:
    name: str

    def make_a_noise(self) -> None:
        choice = randint(0,2)
        songs = [
            "toss a coin to your witcher!",
            "Thunder Struck",
            "And I'm a free bird!"
            ]
        print(songs[choice])



def init() -> None:
    factory.register("bard", Bard) 