# Практическая работа №5

def greet(name):
    print("Привет,", name)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def main():
    greet("Студент")
    print("Сложение:", add(5, 3))
    print("Вычитание:", subtract(10, 4))
    print("Умножение:", multiply(6, 7))

if __name__ == "__main__":
    main()
    def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка"

print("Деление:", divide(8, 2))
