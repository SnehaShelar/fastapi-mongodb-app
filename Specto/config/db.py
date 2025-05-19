from motor.motor_asyncio import AsyncIOMotorClient
from Specto.settings import app_settings

# Create MongoDB Client
client = AsyncIOMotorClient(app_settings.MONGO_URI)

database = client[app_settings.DATABASE_NAME]
project_collection = database.get_collection("projects")
user_collection = database.get_collection("users")
task_collection = database.get_collection("tasks")
user_device_token_collection = database.get_collection("user_device_tokens")
attendance_history_collection = database.get_collection("attendance_history")
