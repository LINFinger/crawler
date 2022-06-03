from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()


class RecentArrival(Base):
    __tablename__ = 'recent_arrivals'

    timestamp = Column(Integer, primary_key=True)
    unspecified = Column(Integer)
    containerShips = Column(Integer)
    dryBreakbulk = Column(Integer)
    dryBulk = Column(Integer)
    fishing = Column(Integer)
    lngCarriers = Column(Integer)
    lpgCarriers = Column(Integer)
    offshoreRigs = Column(Integer)
    otherMarkets = Column(Integer)
    passengerShips = Column(Integer)
    pleasureCraft = Column(Integer)
    roRo = Column(Integer)
    supportingVessels = Column(Integer)
    wetBulk = Column(Integer)

    def __init__(self, d):
        self.timestamp = d['timestamp']
        arrivals = d['arrivals']
        for arrival in arrivals:
            if arrival['type'] == 'containerShips':
                self.containerShips = arrival['numberOfArrivals']
            elif arrival['type'] == 'dryBreakbulk':
                self.dryBreakbulk = arrival['numberOfArrivals']
            elif arrival['type'] == 'dryBulk':
                self.dryBulk = arrival['numberOfArrivals']
            elif arrival['type'] == 'fishing':
                self.fishing = arrival['numberOfArrivals']
            elif arrival['type'] == 'lngCarriers':
                self.lngCarriers = arrival['numberOfArrivals']
            elif arrival['type'] == 'lpgCarriers':
                self.lpgCarriers = arrival['numberOfArrivals']
            elif arrival['type'] == 'offshoreRigs':
                self.offshoreRigs = arrival['numberOfArrivals']
            elif arrival['type'] == 'otherMarkets':
                self.otherMarkets = arrival['numberOfArrivals']
            elif arrival['type'] == 'passengerShips':
                self.passengerShips = arrival['numberOfArrivals']
            elif arrival['type'] == 'pleasureCraft':
                self.pleasureCraft = arrival['numberOfArrivals']
            elif arrival['type'] == 'roRo':
                self.roRo = arrival['numberOfArrivals']
            elif arrival['type'] == 'supportingVessels':
                self.supportingVessels = arrival['numberOfArrivals']
            elif arrival['type'] == 'wetBulk':
                self.wetBulk = arrival['numberOfArrivals']
            else:
                self.unspecified = arrival['numberOfArrivals']


