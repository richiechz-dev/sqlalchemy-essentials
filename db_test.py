
from sqlalchemy import select
from database import engine, get_session
from models import Base, User


def main():
    Base.metadata.create_all(bind=engine) # Crea la bd a partir de la metadata (los modelos declarados en models.py)
    
    
    with get_session() as session:
        query = User(username = "rdev", email = "rchz.nomad@gmail.com", hashed_password = "no password", is_active = True)
        session.add(query)
        session.commit()
    
    with get_session() as session:
        result = session.execute(select(User).where(User.username == "rdev"))
        users = result.scalars().all()
        print(users)
        session.commit()
        
    
if __name__ == "__main__":
    main()