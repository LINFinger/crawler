import json
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker

from model.sql import RecentArrival


def store_in_mysql(index, s):
    engine = create_engine('mysql+pymysql://root:mysqlpsw@localhost:3306/aa')
    DBSession = sessionmaker(bind=engine)
    messages = json.loads(s)
    session = DBSession()
    if index == 0:
        for item in messages:
            new_ra = RecentArrival(item)
            if session.query(RecentArrival).filter(RecentArrival.timestamp == new_ra.timestamp).first() is None:
                session.add(new_ra)
    session.commit()
    session.close()