if __name__ == "__main__":
    engine = create_engine('mysql+pymysql://root:mysqlpsw@localhost:3306/aa')
    DBSession = sessionmaker(bind=engine)
    d = json.loads(
        '[{"timestamp":1653004800,"arrivals":[{"numberOfArrivals":0,"type":"unspecified"},{"numberOfArrivals":43,"type":"containerShips"},{"numberOfArrivals":1042,"type":"dryBreakbulk"},{"numberOfArrivals":23,"type":"dryBulk"},{"numberOfArrivals":5,"type":"fishing"},{"numberOfArrivals":0,"type":"lngCarriers"},{"numberOfArrivals":8,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":195,"type":"otherMarkets"},{"numberOfArrivals":9,"type":"passengerShips"},{"numberOfArrivals":4,"type":"pleasureCraft"},{"numberOfArrivals":3,"type":"roRo"},{"numberOfArrivals":35,"type":"supportingVessels"},{"numberOfArrivals":104,"type":"wetBulk"}]},{"timestamp":1653091200,"arrivals":[{"numberOfArrivals":0,"type":"unspecified"},{"numberOfArrivals":39,"type":"containerShips"},{"numberOfArrivals":1086,"type":"dryBreakbulk"},{"numberOfArrivals":13,"type":"dryBulk"},{"numberOfArrivals":4,"type":"fishing"},{"numberOfArrivals":1,"type":"lngCarriers"},{"numberOfArrivals":5,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":173,"type":"otherMarkets"},{"numberOfArrivals":9,"type":"passengerShips"},{"numberOfArrivals":5,"type":"pleasureCraft"},{"numberOfArrivals":1,"type":"roRo"},{"numberOfArrivals":47,"type":"supportingVessels"},{"numberOfArrivals":91,"type":"wetBulk"}]},{"timestamp":1653177600,"arrivals":[{"numberOfArrivals":1,"type":"unspecified"},{"numberOfArrivals":52,"type":"containerShips"},{"numberOfArrivals":1076,"type":"dryBreakbulk"},{"numberOfArrivals":24,"type":"dryBulk"},{"numberOfArrivals":10,"type":"fishing"},{"numberOfArrivals":0,"type":"lngCarriers"},{"numberOfArrivals":4,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":219,"type":"otherMarkets"},{"numberOfArrivals":10,"type":"passengerShips"},{"numberOfArrivals":2,"type":"pleasureCraft"},{"numberOfArrivals":4,"type":"roRo"},{"numberOfArrivals":38,"type":"supportingVessels"},{"numberOfArrivals":83,"type":"wetBulk"}]},{"timestamp":1653264000,"arrivals":[{"numberOfArrivals":0,"type":"unspecified"},{"numberOfArrivals":41,"type":"containerShips"},{"numberOfArrivals":892,"type":"dryBreakbulk"},{"numberOfArrivals":9,"type":"dryBulk"},{"numberOfArrivals":11,"type":"fishing"},{"numberOfArrivals":0,"type":"lngCarriers"},{"numberOfArrivals":6,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":196,"type":"otherMarkets"},{"numberOfArrivals":9,"type":"passengerShips"},{"numberOfArrivals":3,"type":"pleasureCraft"},{"numberOfArrivals":2,"type":"roRo"},{"numberOfArrivals":35,"type":"supportingVessels"},{"numberOfArrivals":85,"type":"wetBulk"}]},{"timestamp":1653350400,"arrivals":[{"numberOfArrivals":1,"type":"unspecified"},{"numberOfArrivals":36,"type":"containerShips"},{"numberOfArrivals":1055,"type":"dryBreakbulk"},{"numberOfArrivals":12,"type":"dryBulk"},{"numberOfArrivals":14,"type":"fishing"},{"numberOfArrivals":0,"type":"lngCarriers"},{"numberOfArrivals":4,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":160,"type":"otherMarkets"},{"numberOfArrivals":8,"type":"passengerShips"},{"numberOfArrivals":4,"type":"pleasureCraft"},{"numberOfArrivals":5,"type":"roRo"},{"numberOfArrivals":31,"type":"supportingVessels"},{"numberOfArrivals":112,"type":"wetBulk"}]},{"timestamp":1653436800,"arrivals":[{"numberOfArrivals":0,"type":"unspecified"},{"numberOfArrivals":38,"type":"containerShips"},{"numberOfArrivals":1094,"type":"dryBreakbulk"},{"numberOfArrivals":15,"type":"dryBulk"},{"numberOfArrivals":7,"type":"fishing"},{"numberOfArrivals":0,"type":"lngCarriers"},{"numberOfArrivals":2,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":219,"type":"otherMarkets"},{"numberOfArrivals":9,"type":"passengerShips"},{"numberOfArrivals":3,"type":"pleasureCraft"},{"numberOfArrivals":1,"type":"roRo"},{"numberOfArrivals":38,"type":"supportingVessels"},{"numberOfArrivals":96,"type":"wetBulk"}]},{"timestamp":1653523200,"arrivals":[{"numberOfArrivals":1,"type":"unspecified"},{"numberOfArrivals":37,"type":"containerShips"},{"numberOfArrivals":1084,"type":"dryBreakbulk"},{"numberOfArrivals":13,"type":"dryBulk"},{"numberOfArrivals":6,"type":"fishing"},{"numberOfArrivals":1,"type":"lngCarriers"},{"numberOfArrivals":2,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":223,"type":"otherMarkets"},{"numberOfArrivals":11,"type":"passengerShips"},{"numberOfArrivals":4,"type":"pleasureCraft"},{"numberOfArrivals":4,"type":"roRo"},{"numberOfArrivals":36,"type":"supportingVessels"},{"numberOfArrivals":94,"type":"wetBulk"}]},{"timestamp":1653609600,"arrivals":[{"numberOfArrivals":0,"type":"unspecified"},{"numberOfArrivals":38,"type":"containerShips"},{"numberOfArrivals":1245,"type":"dryBreakbulk"},{"numberOfArrivals":15,"type":"dryBulk"},{"numberOfArrivals":12,"type":"fishing"},{"numberOfArrivals":0,"type":"lngCarriers"},{"numberOfArrivals":2,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":217,"type":"otherMarkets"},{"numberOfArrivals":17,"type":"passengerShips"},{"numberOfArrivals":3,"type":"pleasureCraft"},{"numberOfArrivals":6,"type":"roRo"},{"numberOfArrivals":35,"type":"supportingVessels"},{"numberOfArrivals":90,"type":"wetBulk"}]},{"timestamp":1653696000,"arrivals":[{"numberOfArrivals":0,"type":"unspecified"},{"numberOfArrivals":40,"type":"containerShips"},{"numberOfArrivals":1106,"type":"dryBreakbulk"},{"numberOfArrivals":14,"type":"dryBulk"},{"numberOfArrivals":8,"type":"fishing"},{"numberOfArrivals":0,"type":"lngCarriers"},{"numberOfArrivals":2,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":200,"type":"otherMarkets"},{"numberOfArrivals":7,"type":"passengerShips"},{"numberOfArrivals":2,"type":"pleasureCraft"},{"numberOfArrivals":2,"type":"roRo"},{"numberOfArrivals":42,"type":"supportingVessels"},{"numberOfArrivals":100,"type":"wetBulk"}]},{"timestamp":1653782400,"arrivals":[{"numberOfArrivals":0,"type":"unspecified"},{"numberOfArrivals":52,"type":"containerShips"},{"numberOfArrivals":961,"type":"dryBreakbulk"},{"numberOfArrivals":16,"type":"dryBulk"},{"numberOfArrivals":5,"type":"fishing"},{"numberOfArrivals":0,"type":"lngCarriers"},{"numberOfArrivals":4,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":214,"type":"otherMarkets"},{"numberOfArrivals":9,"type":"passengerShips"},{"numberOfArrivals":3,"type":"pleasureCraft"},{"numberOfArrivals":4,"type":"roRo"},{"numberOfArrivals":35,"type":"supportingVessels"},{"numberOfArrivals":105,"type":"wetBulk"}]},{"timestamp":1653868800,"arrivals":[{"numberOfArrivals":1,"type":"unspecified"},{"numberOfArrivals":35,"type":"containerShips"},{"numberOfArrivals":968,"type":"dryBreakbulk"},{"numberOfArrivals":7,"type":"dryBulk"},{"numberOfArrivals":12,"type":"fishing"},{"numberOfArrivals":0,"type":"lngCarriers"},{"numberOfArrivals":3,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":211,"type":"otherMarkets"},{"numberOfArrivals":10,"type":"passengerShips"},{"numberOfArrivals":4,"type":"pleasureCraft"},{"numberOfArrivals":3,"type":"roRo"},{"numberOfArrivals":23,"type":"supportingVessels"},{"numberOfArrivals":96,"type":"wetBulk"}]},{"timestamp":1653955200,"arrivals":[{"numberOfArrivals":0,"type":"unspecified"},{"numberOfArrivals":51,"type":"containerShips"},{"numberOfArrivals":965,"type":"dryBreakbulk"},{"numberOfArrivals":15,"type":"dryBulk"},{"numberOfArrivals":7,"type":"fishing"},{"numberOfArrivals":0,"type":"lngCarriers"},{"numberOfArrivals":0,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":228,"type":"otherMarkets"},{"numberOfArrivals":15,"type":"passengerShips"},{"numberOfArrivals":5,"type":"pleasureCraft"},{"numberOfArrivals":4,"type":"roRo"},{"numberOfArrivals":38,"type":"supportingVessels"},{"numberOfArrivals":92,"type":"wetBulk"}]},{"timestamp":1654041600,"arrivals":[{"numberOfArrivals":3,"type":"unspecified"},{"numberOfArrivals":43,"type":"containerShips"},{"numberOfArrivals":923,"type":"dryBreakbulk"},{"numberOfArrivals":21,"type":"dryBulk"},{"numberOfArrivals":16,"type":"fishing"},{"numberOfArrivals":0,"type":"lngCarriers"},{"numberOfArrivals":4,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":212,"type":"otherMarkets"},{"numberOfArrivals":36,"type":"passengerShips"},{"numberOfArrivals":0,"type":"pleasureCraft"},{"numberOfArrivals":3,"type":"roRo"},{"numberOfArrivals":36,"type":"supportingVessels"},{"numberOfArrivals":79,"type":"wetBulk"}]},{"timestamp":1654128000,"arrivals":[{"numberOfArrivals":5,"type":"unspecified"},{"numberOfArrivals":39,"type":"containerShips"},{"numberOfArrivals":868,"type":"dryBreakbulk"},{"numberOfArrivals":23,"type":"dryBulk"},{"numberOfArrivals":9,"type":"fishing"},{"numberOfArrivals":0,"type":"lngCarriers"},{"numberOfArrivals":2,"type":"lpgCarriers"},{"numberOfArrivals":0,"type":"offshoreRigs"},{"numberOfArrivals":210,"type":"otherMarkets"},{"numberOfArrivals":34,"type":"passengerShips"},{"numberOfArrivals":1,"type":"pleasureCraft"},{"numberOfArrivals":2,"type":"roRo"},{"numberOfArrivals":30,"type":"supportingVessels"},{"numberOfArrivals":82,"type":"wetBulk"}]}]')
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = RecentArrival(d[0])
    # 添加到session:
    if session.query(RecentArrival).filter(RecentArrival.timestamp == new_user.timestamp).first() is None:
        session.add(new_user)
    else:
        print(1)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()
