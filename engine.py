from sqlalchemy import create_engine, Engine
from models import Base
import json

engine = create_engine("sqlite:///data/database.db", echo=True)
Base.metadata.create_all(engine)
