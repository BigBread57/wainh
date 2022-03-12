import sqlalchemy as sa

from src.data_base.base import Base, engine
from src.data_base.models.question_and_category import Question


class File(Base):
    """Файлы, прикрепелнные к вопросу."""
    __tablename__ = 'file'

    id = sa.Column(sa.Integer, primary_key=True)
    question_id = sa.Column(sa.Integer, sa.ForeignKey(Question.id), nullable=False)
    file = sa.Column(sa.String(200), nullable=False)
    type = sa.Column(sa.String(20), nullable=False)


Base.metadata.create_all(engine)
