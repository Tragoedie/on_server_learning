import os
from zipfile import ZipFile


def get_archive(zip_name, extension_file):
    directory = 'G:/python_1/ZipFile/'
    archive_name = zip_name + '.zip'
    if os.path.isfile(directory + archive_name) is True:
        print('Такое имя архива уже существует')
    else:
        change = False
        with ZipFile(archive_name, 'w') as Zip_File:
            for root, folders, file_names in os.walk(directory):
                for file_name in file_names:
                    if file_name.endswith('.' + extension_file):
                        print(file_name)
                        change = True
                        Zip_File.write(file_name)
        if change is False:
            os.remove(archive_name)
            print('Файлов с таким расширением не найдено')
