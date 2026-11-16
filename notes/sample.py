def greet(name: str) -> str:
    return f"hi {name}"


class Counter:
    def __init__(self) -> None:
        self.n = 0

    def tick(self) -> int:
        self.n += 1
        return self.n
