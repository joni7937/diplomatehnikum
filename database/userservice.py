from database.models import User

from database import get_db

from datetime import datetime


def register_user_db(username, email, phone_number, password):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return True

    new_user = User(username=username, email=email, phone_number=phone_number, password=password)

    db.add(new_user)
    db.commit()

    return "Пользователь успешно зарегистрирован"


def login_user_db(email, password):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        if checker.password == password:
            return checker
        elif checker.password != password:
            return "Неверный пароль"
    return "Ошибка в данных"


def edit_user_db(id, edit_data, new_data):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=id).first()

    if exact_user:
        if edit_data == 'email':
            exact_user.email = new_data
        elif edit_data == 'password':
            exact_user.password = new_data

        db.commit()

        return 'Данные успешно изменены'
    else:
        return 'Пользователь не найден'


def get_exact_user_db(id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=id).first()

    return exact_user


def delete_user_db(id):
    db = next(get_db())

    delete_user = db.query(User).filter_by(id=id).first()

    if delete_user:
        db.delete(delete_user)
        db.commit()

        return 'Пользователь успешно удален'
    else:
        return 'Пользователь не найден'



