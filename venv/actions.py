class Action:
    pass

# subclass of action
# esc key to exit game
class EscapeAction(Action):
    pass

# subclass of action
# move player around
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy