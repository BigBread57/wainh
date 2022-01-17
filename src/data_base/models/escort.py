import sqlalchemy as sa

from src.data_base.base import Base, engine
from src.data_base.models.utils import CacheChoiceType


class Escort(Base):
    """Сопровождение к игре."""
    TYPE = [
        (u'joke', u'Шутка'),
        (u'fact', u'Факт'),
        (u'toast', u'Тост'),
        (u'music', u'Музыка'),
        (u'other', u'Другое'),
    ]

    __tablename__ = 'escort'

    id = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column(sa.String(300), nullable=False)
    type = sa.Column(
        CacheChoiceType(TYPE),
        default='other',
    )


Base.metadata.create_all(engine)
