from datetime import date

from src import db
from src.database import models


def populate_films():
    harry_potter = models.Film(
        title="Harry_Potter",
        release_date=date(2001, 1, 1),
        description="blabla",
        distributed_by="WB Pictures",
        length=112,
        rating=8,
    )
    spider_man = models.Film(
        title="Spider-man",
        release_date=date(2001, 1, 1),
        description="qweqweqwe",
        distributed_by="Sony",
        length=123,
        rating=9,
    )

    daniel_radcliffe = models.Actor(name='Daniel Radcliffe', birthday=date(1989, 1, 1), is_active=True)

    harry_potter.actors = [daniel_radcliffe]

    db.session.add(harry_potter)
    db.session.add(spider_man)

    db.session.add(daniel_radcliffe)

    db.session.commit()
    db.session.close()


if __name__ == "__main__":
    populate_films()
    print('Successfully populated')
