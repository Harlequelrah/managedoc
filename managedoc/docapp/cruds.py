from elrahapi.crud.crud_models import CrudModels
from managedoc.docapp.models import Document  #remplacer par l'entité SQLAlchemy
from managedoc.docapp.schemas import DocumentCreateModel, DocumentUpdateModel,DocumentPatchModel,DocumentPydanticModel
from elrahapi.crud.crud_forgery import CrudForgery
from managedoc.settings.database import authentication


myapp_crud_models = CrudModels(
    entity_name='document',
    primary_key_name='id',  #remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=Document, #remplacer par l'entité SQLAlchemy
    CreateModel=DocumentCreateModel, #Optionel
    UpdateModel=DocumentUpdateModel, #Optionel
    PatchModel=DocumentPatchModel, #Optionel
    PydanticModel=DocumentPydanticModel #Optionel
)
myapp_crud = CrudForgery(
    crud_models=myapp_crud_models,
    session_factory= authentication.session_factory
)
