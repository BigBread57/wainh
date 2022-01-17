import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.data_base.base import Base, engine
from src.data_base.models.utils import CacheChoiceType


class Game(Base):
    """Настройка игры."""
    PAUSE = [
        (u'not_pause', u'Без пауз'),
        (u'drink', u'Разлевайте рюмки и готовьте тосты'),
        (u'tea', u'Чайная церемония'),
        (u'music', u'Музыкальная пауза'),
        (u'other', u'Другие развлечения'),
    ]

    __tablename__ = 'game'

    id = sa.Column(sa.Integer, primary_key=True)
    humor = sa.Column(sa.Boolean, default=False)
    view_pause = sa.Column(
        CacheChoiceType(PAUSE),
        default='not_pause',
    )
    point_unity = sa.Column(sa.Integer)
    point_resistance = sa.Column(sa.Integer)
    help_call_friends = sa.Column(sa.Boolean, default=False)
    help_question_yes_no = sa.Column(sa.Boolean, default=False)
    room = relationship(
        'Room',
        uselist=False,
        backref='game',
        cascade='all, delete'
    )


Base.metadata.create_all(engine)
