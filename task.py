import json
import requests
import machines
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db/mydb2.db",connect_args={'check_same_thread':False})
session = sessionmaker(bind=engine)()


def getCrimesCategories(BATCH_SIZE2,LATENCY2):
    print(BATCH_SIZE2, LATENCY2)
    result = session.query(machines.Machines).filter_by(BATCH_SIZE=BATCH_SIZE2,LATENCY=LATENCY2)
    var = 0
    timelim = 1000
    for i in result:
        if i.TIME2 < timelim:
            timelim = i.TIME2
            var =i.WORKERS

    return var


def dropdown():
    result1 = session.query(machines.Machines.BATCH_SIZE).distinct().all()
    result2 = session.query(machines.Machines.LATENCY).distinct().all()
    array1=[]
    array2=[]

    for i in result1:
        array1.append(i.BATCH_SIZE)
    for i in result2:
        array2.append(i.LATENCY)
    return {"BATCH_SIZE":array1,"LATENCY":array2}



    # return a





#def getCrimesOutcome(id):
#    result = session.query(crimeClasses.outcomesCrimes).filter_by(persistent_id=id).all()
#    return result
