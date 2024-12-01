import os
import time


def filter_files():
    while True:
        try:
            filter_time = input('[ОПЦИОНАЛЬНО] Введите время с создания файла: ')
            if filter_time:
                filter_time = int(filter_time)
            else:
                filter_time = None
            break
        except ValueError:
            print('Ошибка! Введите целое число или пропустите фильтрацию (пустая строка)')

    filter_extension = input('[ОПЦИОНАЛЬНО] Введите расширение файла: ')

    return filter_time, filter_extension


def search_files(directory, lifetime, extension):
    found_files = []

    walk = os.walk(directory)

    for path, _, files in walk:
        for file in files:
            file_path = os.path.join(path, file)

            if lifetime:
                if time.time() - os.path.getctime(file_path) > lifetime:
                    continue

            if extension:
                if not file.endswith(extension):
                    continue

            found_files.append(file_path)

    return found_files


def main():
    home_dir = input('Введите путь: ')
    if not os.path.exists(home_dir):
        print('[ОШИБКА] Директория не найдена!')
    else:
        filter_time, filter_extension = filter_files()
        found_files = search_files(home_dir, filter_time, filter_extension)
        if found_files:
            print('\n'.join(found_files))
            print('Спасибо, что пользуетесь нашим сервисом!')
        else:
            print('Файлы не найдены.')


if __name__ == '__main__':
    main()
