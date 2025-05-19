from Specto.serializers import ProjectDropdownResponseEntity
from Specto.config.db import project_collection


def TaskResponseEntity(task) -> dict:
    return {
        "id": str(task['_id']),
        "title": task['title'],
        "description": task['description'],
        "start_date": task['start_date'],
        "end_date": task['end_date'],
        "project_id": str(task['_id'])
    }

def TaskListResponseEntity(tasks) -> list:
    return [
        {"id": str(task.get('_id')),
        "title": task.get('title'),
        "description": task.get('description'),
        "start_date": str(task.get('start_date')),
        "end_date": str(task.get('end_date')),
        "project_name": ProjectDropdownResponseEntity(task.get('project_name')),
        "status": {"id": task.get('status'), "name":task.get('status')},
        "estimated_hours": task.get('estimated_hours')
        }
        for task in tasks
        ]
   
