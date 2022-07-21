def add_digits(numbers):
    return sum(list(map(int, list(numbers))))

if __name__ == "__main__":
    numbers = input()
    print(add_digits(numbers))