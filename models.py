from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str] = mapped_column(String(50), unique=True)
    token:Mapped[str] = mapped_column(String(50))
    card:Mapped[int] = relationship("Card", back_populates="user", cascade='all, delete-orphan')

class Card(Base):
    __tablename__ = "card"
    id:Mapped[int] = mapped_column(primary_key=True)
    card_number:Mapped[str] = mapped_column(String(60))
    exp_month:Mapped[str] = mapped_column(String(2))
    exp_year:Mapped[str] = mapped_column(String(2))
    cvc:Mapped[str] = mapped_column(String(3))
    token:Mapped[str] = mapped_column(String(50))
    user_id:Mapped[int] = mapped_column(ForeignKey("user.id"))
    user:Mapped["User"] = relationship(back_populates="card")