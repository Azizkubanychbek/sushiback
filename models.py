import pandas as pd
import os
from datetime import datetime

# Пути к файлам базы данных
INGREDIENTS_FILE = 'ingredients.xlsx'
ROLLS_FILE = 'rolls.xlsx'
ROLL_RECIPES_FILE = 'roll_recipes.xlsx'
ORDERS_FILE = 'orders.xlsx'
EMPLOYEES_FILE = 'employees.xlsx'
ATTENDANCE_FILE = 'attendance.xlsx'
STOCK_HISTORY_FILE = 'stock_history.xlsx'

# Статусы заказов
ORDER_STATUSES = [
    'Принят',
    'Готовится',
    'Готов',
    'Отправлен',
    'Доставлен'
]

def init_db():
    if not os.path.exists(INGREDIENTS_FILE):
        df = pd.DataFrame(columns=['id', 'name', 'quantity', 'unit', 'price_per_unit'])
        df.to_excel(INGREDIENTS_FILE, index=False)
    if not os.path.exists(ROLLS_FILE):
        df = pd.DataFrame(columns=['id', 'name', 'sale_price'])
        df.to_excel(ROLLS_FILE, index=False)
    if not os.path.exists(ROLL_RECIPES_FILE):
        df = pd.DataFrame(columns=['roll_id', 'ingredient_id', 'amount_per_roll'])
        df.to_excel(ROLL_RECIPES_FILE, index=False)
    if not os.path.exists(ORDERS_FILE):
        df = pd.DataFrame(columns=['id', 'roll_id', 'quantity', 'order_time', 'total_price', 'cost_per_roll', 'status', 'comment'])
        df.to_excel(ORDERS_FILE, index=False)
    if not os.path.exists(EMPLOYEES_FILE):
        df = pd.DataFrame([
            {'id': 1, 'name': 'Админ', 'login': 'admin', 'password': 'admin123', 'role': 'admin'},
            {'id': 2, 'name': 'Шеф-повар', 'login': 'chef', 'password': '123345', 'role': 'chef'},
            {'id': 3, 'name': 'Сотрудник', 'login': 'staff', 'password': '123456', 'role': 'staff'},
            {'id': 4, 'name': 'Бухгалтер', 'login': 'accountant', 'password': '123789', 'role': 'accountant'}
        ])
        df.to_excel(EMPLOYEES_FILE, index=False)
    if not os.path.exists(ATTENDANCE_FILE):
        df = pd.DataFrame(columns=['employee_id', 'name', 'role', 'date', 'time', 'mark_type'])
        df.to_excel(ATTENDANCE_FILE, index=False)
    if not os.path.exists(STOCK_HISTORY_FILE):
        df = pd.DataFrame(columns=['date', 'ingredient_id', 'ingredient_name', 'operation', 'amount', 'comment'])
        df.to_excel(STOCK_HISTORY_FILE, index=False)

