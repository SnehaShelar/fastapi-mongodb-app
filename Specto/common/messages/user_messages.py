from enum import Enum

class UserMessages(Enum):
    CONFIRM_PASSWORD = "Password & Confirm Password must be same."
    EMAIL_ALREADY_REGISTERED = "Email is already registered."
    USER_REGISTERED_SUCCESSFULLY = "User is registered successfully."
    USER_LOGGED_SUCCESSFULLY = "User logged in successfully."
    USER_LOGGED_OUT_SUCCESSFULLY = "User logged out successfully."
    