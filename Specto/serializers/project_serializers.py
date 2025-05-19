def ProjectDropdownResponseEntity(projects) -> list:
    return [{
        "id": str(project["_id"]),
        "name": project.get("name"),
    } for project in projects]
