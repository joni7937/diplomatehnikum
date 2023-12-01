from fastapi import APIRouter

from health import UsersHealthValidator, EditHealthRecordValidator

from database.healthservice import add_health_info_db, edit_health_info_db, delete_health_info_db

health_router = APIRouter(prefix='/user_health', tags=['Данные о здоровье пользователей'])


@health_router.post('/add_health')
async def add_health(data: UsersHealthValidator):
    result = add_health_info_db(**data.model_dump())

    return {'message': result}


@health_router.put('/edit_health')
async def edit_health(data: EditHealthRecordValidator):
    change_health = data.model_dump()

    result = edit_health_info_db(**change_health)

    if result:
        return {'message': result}
    else:
        return {'message': "Нет такой информации что бы изменить"}


@health_router.delete('/delete_health')
async def delete_health(user_id: int):
    result = delete_health_info_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Нет данных что бы удалить'}