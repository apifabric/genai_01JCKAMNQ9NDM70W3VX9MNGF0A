# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Sport(Base):
    __tablename__ = 'sports'
    
    """description: Table to store different sports"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    equipment_needed = Column(String)
    team_based = Column(Boolean, default=False)



class Athlete(Base):
    __tablename__ = 'athletes'
    
    """description: Table for storing athlete information"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date)
    nationality = Column(String)



class Team(Base):
    __tablename__ = 'teams'
    
    """description: Table for storing team details"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    sport_id = Column(Integer, ForeignKey('sports.id'))
    founding_date = Column(Date)



class Match(Base):
    __tablename__ = 'matches'

    """description: Table for storing match information"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    location = Column(String)
    sport_id = Column(Integer, ForeignKey('sports.id'))



class Performance(Base):
    __tablename__ = 'performances'

    """description: Table for storing athlete performance in different matches"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    athlete_id = Column(Integer, ForeignKey('athletes.id'))
    match_id = Column(Integer, ForeignKey('matches.id'))
    score = Column(Integer)
    assists = Column(Integer)
    penalties = Column(Integer)
    performance_date = Column(Date)



class League(Base):
    __tablename__ = 'leagues'

    """description: Table to store league details"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    establishment_year = Column(Integer)



class Registration(Base):
    __tablename__ = 'registrations'

    """description: Table for athletes' registrations in different leagues"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    athlete_id = Column(Integer, ForeignKey('athletes.id'))
    league_id = Column(Integer, ForeignKey('leagues.id'))
    registration_date = Column(Date, nullable=False)



class Sponsor(Base):
    __tablename__ = 'sponsors'

    """description: Table for storing sponsor information"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    budget = Column(Integer)



class Sponsorship(Base):
    __tablename__ = 'sponsorships'

    """description: Table for storing details about sponsorships for different teams"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    sponsor_id = Column(Integer, ForeignKey('sponsors.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    amount = Column(Integer)



class Player(Base):
    __tablename__ = 'players'

    """description: Table for linking athletes to the teams they play for"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    athlete_id = Column(Integer, ForeignKey('athletes.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))
    join_date = Column(Date)



class Coach(Base):
    __tablename__ = 'coaches'

    """description: Table for storing information about team coaches"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date)
    team_id = Column(Integer, ForeignKey('teams.id'))



class Event(Base):
    __tablename__ = 'events'

    """description: Table for storing information about special sporting events"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String)
    sport_id = Column(Integer, ForeignKey('sports.id'))



# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

# Create test data for each table separately

# Sport Test Data
sport1 = Sport(name="Football", equipment_needed="Ball, Goalposts", team_based=True)
sport2 = Sport(name="Basketball", equipment_needed="Ball, Basket", team_based=True)
sport3 = Sport(name="Tennis", equipment_needed="Racket, Ball", team_based=False)
sport4 = Sport(name="Swimming", equipment_needed="Goggles, Swimsuit", team_based=False)

# Athlete Test Data
athlete1 = Athlete(first_name="John", last_name="Doe", date_of_birth=date(1990, 7, 14), nationality="USA")
athlete2 = Athlete(first_name="Lucy", last_name="Smith", date_of_birth=date(1992, 1, 19), nationality="UK")
athlete3 = Athlete(first_name="Marco", last_name="Polo", date_of_birth=date(1988, 5, 23), nationality="Italy")
athlete4 = Athlete(first_name="Juan", last_name="Carlos", date_of_birth=date(1985, 11, 30), nationality="Spain")

# Team Test Data
team1 = Team(name="Eagles", sport_id=1, founding_date=date(1980, 2, 5))
team2 = Team(name="Hawks", sport_id=2, founding_date=date(1990, 6, 15))
team3 = Team(name="Wolves", sport_id=3, founding_date=date(1995, 9, 10))
team4 = Team(name="Sharks", sport_id=4, founding_date=date(2000, 3, 20))

# Match Test Data
match1 = Match(date=date(2023, 8, 12), location="Stadium A", sport_id=1)
match2 = Match(date=date(2023, 9, 18), location="Arena B", sport_id=2)
match3 = Match(date=date(2023, 10, 24), location="Court C", sport_id=3)
match4 = Match(date=date(2023, 11, 30), location="Pool D", sport_id=4)

