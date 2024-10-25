def main():
    print("Введите числовые строки одну за другой. Чтобы завершить ввод, введите пустую строку.")

    total_sum = 0
    while True:
        user_input = input("Введите строку: ").strip()

        try:
            # Удаляем пробелы и преобразуем строку в число
            number = int(user_input.replace(" ", ""))
            total_sum += number
        except ValueError:
            print("Пожалуйста, введите только числовые строки.")
        print(total_sum)

    print(f"Сумма числовых строк: {total_sum}")


if __name__ == "__main__":
    main()