from sqlalchemy import Boolean, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass
    
class User(Base):
    __tablename__ = "User"
    
    id: Mapped[int] = mapped_column (primary_key = True)
    username: Mapped[str] = mapped_column (String(30))
    email: Mapped[str] = mapped_column (String(30))
    hashed_password: Mapped[str] = mapped_column (String(30), nullable=False)
    is_active: Mapped[bool] = mapped_column (Boolean, default = True)
    
    def __repr__(self) -> str:
        return f"User( id = {self.id}, username = {self.username}, email = {self.email}, password = {self.hashed_password}, is_active = {self.is_active})"

   