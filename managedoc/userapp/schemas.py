from typing import List, Optional
from elrahapi.user import  model

class UserBaseModel(model.UserBaseModel):
    pass

class UserCreateModel(model.UserCreateModel):
    pass

class UserUpdateModel(model.UserUpdateModel):
    pass

class UserPatchModel(model.UserPatchModel):
    pass

class UserPydanticModel(model.UserPydanticModel):
    class Config :
        from_attributes=True



