from sqlalchemy import Column, Integer, String
from db_connection import Base, engine

class UserInDB(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, unique=True)
    password = Column(String)
    balance = Column(Integer)

Base.metadata.create_all(bind=engine)


"""
from typing import Dict
from pydantic import BaseModel

# Bloque 1: definición de UserInDB
class UserInDB(BaseModel): # (BaseModel) indica la herencia (extends en Java)
    username: str
    password: str
    balance: int


# Bloque 2: definición de la base de datos ficticia
database_users = Dict[str, UserInDB]    # Esta definición dice que en el diccionario
                                        # la llave es "str", y el valor es el objeto "UserInDB"

database_users = {
    "camilo24": UserInDB(**{"username":"camilo24", # los ** hace un mapeo a los atributos de la clase (instanciar)
                            "password":"root",
                            "balance":12000}),
    "andres18": UserInDB(**{"username":"andres18",
                            "password":"hola",
                            "balance":34000}),
}

# Bloque 3: definición de funciones sobre la base de datos ficticia
def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db 

"""