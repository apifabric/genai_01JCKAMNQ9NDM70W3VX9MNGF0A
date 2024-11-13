# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 13, 2024 17:56:26
# Database: sqlite:////tmp/tmp.oIYhsATcwK-01JCKAMNQ9NDM70W3VX9MNGF0A/SportStatisticsTracker/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Athlete(SAFRSBaseX, Base):
    __tablename__ = 'athletes'
    _s_collection_name = 'Athlete'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date)
    nationality = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    RegistrationList : Mapped[List["Registration"]] = relationship(back_populates="athlete")
    PerformanceList : Mapped[List["Performance"]] = relationship(back_populates="athlete")
    PlayerList : Mapped[List["Player"]] = relationship(back_populates="athlete")



class League(SAFRSBaseX, Base):
    __tablename__ = 'leagues'
    _s_collection_name = 'League'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    establishment_year = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    RegistrationList : Mapped[List["Registration"]] = relationship(back_populates="league")



class Sponsor(SAFRSBaseX, Base):
    __tablename__ = 'sponsors'
    _s_collection_name = 'Sponsor'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    budget = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    SponsorshipList : Mapped[List["Sponsorship"]] = relationship(back_populates="sponsor")



class Sport(SAFRSBaseX, Base):
    __tablename__ = 'sports'
    _s_collection_name = 'Sport'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    equipment_needed = Column(String)
    team_based = Column(Boolean)

    # parent relationships (access parent)

    # child relationships (access children)
    EventList : Mapped[List["Event"]] = relationship(back_populates="sport")
    MatchList : Mapped[List["Match"]] = relationship(back_populates="sport")
    TeamList : Mapped[List["Team"]] = relationship(back_populates="sport")



class Event(SAFRSBaseX, Base):
    __tablename__ = 'events'
    _s_collection_name = 'Event'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String)
    sport_id = Column(ForeignKey('sports.id'))

    # parent relationships (access parent)
    sport : Mapped["Sport"] = relationship(back_populates=("EventList"))

    # child relationships (access children)



class Match(SAFRSBaseX, Base):
    __tablename__ = 'matches'
    _s_collection_name = 'Match'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    location = Column(String)
    sport_id = Column(ForeignKey('sports.id'))

    # parent relationships (access parent)
    sport : Mapped["Sport"] = relationship(back_populates=("MatchList"))

    # child relationships (access children)
    PerformanceList : Mapped[List["Performance"]] = relationship(back_populates="match")



class Registration(SAFRSBaseX, Base):
    __tablename__ = 'registrations'
    _s_collection_name = 'Registration'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    athlete_id = Column(ForeignKey('athletes.id'))
    league_id = Column(ForeignKey('leagues.id'))
    registration_date = Column(Date, nullable=False)

    # parent relationships (access parent)
    athlete : Mapped["Athlete"] = relationship(back_populates=("RegistrationList"))
    league : Mapped["League"] = relationship(back_populates=("RegistrationList"))

    # child relationships (access children)



class Team(SAFRSBaseX, Base):
    __tablename__ = 'teams'
    _s_collection_name = 'Team'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    sport_id = Column(ForeignKey('sports.id'))
    founding_date = Column(Date)

    # parent relationships (access parent)
    sport : Mapped["Sport"] = relationship(back_populates=("TeamList"))

    # child relationships (access children)
    CoachList : Mapped[List["Coach"]] = relationship(back_populates="team")
    PlayerList : Mapped[List["Player"]] = relationship(back_populates="team")
    SponsorshipList : Mapped[List["Sponsorship"]] = relationship(back_populates="team")



class Coach(SAFRSBaseX, Base):
    __tablename__ = 'coaches'
    _s_collection_name = 'Coach'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date)
    team_id = Column(ForeignKey('teams.id'))

    # parent relationships (access parent)
    team : Mapped["Team"] = relationship(back_populates=("CoachList"))

    # child relationships (access children)



class Performance(SAFRSBaseX, Base):
    __tablename__ = 'performances'
    _s_collection_name = 'Performance'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    athlete_id = Column(ForeignKey('athletes.id'))
    match_id = Column(ForeignKey('matches.id'))
    score = Column(Integer)
    assists = Column(Integer)
    penalties = Column(Integer)
    performance_date = Column(Date)

    # parent relationships (access parent)
    athlete : Mapped["Athlete"] = relationship(back_populates=("PerformanceList"))
    match : Mapped["Match"] = relationship(back_populates=("PerformanceList"))

    # child relationships (access children)



class Player(SAFRSBaseX, Base):
    __tablename__ = 'players'
    _s_collection_name = 'Player'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    athlete_id = Column(ForeignKey('athletes.id'))
    team_id = Column(ForeignKey('teams.id'))
    join_date = Column(Date)

    # parent relationships (access parent)
    athlete : Mapped["Athlete"] = relationship(back_populates=("PlayerList"))
    team : Mapped["Team"] = relationship(back_populates=("PlayerList"))

    # child relationships (access children)



class Sponsorship(SAFRSBaseX, Base):
    __tablename__ = 'sponsorships'
    _s_collection_name = 'Sponsorship'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    sponsor_id = Column(ForeignKey('sponsors.id'))
    team_id = Column(ForeignKey('teams.id'))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    amount = Column(Integer)

    # parent relationships (access parent)
    sponsor : Mapped["Sponsor"] = relationship(back_populates=("SponsorshipList"))
    team : Mapped["Team"] = relationship(back_populates=("SponsorshipList"))

    # child relationships (access children)
