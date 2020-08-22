from sqlalchemy import  Column
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import Sequence
from sqlalchemy import Float

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Machines(Base):
    __tablename__ = "Machines"
    WORKERS = Column(Integer)
    BATCH_SIZE = Column(Integer)
    LATENCY = Column(Integer)
    TIME1 = Column(Float)
    TIME2 = Column(Float)
    ACCURACY = Column(Float, primary_key=True)






    def __repr__(self):
        return "<streetLevelCrimes(WORKERS='%i',BATCH_SIZE='%i',LATENCY='%i',TIME1='%d',TIME2='%d',ACCURACY='%d')>" % (
                                self.WORKERS, self.BATCH_SIZE, self.LATENCY, self.TIME1, self.TIME2, self.ACCURACY)
