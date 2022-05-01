# Функционал принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.
import requests
from pprint import pprint

files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
token = ''

class YaUploader:
    files_url: str = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    upload_url: str = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    @property
    def header(self):
        return self.get_headers()

    def get_upload_link(self, file_path: str):
        """получить ссылку для загрузки файла на яндекс диск"""
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(self.upload_url, params=params, headers=self.header)
        return response.json()

    def upload(self, file_path: str, file_name: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_upload_link(file_path).get('href')
        if not href:
            return False

        response = requests.put(href, data=open(file_path, 'rb'))
        if response.status_code == 201:
            print('Файл загружен')
            return True


ya = YaUploader(token)
ya.upload('1.txt', '1.txt')