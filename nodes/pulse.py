from timeflux.core.node import Node


class Pulse(Node):
    """Transform a sine signal to a pulse signal.

    Attributes:
        o (Port): Default output, provides DataFrame.

    Args:
        threshold (float): duty cycle
    """

    def __init__(self, threshold=0):
        self._threshold = threshold

    def update(self):
        if not self.i.ready():
            return
        self.o.data = None # Edit this line!
