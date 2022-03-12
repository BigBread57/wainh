import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.data_base.base import Base, engine
from src.data_base.models.game import Game
from src.data_base.models.utils import CacheChoiceType

players_in_room = sa.Table(
    'players_in_room',
    Base.metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('room_id', sa.Integer, sa.ForeignKey('room.id')),
    sa.Column('player_id', sa.Integer, sa.ForeignKey('player.id'))
)


class Player(Base):
    """Игрок."""
    ROLE = [
        (u'', u''),
        (u'leading', u'Ведущий'),
        (u'captain_unity', u'Капитан единства'),
        (u'captain_resistance', u'Капитан сопротивления'),
        (u'unity', u'Единство'),
        (u'resistance', u'Сопротивление'),
    ]

    STATUS = [
        (u'', u''),
        (u'silence', u'Молчание'),
    ]

    __tablename__ = 'player'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, nullable=False)
    username = sa.Column(sa.String(50), nullable=False)
    points = sa.Column(sa.Integer)
    role = sa.Column(
        CacheChoiceType(ROLE),
        default='',
    )
    status = sa.Column(
        CacheChoiceType(STATUS),
        default='',
    )
    rating = sa.Column(sa.Integer)
    rooms = relationship(
        'Room',
        secondary=players_in_room,
        back_populates='players',
    )


class Room(Base):
    """Комната."""
    __tablename__ = 'room'

    id = sa.Column(sa.Integer, primary_key=True)
    code = sa.Column(sa.Integer)
    game = sa.Column(sa.Integer, sa.ForeignKey(Game.id), nullable=False)
    players = relationship(
        'Player',
        secondary=players_in_room,
        back_populates='rooms',
    )
    created_at = sa.Column(sa.DateTime)


Base.metadata.create_all(engine)
