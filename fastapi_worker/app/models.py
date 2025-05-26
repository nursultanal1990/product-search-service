# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import String, Text, DateTime, func


# class Base(DeclarativeBase):
#     pass


# class Product(Base):
#     __tablename__ = "product"

#     id: Mapped[str] = mapped_column(String, primary_key=True)
#     name: Mapped[str] = mapped_column(Text)
#     description: Mapped[str | None] = mapped_column(Text, nullable=True)
#     created_at: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now())
