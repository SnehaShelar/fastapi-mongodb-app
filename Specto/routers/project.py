from fastapi import APIRouter, Depends, status

from Specto.common.messages import ProjectMessages
from Specto.common.response import ResponseHandler
from Specto.config.db import project_collection
from Specto.schemas.project_schema import Project
from Specto.serializers import ProjectDropdownResponseEntity

router = APIRouter(
    prefix='/specto',
    tags=['Projects']
)

@router.post("/project/", status_code=status.HTTP_201_CREATED)
async def create(project: Project):
    proj = await project_collection.insert_one(dict(project))
    return {"message": ProjectMessages.PROJECT_CREATED}

@router.get("/project-dropdown/", status_code=status.HTTP_200_OK)
async def project_dropdown():
    project_objects = await project_collection.find().sort("_id", -1).to_list(length=None)
    dropdown_response = ProjectDropdownResponseEntity(project_objects)
    return ResponseHandler.success(message=ProjectMessages.PROJECT_RETRIEVED_SUCCESSFULLY.value, data=dropdown_response)

