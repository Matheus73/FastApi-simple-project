from sqlalchemy import Column, String, Integer

from database import Base

class Book(Base):
    __tablename__ = 'livro'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor = Column(String)
    ano = Column(Integer)

    def __init__(self, id, titulo, autor, ano):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __repr__(self):
        return '<Livro %r>' % self.titulo
