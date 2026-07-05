from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey

from app.models import db, Statistics, Response


class Question(db.Model):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(100))

    statistics: Mapped['Statistics'] = relationship(back_populates='question', uselist=False)
    responses: Mapped[list['Response']] = relationship(back_populates='question')
    categories_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category: Mapped['Category'] = relationship(back_populates='question')

    def __str__(self):
        return self.text

    def __repr__(self):
        return f'id={self.id}, text={self.text}'


class Category(db.Model):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(String(255), nullable=True)
    question: Mapped[list['Question']] = relationship(back_populates='category')

    def __str__(self):
        return self.text

    def __repr__(self):
        return f'id={self.id}, text={self.text}'


