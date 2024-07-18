def load_phonebook(filename):
    phonebook = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    phonebook.append({
                        'last_name': parts[0],
                        'first_name': parts[1],
                        'middle_name': parts[2],
                        'phone_number': parts[3]
                    })
    except FileNotFoundError:
        print(f"Файл {filename} не найден, создаем новый справочник.")
    return phonebook

def save_phonebook(phonebook, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in phonebook:
            file.write(f"{entry['last_name']},{entry['first_name']},{entry['middle_name']},{entry['phone_number']}\n")

def display_phonebook(phonebook):
    if not phonebook:
        print("Справочник пуст.")
    else:
        for i, entry in enumerate(phonebook):
            print(f"{i+1}. Фамилия: {entry['last_name']}, Имя: {entry['first_name']}, Отчество: {entry['middle_name']}, Телефон: {entry['phone_number']}")

def search_phonebook(phonebook, query):
    results = [entry for entry in phonebook if query in entry.values()]
    if results:
        for entry in results:
            print(f"Фамилия: {entry['last_name']}, Имя: {entry['first_name']}, Отчество: {entry['middle_name']}, Телефон: {entry['phone_number']}")
    else:
        print("Запись не найдена.")

def add_entry(phonebook):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    phonebook.append({
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    })

def copy_entry(source_filename, target_filename, line_number):
    source_phonebook = load_phonebook(source_filename)
    if 1 <= line_number <= len(source_phonebook):
        entry = source_phonebook[line_number - 1]
        target_phonebook = load_phonebook(target_filename)
        target_phonebook.append(entry)
        save_phonebook(target_phonebook, target_filename)
        print("Запись успешно скопирована.")
    else:
        print("Неверный номер строки.")