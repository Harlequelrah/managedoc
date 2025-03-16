from .database import Base
from managedoc.docapp.models import metadata as myapp_metadata
# from managedoc.docapp2.models import metadata as myapp2_metadata
from sqlalchemy import MetaData

target_metadata = MetaData()

target_metadata = Base.metadata
target_metadata = myapp_metadata
# target_metadata = myapp2_metadata
