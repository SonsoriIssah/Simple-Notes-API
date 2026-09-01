from sqlalchemy.orm import mapped_column, Mapped
from database import Base


class Note(Base):
    __tablename__='notes'
    id:Mapped[int] =mapped_column(primary_key=True,index=True)
    title:Mapped[str] = mapped_column(nullable=False)
    content:Mapped[str] = mapped_column(nullable=True)

