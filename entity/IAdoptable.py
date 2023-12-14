from abc import ABC, abstractmethod


class IAdoptable(ABC):
    @abstractmethod
    def Adopt(self):
        pass
