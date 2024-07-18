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