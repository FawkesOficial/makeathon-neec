import threading
from typing import Callable


class EventHandler:

    def __init__(self):
        self.events: dict[str, Callable] = {}

    def register_event(self, event_name: str, callback: Callable) -> None:
        """Registers a function to be called when an event happens"""

        self.events[event_name] = callback

    def trigger_event(self, event_name: str, *args, **kwargs) -> None:
        """Calls the function associated with the event"""

        if event_name in self.events:
            thread = threading.Thread(target=self.events[event_name], args=args, kwargs=kwargs)
            thread.start()

