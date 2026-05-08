from pydantic import BaseModel
from datetime import datetime
from pydantic import ConfigDict
from pydantic import HttpUrl

class URLCreate(BaseModel):
    full_link: HttpUrl
    
class URLResponse(BaseModel):
    id: int
    full_link: str
    short_code: str
    date_created: datetime
    active: bool
    model_config = ConfigDict(from_attributes=True)

class DeleteResponse(BaseModel):
    message:str