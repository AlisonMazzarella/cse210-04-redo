from game.casting.actor import Actor
from game.shared.point import Point


class Rock(Actor):
    """
    Responsibility: Exist as an actor, and add to the score when touched
    Specifics -
        Make a method that takes the current score, adds one to it, and returns the new score
    """

    def __init__(self):
        super().__init__()
        self.new_score = 0
        self._velocity = Point(0, 1)

    def get_score(self):
        return self.new_score

    def add_score(self, score):
        return score - 100