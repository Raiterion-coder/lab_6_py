class Presentation:
    def __init__(self, tema, start_time, time):
        self.tema = tema
        self.start_time = start_time
        self.time = time
        self.end_time = start_time + time

    def overlaps(self, other):
        return not (self.end_time <= other.start_time or other.end_time <= self.start_time)

    def __str__(self):
        return f"{self.tema} ({self.start_time}-{self.end_time})"


class Conference:
    def __init__(self):
        self.presentations = []

    def add_presentation(self, presentation):
        for existing in self.presentations:
            if existing.overlaps(presentation):
                print(f"Ошибка: доклад '{presentation.tema}' пересекается с '{existing.time}'")
                return False
        self.presentations.append(presentation)
        self.presentations.sort(key=lambda p: p.start_time)
        print(f"Доклад '{presentation.tema}' успешно добавлен")
        return True

    def total_duration(self):
        return sum(p.time for p in self.presentations)

    def max_break(self):
        if len(self.presentations) < 2:
            return 0
        breaks = [self.presentations[i + 1].start_time - self.presentations[i].end_time
                  for i in range(len(self.presentations) - 1)]
        return max(breaks) if breaks else 0

    def print_schedule(self):
        print("Расписание конференции:")
        for i, p in enumerate(self.presentations, 1):
            print(f"{i}. {p}")


# Пример использования:
conference = Conference()

while True:
    print("\n1. Добавить доклад")
    print("2. Показать расписание")
    print("3. Общая продолжительность")
    print("4. Максимальный перерыв")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        tema = input("Введите тему доклада: ")
        start = float(input("Введите время начала (например, 9.5 для 9:30): "))
        time = float(input("Введите продолжительность (в часах): "))
        p = Presentation(tema, start, time)
        conference.add_presentation(p)
    elif choice == '2':
        conference.print_schedule()
    elif choice == '3':
        print(f"Общая продолжительность: {conference.total_duration()} часов")
    elif choice == '4':
        print(f"Максимальный перерыв: {conference.max_break()} часов")
    elif choice == '5':
        break