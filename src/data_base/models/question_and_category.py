import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.data_base.base import Base, engine
from src.data_base.models.utils import CacheChoiceType


categories_questions = sa.Table(
    'categories_questions',
    Base.metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('question_id', sa.Integer, sa.ForeignKey('question.id')),
    sa.Column('category_id', sa.Integer, sa.ForeignKey('category.id')),
)


class Question(Base):
    """Вопрос."""

    STATUS = [
        (u'moderation', u'На модерации'),
        (u'rejected', u'Отклонено'),
        (u'accepted', u'Принято'),
    ]

    __tablename__ = 'question'

    id = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column(sa.String(500), nullable=False)
    answer = sa.Column(sa.String(100), nullable=False)
    count_right = sa.Column(sa.Integer())
    count_wrong = sa.Column(sa.Integer())
    files = relationship(
        'File',
        backref='question',
        cascade='all, delete',
        lazy='dynamic',
    )
    categories = relationship(
        'Category',
        secondary=categories_questions,
        back_populates='questions',
    )
    status = sa.Column(CacheChoiceType(STATUS))


class Category(Base):
    """Категория."""
    __tablename__ = 'category'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    questions = relationship(
        'Question',
        secondary=categories_questions,
        back_populates='categories',
    )


Base.metadata.create_all(engine)
