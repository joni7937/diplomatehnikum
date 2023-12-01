from database.models import UserHealthData

from database import get_db

from datetime import datetime


def add_health_info_db(user_id, weight, height, gender, pulse):
    db = next(get_db())

    new_health_info = UserHealthData(user_id=user_id, weight=weight, height=height, gender=gender, pulse=pulse)

    db.add(new_health_info)
    db.commit()

    return "Данные успешно добавлены"


def edit_health_info_db(user_id, edit_data, new_data):
    db = next(get_db())

    exact_edit_info = db.query(UserHealthData).filter_by(id=user_id).first()

    if exact_edit_info:
        if edit_data == "weight":
            exact_edit_info.weight = new_data
        elif edit_data == "height":
            exact_edit_info.height = new_data
        elif edit_data == "pulse":
            exact_edit_info.pulse = new_data

        db.commit()
        return 'Данные о здоровье успешно изменены'
    else:
        return 'Запись о здоровье не найдена'


def delete_health_info_db(user_id):
    db = next(get_db())

    delete_health = db.query(UserHealthData).filter_by(user_id=user_id).first()

    if delete_health:
        db.delete(delete_health)
        db.commit()

        return "Данные удалены"
    else:
        return "Данные не найдены"

