from sqlalchemy.orm import Session
from sqlalchemy.orm import exc

from . import models, schemas

from app.model.database import MysqlSession


async def create_translate(translate: schemas.TranslateCreate):
    # SQLAlchemy 모델 인스턴스를 만들고 데이터를 넣습니다.
    query = models.Translate(src_lang=translate.sl,
                             src_text=translate.text,
                             tgt_lang=translate.tl,
                             mt_text=translate.mt
                             )
    try:
        # db 세션 지정
        db = MysqlSession()
        db.add(query)
        db.commit()
        db.refresh(query)
    # 기본키에 어긋나는 데이터가 DB에 들어가면 발생
    except exc.IntegrityError:
        raise
    except exc.OperationalError:
        db.rollback()
        raise


async def get_history(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Translate).offset(skip).limit(limit).all()
