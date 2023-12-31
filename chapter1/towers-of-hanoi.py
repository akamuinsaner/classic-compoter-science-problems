from typing import TypeVar, Generic, List
T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self) -> None:
        self.container: List[T] = []


    def push(self, item: T) -> None:
        self.container.append(item)

    def pop(self) -> T:
        return self.container.pop()

    def __repr__(self) -> str:
        return repr(self.container)

num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)

def haoni(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        haoni(begin, temp, end, n - 1)
        haoni(begin, end, temp, 1)
        haoni(temp, end, begin, n - 1)

if __name__ == "__main__":
    haoni(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)
