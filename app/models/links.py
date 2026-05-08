from sqlalchemy import String, Column, Integer, DateTime, Boolean
from datetime import datetime
from app.database import Base

class Linking(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, index=True)
    full_link = Column(String, unique=False, nullable=False)
    short_code = Column(String, index=True, unique=True, nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean, default=True)