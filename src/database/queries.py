"""
SELECT QUERIES
"""
from src import db
from src.database import models

films = db.session.query(models.Film).order_by(models.Film.rating).all()

harry_potter_and_ch_s = db.session.query(models.Film).filter(models.Film.title == "Harry_Potter").first()

sp = db.session.query(models.Film).filter_by(title="Spider-man").first()

and_statement_hp = db.session.query(models.Film).filter(models.Film.title != "Harry_Potter",
                                                        models.Film.rating >= 7.5).first()

spider_man = db.session.query(models.Film).filter(models.Film.title.like('%man%')).all()

"""
QUERYING WITH JOINS
"""

films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()
print(films_with_actors)
