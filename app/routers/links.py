from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.links import Linking
from app.schemas.links import URLCreate, URLResponse
import secrets
import string

router = APIRouter(prefix="/links")

@router.post("/shorten", response_model=URLResponse)
def send_url(url_data: URLCreate, db: Session=Depends(get_db)):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(secrets.choice(characters) for _ in range(6)) 

    while db.query(Linking).filter(Linking.short_code == short_code).first():
        short_code = ''.join(secrets.choice(characters) for _ in range(6)) 

    new_link = Linking(
        full_link = url_data.full_link,
        short_code = short_code
    )  

    db.add(new_link)
    db.commit()
    db.refresh(new_link)

    return new_link