import gspread
import asyncio
from google.oauth2.service_account import Credentials

class GoogleSheetsManager:
    def __init__(self, credentials_path, spreadsheet_id):
        """Инициализирует менеджер Google Sheets с данными для подключения."""
        self.spreadsheet_id = spreadsheet_id
        self.client = None
        self.sheet = None
        self.credentials_path = credentials_path

    async def authenticate(self):
        """Аутентификация через сервисный аккаунт и возвращение клиента gspread."""
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file(self.credentials_path, scopes=scopes)
        self.client = gspread.authorize(creds)
        self.sheet = self.client.open_by_key(self.spreadsheet_id).sheet1

    async def save_to_sheet(self, data):
        """Добавляет новую строку данных в таблицу."""
        await self.authenticate()
        row_data = data  # Добавляем никнейм в начало данных
        await asyncio.to_thread(self.sheet.append_row, row_data)

    async def read_from_sheet(self, row_number):
        """Читает и возвращает данные из указанной строки таблицы."""
        await self.authenticate()
        return await asyncio.to_thread(self.sheet.row_values, row_number)
