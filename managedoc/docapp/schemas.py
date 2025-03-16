from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form
from datetime import datetime

class DocumentBaseModel(BaseModel):
    titre:str=Field(example='rapport de stage')
    contenue:str=Field(example="Mon stage s'est déroulé sur la lune")

class DocumentCreateModel(DocumentBaseModel):
    pass

class DocumentUpdateModel(DocumentBaseModel):
    pass

class DocumentPatchModel(BaseModel):
    titre:Optional[str]=Field(example='rapport de stage',default=None)
    contenue:Optional[str]=Field(example="Mon stage s'est déroulé sur la lune",default=None)

class DocumentPydanticModel(DocumentBaseModel):
    id:int
    date_creation:datetime
    date_modification:Optional[datetime]
    class Config:
        from_attributes=True


