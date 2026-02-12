"""
models.py sirve para definir los modelos de la base de datos
"""

from sqlalchemy import Boolean, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase): # La clase Base sirve para declarar todos los modelos (tablas de la base de datos basados en Objetos)
    pass
    
class User(Base): # Declaramos la tabla User o el modelo. Tambien conocido como blueprint. Es un plano de la tabla User
    __tablename__ = "User"
    # Son las columnas de nuestra Tabla, y nos dice como se debe mapear en la bd
    id: Mapped[int] = mapped_column (primary_key = True)
    username: Mapped[str] = mapped_column (String(30))
    email: Mapped[str] = mapped_column (String(30))
    hashed_password: Mapped[str] = mapped_column (String(30), nullable=False)
    is_active: Mapped[bool] = mapped_column (Boolean, default = True)
    
    def __repr__(self) -> str:
        return f"User( id = {self.id}, username = {self.username}, email = {self.email}, password = {self.hashed_password}, is_active = {self.is_active})"

   