from fastapi import APIRouter

from users import LoginUserValidator, RegisterUserValidator, EditUserValidator

from database.userservice import login_user_db, register_user_db, edit_user_db, delete_user_db, get_exact_user_db

user_router = APIRouter(prefix='/user', tags=['Управление пользователями'])


@user_router.post('/login')
async def login_user(data: LoginUserValidator):
    result = login_user_db(**data.model_dump())

    return {'message': result}


@user_router.post('/register')
async def register_user(data: RegisterUserValidator):
    result = register_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Пользователь с этой почтой имеется'}


@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такого пользователя нету'}


@user_router.put('/edit')
async def edit_user(data: EditUserValidator):
    change_data = data.model_dump()

    result = edit_user_db(**change_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'Нет пользователя что бы изменить'}


@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Нет пользователя что бы удалить '}