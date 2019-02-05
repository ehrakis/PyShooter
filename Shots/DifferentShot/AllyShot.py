from Shots.DifferentShot.ShipShot import ShipShot


class AllyShot(ShipShot):
    """
    Represent an ally shot in-game
    """

    def __init__(self, vector: tuple, damage: int, position: tuple):
        super(AllyShot, self).__init__(vector, damage, position, "allyShot.bmp")

