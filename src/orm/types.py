import re
from enum import Enum as PyEnum
from sqlalchemy import TypeDecorator, String

class Roles(PyEnum):
    USER = "user"
    ADMIN = "admin"
    SUPERADMIN = "superadmin"

class LowerString(TypeDecorator):
    impl = String
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if isinstance(value, str):
            return value.lower()
        return value

    def process_result_value(self, value, dialect):
        if isinstance(value, str):
            return value.lower()
        return value

class EmailString(LowerString):
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if isinstance(value, str):
            if not re.match(r"^[\w\d_]+@[\w]+(\.[\w]{1,4}){1,2}$", value):
                raise ValueError("Invalid email format")
        return super().process_bind_param(value, dialect)
