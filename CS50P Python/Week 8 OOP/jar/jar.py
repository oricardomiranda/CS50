class Jar:
    def __init__(self, capacity=12):
       if capacity < 0:
            raise ValueError("Capacity cannot be negative")
       self._capacity = capacity
       self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self._capacity:
            raise ValueError("Too many cookies")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies")
        self.size -= n

    # Getter
    @property
    def capacity(self):
        return self._capacity

    # Setter
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity error")
        self._capacity = capacity

    # Getter
    @property
    def size(self):
        return self._size

    # Setter
    @size.setter
    def size(self, size):
        if size > self._capacity:
            raise ValueError("Size error")
        self._size = size

def main():
    jar = Jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.deposit(4)
    print(jar)
    jar.withdraw(2)
    print(jar)

if __name__ == "__main__":
    main()
