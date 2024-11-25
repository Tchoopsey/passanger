from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class MasterPassword(Base):
    __tablename__ = 'master_password'

    id: Mapped[int] = mapped_column(primary_key=True)
    master_password: Mapped[str] = mapped_column(String)

class ServicePasswords(Base):
    __tablename__ = 'service_passwords'

    id: Mapped[int] = mapped_column(primary_key=True)
    service: Mapped[str] = mapped_column(String(20))
    username: Mapped[str] = mapped_column(String(20))
    email_address: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
