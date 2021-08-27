def igor(n:int = 5) -> bool:
    if n == 5:
        print("Ну ты и ленивец")
        return False
    else:
        print("Молодец")
        return True


if __name__ == "__main__":
    print(igor(int(input("Число: "))))
