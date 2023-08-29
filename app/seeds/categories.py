from app.models import db, Category, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    rpg = Category(
        name='RPG', description='Role-Playing Game')
    strategy = Category(
        name='Strategy', description='Strategy')
    simulation = Category(
        name='Simulation', description='Simulation')
    action = Category(
        name='Action', description='Action')
    adventure = Category(
        name='Adventure', description='Adventure')
    indie = Category(
        name='Indie', description='Indie')
    sports = Category(
        name='Sports', description='Sports')
    puzzle = Category(
        name='Puzzle', description='Puzzle')

    db.session.add(rpg)
    db.session.add(strategy)
    db.session.add(simulation)
    db.session.add(action)
    db.session.add(adventure)
    db.session.add(indie)
    db.session.add(sports)
    db.session.add(puzzle)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(f"TRUNCATE table categories RESTART IDENTITY CASCADE;")

    db.session.commit()
