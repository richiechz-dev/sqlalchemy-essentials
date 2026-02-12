from sqlalchemy import create_engine # Es la funcion para crear el motor. El motor es el objeto que conoce como conectrase a la base de datos
from sqlalchemy.orm import sessionmaker # Es el modulo del orm de sqlalchemy para crar la session, es el constructor de sessiones ORM, sessionmaker es una fabrica que produce instancias concentadas al engine

engine = create_engine("sqlite:///:memory:", echo=True)
SessionLocal = sessionmaker(bind=engine)    #SessionLocal es un objeto fabrica, pues implementa el patron factory

def get_session(): # Creamos esta funcion simple para obtener una session desde cualquiera parte del proyecto
    return SessionLocal()


    
