# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import List, Tuple
from abc import abstractmethod

# Local
from .notifier import Notifier

# -------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------------- class: Task --------------------------------------------------------- #

class Task:

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        tg_token: str,
        tg_chat_id: str
    ):
        self.notifier = Notifier(
            tg_token=tg_token,
            tg_chat_id=tg_chat_id
        )


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def start(self):
        self.notifier.start(self._scrape)


    # ---------------------------------------------------- Private methods --------------------------------------------------- #

    @abstractmethod
    def _scrape(self) -> Tuple[float, List[str]]:
        pass


# -------------------------------------------------------------------------------------------------------------------------------- #