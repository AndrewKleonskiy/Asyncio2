from threading import RLock
from typing import List


class InListThreadsafe:

    def __init__(self, wrapped_list: List[int]):
        self._lock = RLock()
        self.__inner_list = wrapped_list

    def indices_off(self, to_find: int) -> List[int]:
        with self._lock:
            enumerator = enumerate(self.__inner_list)
            return [index for index, value in enumerator if value == to_find]

    def find_and_replace(self, to_replace: int, replace_with: int) -> None:
        with self._lock:
            indices = self.indices_off(to_replace)
            for index in indices:
                self.__inner_list[index] = replace_with


threadsafe_list = InListThreadsafe([1, 2, 1, 2, 1])
threadsafe_list.find_and_replace(1, 2)

x
