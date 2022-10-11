from datetime import datetime
from sqlalchemy import (Column, ForeignKey, Integer, String, DateTime, Text,
                        Boolean, Table)
from sqlalchemy.orm import relationship
from app.database import ModelBase

class User(ModelBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255, collation='utf8_bin'), nullable=False, index=True, unique=True)
    email = Column(String(255, collation='utf8_bin'), nullable=False, index=True, unique=True)
    passhash = Column(String(500, collation='utf8_bin'), nullable=False)
    status = Column(String(50, collation='utf8_bin'), nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    verifications = relationship('UserVerification', back_populates='user')
    skill_revisions = relationship('SkillRevision', back_populates='contributor')

    def __repr__(self):
        return f'User(id={self.id!r}, username={self.username!r}, email={self.email!r}, passhash={self.passhash!r}, status={self.status!r}, created={self.created!r}, updated={self.updated!r})'


class UserVerification(ModelBase):
    __tablename__ = 'user_verifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    url_key = Column(String(45, collation='utf8_bin'), nullable=False)
    status = Column(String(50, collation='utf8_bin'), nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship('User', back_populates='verifications')

    def __repr__(self):
        return f'UserVerification(id={self.id!r}, user_id={self.user_id!r}, url_key={self.url_key!r}, status={self.status!r}, created={self.created!r}, updated={self.updated!r})'



class Skill(ModelBase):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    title = Column(String(255, collation='utf8_bin'), nullable=False, index=True, unique=True)
    description = Column(String(600, collation='utf8_bin'), nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    revisions = relationship('SkillRevision', back_populates='skill')

    def __repr__(self):
        return f'Skill(id={self.id!r}, title={self.title!r}, description={self.description!r}, created={self.created!r}, updated={self.updated!r})'


class SkillRevision(ModelBase):
    __tablename__ = 'skill_revisions'

    id = Column(Integer, primary_key=True)
    skill_id = Column(ForeignKey('skills.id'), nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    text = Column(Text(collation='utf8_bin'), nullable=False)
    is_current_revision = Column(Boolean, nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    skill = relationship('Skill', back_populates='revisions')
    contributor = relationship('User', back_populates='skill_revisions')

    def __repr__(self):
        return f'SkillRevision(id={self.id!r}, text={self.text!r}, is_current_revision={self.is_current_revision!r}, created={self.created!r}, updated={self.updated!r})'


skill_relations = Table('skill_relations', ModelBase.metadata,
    Column('origin_skill', ForeignKey('skills.id')),
    Column('relation_type', String(255), nullable=False),
    Column('destination_skill', ForeignKey('skills.id')),
    Column('created', DateTime, nullable=False, default=datetime.now),
    Column('creator', ForeignKey('users.id'))
)
