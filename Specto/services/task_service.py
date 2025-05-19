from bson import ObjectId
from datetime import datetime

from Specto.common.constants import StatusConstants
from Specto.common.messages import TaskMessages
from Specto.common.response import ResponseHandler
from Specto.config.db import task_collection
from Specto.helpers import build_paginated_response
from Specto.serializers.task_serializers import (TaskListResponseEntity,
                                                 TaskResponseEntity)


class TaskService:

    async def create_task(self, request, auth_user):
        task_response = dict()
        request_document = dict(request)
        request_document.update({
            "project_id": ObjectId(request_document.get("project_id")),
            "status": request_document.get('status').value,
            "created_by": ObjectId(auth_user.user_id),
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
        })
        task = await task_collection.insert_one(request_document)
        if task:
            document_obj = await task_collection.find_one({'_id': task.inserted_id})
            task_response = TaskResponseEntity(document_obj)
        return task_response
    
    async def list_task(self, page, limit):
        total_count = await task_collection.count_documents({})
        pipeline_filter = [
            {'$lookup' : {
                            'from': 'projects',
                            'localField': 'project_id',
                            'foreignField': '_id',
                            'as': 'project_name'
            }}, 
            {'$skip': (page-1)*limit},
            {'$limit': limit}, 
            {'$sort': {'_id': -1}}
        ]
        task_aggregates = await task_collection.aggregate(pipeline_filter).to_list(length=None)
        tasks_response = TaskListResponseEntity(task_aggregates)
        paginated_response = build_paginated_response(tasks_response, page, limit, total_count, message=TaskMessages.TASK_RETRIEVED_SUCCESSFULLY.value)
        return paginated_response
    
    async def retrieve_task(self, id):
        pipeline_filter = [
            {'$lookup' : {
                            'from': 'projects',
                            'localField': 'project_id',
                            'foreignField': '_id',
                            'as': 'project_name'
            }},
            {'$match': {
                '_id': ObjectId(id)
            }}
        ]
        task_record = await task_collection.aggregate(pipeline_filter).to_list(length=1)
        task_response = TaskListResponseEntity(task_record)
        return task_response
    
    async def update_task(self, request, id, auth_user):
        update_document = dict(request)
        update_document.update({
            "updated_at": datetime.utcnow(),
            "status": update_document.get("status").value,
            "project_id": ObjectId(update_document.get("project_id"))
        })
        filter_condition = {"_id": ObjectId(id)}
        update_query = {"$set": dict(update_document)}
        update_task = await task_collection.update_one(filter_condition, update_query)
        if update_task.modified_count:
            return True
        return False
    
    async def task_status(self):
        status_response = []
        for status in StatusConstants:
            status_response.append({
                'id': status.name,
                'name': status.value
            })

        return status_response
    
    