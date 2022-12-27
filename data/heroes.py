import sqlalchemy

from .db_session import SqlAlchemyBase




class SkinsGif(SqlAlchemyBase):
    __tablename__ = 'skins_gif'

    name = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    gif = sqlalchemy.Column(sqlalchemy.BLOB)

    def __repr__(self):
        return f"<Skins> {self.name} {self.gif}"


class Avatars(SqlAlchemyBase):
    __tablename__ = 'avatars_of_skins'

    name = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    image = sqlalchemy.Column(sqlalchemy.BLOB)

    def __repr__(self):
        return f"<Images> {self.name} {self.image}"