def fill_test_data():
    import numpy as np
    # Ингредиенты
    ingredients = [
        {'id': 1, 'name': 'Рис', 'quantity': 10, 'unit': 'кг', 'price_per_unit': 100},
        {'id': 2, 'name': 'Лосось', 'quantity': 5, 'unit': 'кг', 'price_per_unit': 800},
        {'id': 3, 'name': 'Сыр сливочный', 'quantity': 3, 'unit': 'кг', 'price_per_unit': 500},
        {'id': 4, 'name': 'Огурец', 'quantity': 2, 'unit': 'кг', 'price_per_unit': 120},
        {'id': 5, 'name': 'Нори', 'quantity': 100, 'unit': 'лист', 'price_per_unit': 20},
        {'id': 6, 'name': 'Крабовые палочки', 'quantity': 2, 'unit': 'кг', 'price_per_unit': 300},
        {'id': 7, 'name': 'Авокадо', 'quantity': 1, 'unit': 'кг', 'price_per_unit': 400},
        {'id': 8, 'name': 'Икра масаго', 'quantity': 0.5, 'unit': 'кг', 'price_per_unit': 1500},
        {'id': 9, 'name': 'Угорь', 'quantity': 1, 'unit': 'кг', 'price_per_unit': 1200},
        {'id': 10, 'name': 'Кунжут', 'quantity': 0.5, 'unit': 'кг', 'price_per_unit': 200},
    ]
    pd.DataFrame(ingredients).to_excel(INGREDIENTS_FILE, index=False)
    # Роллы
    rolls = [
        {'id': 1, 'name': 'Филадельфия', 'sale_price': ''},
        {'id': 2, 'name': 'Калифорния', 'sale_price': ''},
        {'id': 3, 'name': 'Каппа маки', 'sale_price': ''},
        {'id': 4, 'name': 'Унаги маки', 'sale_price': ''},
        {'id': 5, 'name': 'Крабовый ролл', 'sale_price': ''},
    ]
    pd.DataFrame(rolls).to_excel(ROLLS_FILE, index=False)
    # Рецепты роллов
    roll_recipes = [
        # Филадельфия
        {'roll_id': 1, 'ingredient_id': 1, 'amount_per_roll': 0.12}, # Рис
        {'roll_id': 1, 'ingredient_id': 2, 'amount_per_roll': 0.06}, # Лосось
        {'roll_id': 1, 'ingredient_id': 3, 'amount_per_roll': 0.03}, # Сыр
        {'roll_id': 1, 'ingredient_id': 5, 'amount_per_roll': 1},    # Нори
        # Калифорния
        {'roll_id': 2, 'ingredient_id': 1, 'amount_per_roll': 0.10}, # Рис
        {'roll_id': 2, 'ingredient_id': 6, 'amount_per_roll': 0.04}, # Крабовые палочки
        {'roll_id': 2, 'ingredient_id': 4, 'amount_per_roll': 0.02}, # Огурец
        {'roll_id': 2, 'ingredient_id': 8, 'amount_per_roll': 0.01}, # Икра масаго
        {'roll_id': 2, 'ingredient_id': 5, 'amount_per_roll': 1},    # Нори
        # Каппа маки
        {'roll_id': 3, 'ingredient_id': 1, 'amount_per_roll': 0.08}, # Рис
        {'roll_id': 3, 'ingredient_id': 4, 'amount_per_roll': 0.03}, # Огурец
        {'roll_id': 3, 'ingredient_id': 5, 'amount_per_roll': 1},    # Нори
        # Унаги маки
        {'roll_id': 4, 'ingredient_id': 1, 'amount_per_roll': 0.09}, # Рис
        {'roll_id': 4, 'ingredient_id': 9, 'amount_per_roll': 0.04}, # Угорь
        {'roll_id': 4, 'ingredient_id': 5, 'amount_per_roll': 1},    # Нори
        {'roll_id': 4, 'ingredient_id': 10, 'amount_per_roll': 0.005}, # Кунжут
        # Крабовый ролл
        {'roll_id': 5, 'ingredient_id': 1, 'amount_per_roll': 0.09}, # Рис
        {'roll_id': 5, 'ingredient_id': 6, 'amount_per_roll': 0.05}, # Крабовые палочки
        {'roll_id': 5, 'ingredient_id': 3, 'amount_per_roll': 0.02}, # Сыр
        {'roll_id': 5, 'ingredient_id': 5, 'amount_per_roll': 1},    # Нори
    ]
    pd.DataFrame(roll_recipes).to_excel(ROLL_RECIPES_FILE, index=False)

# Вызов инициализации при импорте
init_db()
# fill_test_data()  # ОТКЛЮЧЕНО: чтобы не затирать актуальные данные

def migrate_orders_add_status():
    if os.path.exists(ORDERS_FILE):
        df = pd.read_excel(ORDERS_FILE)
        if 'status' not in df.columns:
            df['status'] = 'Готовится'
            df.to_excel(ORDERS_FILE, index=False)
    # Создать файл для расхода по заказам, если нет
    ORDER_INGREDIENTS_FILE = 'order_ingredients.xlsx'
    if not os.path.exists(ORDER_INGREDIENTS_FILE):
        pd.DataFrame(columns=['order_id', 'ingredient_id', 'used_amount']).to_excel(ORDER_INGREDIENTS_FILE, index=False)
migrate_orders_add_status()
ORDER_INGREDIENTS_FILE = 'order_ingredients.xlsx' 