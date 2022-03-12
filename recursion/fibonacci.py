class Fibonacci:
    
    def Fib(self, n: int) -> int:

        if n < 2:
            return n

        return self.Fib(n - 1) + self.Fib(n - 2)


if __name__ == "__main__":
    fibonacci = Fibonacci()
    print(fibonacci.Fib(9))