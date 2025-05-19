from fastapi import APIRouter, Depends, status

from Specto.common.messages import BaseMessages, TaskMessages
from Specto.common.response import ResponseHandler
from Specto.config.oauth import get_current_user
from Specto.decorators.transaction_decorator import with_transaction
from Specto.schemas.tasks_schema import TaskCreateSchema

from Specto.services import TaskService

router = APIRouter(prefix='/specto', tags=['Tasks'])

@with_transaction
@router.post('/create-task/', status_code=status.HTTP_201_CREATED)
async def create_task(request: TaskCreateSchema, auth_user: dict = Depends(get_current_user)):
    response_data = await TaskService().create_task(request, auth_user)
    return ResponseHandler.success(message=TaskMessages.TASK_CREATED_SUCCESSFULLY.value, data=response_data)

@router.get('/status-dropdown/', status_code=status.HTTP_200_OK)
async def status_dropdown():
    response_data = await TaskService().task_status()
    return ResponseHandler.success(message=BaseMessages.RECORD_RETRIEVED_SUCCESSFULLY.value, data=response_data)

@router.get('/task-list/', status_code=status.HTTP_200_OK)
async def task_list(page: int=1, limit: int=10, auth_user: dict = Depends(get_current_user)):
    paginated_response_data = await TaskService().list_task(page, limit)
    return ResponseHandler.success(message=TaskMessages.TASK_RETRIEVED_SUCCESSFULLY.value, data=paginated_response_data)

@router.get('/retrieve-task-details/{id}', status_code=status.HTTP_200_OK)
async def retrieve_task(id, auth_user: dict = Depends(get_current_user)):
    response_data = await TaskService().retrieve_task(id)
    return ResponseHandler.success(message=TaskMessages.TASK_RETRIEVED_SUCCESSFULLY.value, data=response_data)


@router.patch("/update-task/{id}", status_code=status.HTTP_200_OK)
async def update_task(id, request: TaskCreateSchema, auth_user: dict = Depends(get_current_user)):
    response_data = await TaskService().update_task(request, id, auth_user)
    return ResponseHandler.success(message=TaskMessages.TASK_UPDATED_SUCCESFULLY.value, data=response_data)