# Performance Test Data
performance1 = Performance(athlete_id=1, match_id=1, score=10, assists=2, penalties=0, performance_date=date(2023, 8, 12))
performance2 = Performance(athlete_id=2, match_id=2, score=15, assists=3, penalties=1, performance_date=date(2023, 9, 18))
performance3 = Performance(athlete_id=3, match_id=3, score=0, assists=5, penalties=2, performance_date=date(2023, 10, 24))
performance4 = Performance(athlete_id=4, match_id=4, score=20, assists=1, penalties=0, performance_date=date(2023, 11, 30))

# League Test Data
league1 = League(name="Champions League", description="Annual international competition", establishment_year=1992)
league2 = League(name="World Cup", description="Global international tournament", establishment_year=1930)
league3 = League(name="National League", description="Country-based competition", establishment_year=1888)
league4 = League(name="Olympics", description="Worldwide quadrennial event", establishment_year=1896)

# Registration Test Data
registration1 = Registration(athlete_id=1, league_id=1, registration_date=date(2023, 5, 1))
registration2 = Registration(athlete_id=2, league_id=2, registration_date=date(2023, 5, 2))
registration3 = Registration(athlete_id=3, league_id=3, registration_date=date(2023, 5, 3))
registration4 = Registration(athlete_id=4, league_id=4, registration_date=date(2023, 5, 4))

# Sponsor Test Data
sponsor1 = Sponsor(name="Nike", contact_info="nike@company.com", budget=1000000)
sponsor2 = Sponsor(name="Adidas", contact_info="adidas@company.com", budget=1200000)
sponsor3 = Sponsor(name="Puma", contact_info="puma@company.com", budget=900000)
sponsor4 = Sponsor(name="Reebok", contact_info="reebok@company.com", budget=800000)

# Sponsorship Test Data
sponsorship1 = Sponsorship(sponsor_id=1, team_id=1, start_date=date(2023, 1, 1), end_date=date(2023, 12, 31), amount=500000)
sponsorship2 = Sponsorship(sponsor_id=2, team_id=2, start_date=date(2023, 1, 1), end_date=date(2023, 12, 31), amount=600000)
sponsorship3 = Sponsorship(sponsor_id=3, team_id=3, start_date=date(2023, 1, 1), end_date=date(2023, 12, 31), amount=700000)
sponsorship4 = Sponsorship(sponsor_id=4, team_id=4, start_date=date(2023, 1, 1), end_date=date(2023, 12, 31), amount=800000)

# Player Test Data
player1 = Player(athlete_id=1, team_id=1, join_date=date(2023, 4, 1))
player2 = Player(athlete_id=2, team_id=2, join_date=date(2023, 4, 2))
player3 = Player(athlete_id=3, team_id=3, join_date=date(2023, 4, 3))
player4 = Player(athlete_id=4, team_id=4, join_date=date(2023, 4, 4))

# Coach Test Data
coach1 = Coach(first_name="Alex", last_name="Ferguson", birth_date=date(1975, 3, 12), team_id=1)
coach2 = Coach(first_name="Bill", last_name="Jackson", birth_date=date(1960, 1, 17), team_id=2)
coach3 = Coach(first_name="Pep", last_name="Guardiola", birth_date=date(1971, 2, 24), team_id=3)
coach4 = Coach(first_name="Jose", last_name="Mourinho", birth_date=date(1963, 7, 26), team_id=4)

# Event Test Data
event1 = Event(name="Football World Final", date=date(2023, 12, 25), location="Stadium X", sport_id=1)
event2 = Event(name="Basketball World Series", date=date(2023, 11, 15), location="Arena Y", sport_id=2)
event3 = Event(name="Tennis Grand Slam", date=date(2023, 12, 5), location="Court Z", sport_id=3)
event4 = Event(name="Swimming Championship", date=date(2023, 10, 20), location="Pool A", sport_id=4)


session.add_all([sport1, sport2, sport3, sport4, athlete1, athlete2, athlete3, athlete4, team1, team2, team3, team4, match1, match2, match3, match4, performance1, performance2, performance3, performance4, league1, league2, league3, league4, registration1, registration2, registration3, registration4, sponsor1, sponsor2, sponsor3, sponsor4, sponsorship1, sponsorship2, sponsorship3, sponsorship4, player1, player2, player3, player4, coach1, coach2, coach3, coach4, event1, event2, event3, event4])
session.commit()
