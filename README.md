# My Django Shop

## Опис
Цей проект є інтернет-магазином, створеним за допомогою Django. Він дозволяє користувачам переглядати категорії продуктів, додавати продукти до кошика, оформляти замовлення та керувати профілем користувача.

## Встановлення
Щоб розгорнути цей проект локально, виконайте наступні кроки:

1. Клонування репозиторію:
    ```sh
    git clone https://github.com/venator2/Web_Pro_Ds.git
    cd my_store
    ```

2. Створіть та активуйте віртуальне середовище:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows використовуйте `venv\Scripts\activate`
    ```

3. Встановіть залежності:
    ```sh
    pip install -r requirements.txt
    ```

4. Застосуйте міграції бази даних:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Створіть суперкористувача:
    ```sh
    python manage.py createsuperuser
    ```

6. Запустіть сервер розробки:
    ```sh
    python manage.py runserver
    ```

## Використання
Після запуску сервера розробки, відкрийте браузер і перейдіть за адресою `http://127.0.0.1:8000/`. 

- Для входу в адмін-панель перейдіть за адресою `http://127.0.0.1:8000/admin/`.
- Для перегляду категорій, додавання продуктів до кошика та оформлення замовлень, використовуйте головну сторінку та відповідні розділи.

## Контакти
Якщо у вас є питання або пропозиції, будь ласка, зв'яжіться зі мною за допомогою електронної пошти: bohdan.konon@gmail.com
