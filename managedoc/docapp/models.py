from sqlalchemy import (
    Boolean,
    Column,
    DECIMAL,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text,
    Table,
)
from managedoc.settings.database import Base

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True,index=True)
    titre = Column(String(30),nullable=False)
    date_creation = Column(DateTime(timezone=True), default=func.now())
    date_modification = Column(DateTime(timezone=True),nullable=True,onupdate=func.now())
    contenue=Column(Text,nullable=False)
    # proprietaire_id = Column(Integer,ForeignKey('users.id'))
    # proprietaire = relationship("User",back_populates="documents")

metadata= Base.metadata
