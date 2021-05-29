
import sqlite3
conn=sqlite3.connect('Trip.db')
cur=conn.cursor()


#get the names of all cities in the database
def get_city_list():
    s="SELECT * FROM CITY"
    cur.execute(s)
    city_list = []
    for i in cur.fetchall():
        city_list.append(str(i[0]))
    return city_list


#for all the selected category get the place information
def get_places_type(category):
    result = []
    s = "SELECT P.PLACE_NAME ,P.PLACE_TYPE ,L.LOCALITY_NAME ,P.RATING ,C.CITY_NAME " \
        "FROM PLACESTOVISIT P,CITY C,LOCALITY L " \
        "WHERE P.LOCALITY_ID=L.LOCALITY_ID AND C.CITY_NAME=L.CITY_NAME " \
        "AND P.PLACE_TYPE IN "+str(tuple(category))
    cur.execute(s)
    for i in cur.fetchall():
        result.append(i)
    return result



#for a place get entire information about that place
def get_place_info(place_name):
    try:
        q="SELECT P.PLACE_NAME,P.PLACE_TYPE,P.DESCRIPTION_OF_THE_PLACE,P.STREET_ADDRESS,P.RATING,P.AVG_COST " \
          "FROM PLACESTOVISIT P " \
          "WHERE P.PLACE_NAME='{}'".format(str(place_name))
        cur.execute(q)
        return cur.fetchall()
    except Exception as e:
        print(e)




#for city parameter, get all place available under this city
def get_places_city(city):
    q ="SELECT P.PLACE_NAME ,P.PLACE_TYPE ,L.LOCALITY_NAME ,P.RATING ,C.CITY_NAME " \
       "FROM PLACESTOVISIT P,CITY C,LOCALITY L " \
       "WHERE P.LOCALITY_ID=L.LOCALITY_ID AND C.CITY_NAME=L.CITY_NAME " \
       "AND C.CITY_NAME='{}'".format(str(city))
    cur.execute(q)
    result=[]
    for i in cur.fetchall():
        result.append(i)
    return result




#get all image address for the selected place
def get_place_images(place_name):
    q="""SELECT IMG_ADDRESS FROM PLACE_IMAGES WHERE PLACE_NAME='{}'""".format(place_name)
    cur.execute(q)
    res=cur.fetchall()
    if len(res)==0:
        return []
    j=1
    for i in res:
        with open(r'.\ImageFile\place_image{}.jpg'.format(j),'wb')as f:
            f.write(i[0].read())
        j=j+1
    img_address=[]
    for i in range(1,5):
        img_address.append(r'.\ImageFile\place_image{}.jpg'.format(i))
    return img_address



#call the Stored Procedure passing src and dest to get train info
def get_Train_info(source,destionation):
    s="""SELECT T.TRAIN_NAME,TR.CLASS,TR.FARE,TJH.JOURNEY_HOURS,TR.DEPARTURE_DATE,TDT.DEPARTURE_TIME,TR.NO_OF_SEATS,TR.TRAIN_STATUS
    FROM TRAIN T,TRAINRESERVATION TR,TRAINDEPARTURETIME TDT,TRAINJOURNEYHOURS TJH
    WHERE TR.SOURCE_CITY='{}'
    AND TDT.SOURCE_CITY='{}'
    AND TJH.SOURCE_CITY='{}'
    AND TJH.DESTINATION='{}'
    AND TR.DESTINATION='{}'
    AND T.TRAIN_ID=TR.TRAIN_ID
    AND TR.TRAIN_ID=TDT.TRAIN_ID
    AND TDT.TRAIN_ID=TJH.TRAIN_ID
    ORDER BY TR.DEPARTURE_DATE""".format(str(source),str(source),str(source),str(destionation),str(destionation))
    result=[]
    try:
        cur.execute(s)
        for i in cur.fetchall():
            result.append(i)
    except:
        return result
    return result




#method to get plane info between src and dest
def get_Plane_info(source,destionation):
    s="""SELECT P.PLANE_NAME,PR.CLASS,PR.FARE,PJH.JOURNEY_HOURS,PR.DEPARTURE_DATE,PDT.DEPARTURE_TIME,PR.NO_OF_SEATS
    FROM PLANE P,PLANERESERVATION PR,PLANEDEPARTURETIME PDT,PLANEJOURNEYHOURS PJH
    WHERE PR.SOURCE_CITY='{}'
    AND PDT.SOURCE_CITY='{}'
    AND PJH.SOURCE_CITY='{}'
    AND PJH.DESTINATION='{}'
    AND PR.DESTINATION='{}'
    AND P.PLANE_ID=PR.PLANE_ID
    AND PR.PLANE_ID=PDT.PLANE_ID
    AND PDT.PLANE_ID=PJH.PLANE_ID
    ORDER BY PR.DEPARTURE_DATE""".format(str(source),str(source),str(source),str(destionation),str(destionation))
    result=[]
    try:
        cur.execute(s)
        for i in cur.fetchall():
            result.append(i)
    except:
        return result
    return result


#method to get bus info between src and dest
def get_Bus_info(source,destionation):
    s="""SELECT B.BUS_SERVICE_PROVIDER,B.RATING,BR.COST,BR.SEAT_TYPE,B.IS_AC,BR.DEPARTURE_DATE,BDT.TIME_OF_DEPARTURE,BJH.JOURNEY_HOURS,BR.TOTAL_AVAILABLE_SEATS
    FROM BUS B,BUSRESERVATION BR,BUSJOURNEYHOURS BJH,BUSDEPARTURETIME BDT
    WHERE BR.SOURCE_CITY='{}'
    AND BDT.SOURCE_CITY='{}'
    AND BJH.SOURCE_CITY='{}'
    AND BJH.DESTINATION='{}'
    AND BR.DESTINATION='{}'
    AND B.BUS_ID=BR.BUS_ID
    AND BR.BUS_ID=BDT.BUS_ID
    AND BDT.BUS_ID=BJH.BUS_ID
    ORDER BY BR.DEPARTURE_DATE""".format(str(source),str(source),str(source),str(destionation),str(destionation))
    result=[]
    try:
        cur.execute(s)
        for i in cur.fetchall():
            result.append(i)
    except:
        return result
    return result




#get locality id for the given placeName
def getLocality(placeName):
    q="""SELECT LOCALITY_ID FROM PLACESTOVISIT WHERE PLACE_NAME='{}'""".format(str(placeName))
    try:
        cur.execute(q)
        return cur.fetchall()[0]
    except:
        return []


#get all the hotels in the given locality_id
def getHotels(locality):
    q="SELECT HOTEL_NAME,TOTAL_AVAILABLE_ROOMS,RATING,IS_ROOM_SERVICE,COST,CONTACT_NO," \
      "STREET_ADDRESS FROM HOTEL WHERE LOCALITY_ID={}".format(locality[0])
    result = []
    try:
        cur.execute(q)
        for i in cur.fetchall():
            result.append(i)
    except:
        return result
    return result







#Db query written to verify user
def verifyUser(username,password):
    q = """SELECT * FROM USER_PASS WHERE UNAME='{}' AND PASS='{}'""".format(str(username),str(password))
    try:
        cur.execute(q)
        return cur.fetchall()
    except:
        return []


#methods to delete a hotel/bus/train/plane from db with their pk

def deleteHotel(hotelName):
    q="""DELETE FROM HOTEL WHERE HOTEL_NAME='{}'""".format(str(hotelName))
    try:
        cur.execute(q)
    except:
        return -1
    cur.execute('commit')
    return 1

def deleteBus(busId):
    q="""DELETE FROM BUS WHERE BUS_ID='{}'""".format(str(busId))
    try:
        cur.execute(q)
    except:
        return -1
    cur.execute('commit')
    return 1

def deletePlane(planeId):
    q="""DELETE FROM PLANE WHERE PLANE_ID='{}'""".format(str(planeId))
    try:
        cur.execute(q)
    except:
        return -1
    cur.execute('commit')
    return 1

def deleteTrain(trainId):
    q="""DELETE FROM TRAIN WHERE TRAIN_ID='{}'""".format(str(trainId))
    try:
        cur.execute(q)
        cur.execute('commit')
    except:
        return -1
    return 1




#method to insert a new plane into database by passing all attributes


def insertPlane(planeId,planeName,source,destination,fare,numberOfSeats,journeyHours,departureDate,departureTime,plane_class):
    q1= "INSERT INTO PLANE VALUES"
    q2= "INSERT INTO PLANEDEPARTURETIME VALUES"
    q3= "INSERT INTO PLANEJOURNEYHOURS VALUES"
    q4= "INSERT INTO PLANERESERVATION VALUES"

    try:
        cur.execute(q1,(str(planeId),str(planeName)))
        cur.execute(q2,(str(planeId), str(source),str(departureTime)))
        cur.execute(q3,(str(planeId),str(source),str(destination),journeyHours))
        cur.execute(q4,(str(planeId),str(plane_class), str(source), str(destination),str(departureDate),fare,numberOfSeats))
        cur.execute('commit')
        return 1
    except:
        cur.execute('rollback')
        return -1



def insertBus(busId,source,destination,acRating,fare,numberOfSeats,journeyHours,busServiceProvider,departureDate,departureTime,rating,seat_type):

    q1 = """INSERT INTO BUS VALUES('{}','{}',{},{})""".format(str(busId), str(busServiceProvider), acRating, rating)
    q2 = """INSERT INTO BUSDEPARTURETIME VALUES('{}','{}','{}')""".format(str(busId), str(source), str(departureTime))
    q3 = "INSERT INTO BUSJOURNEYHOURS VALUES('{}','{}','{}',{})".format(str(busId), str(source), str(destination),
                                                                            journeyHours)
    q4 = """INSERT INTO BUSRESERVATION VALUES('{}','{}','{}','{}','{}',{},{})""".format(str(busId), str(source),
                                                                                        str(destination),
                                                                                        str(departureDate), str(seat_type),
                                                                                        fare, numberOfSeats)
    try:
        cur.execute(q1)
        cur.execute(q2)
        cur.execute(q3)
        cur.execute(q4)
    except Exception as e:
        print(e)
        cur.execute('rollback')
        return -1
    cur.execute('commit')
    return 1





def insertTrain(trainId,trainName,source,destination,fare,numberOfSeats,journeyHours,trainStatus,departureDate,departureTime,train_class):
    q1="""INSERT INTO TRAIN VALUES('{}','{}')""".format(str(trainId),str(trainName))
    q2= """INSERT INTO TRAINDEPARTURETIME VALUES('{}','{}','{}')""".format(str(trainId), str(source),
                                                                           str(departureTime))
    q3= """INSERT INTO TRAINRESERVATION VALUES('{}','{}','{}','{}','{}',{},'{}',{})""".format(str(trainId), str(train_class),
                                                                                              str(source),
                                                                                              str(destination),
                                                                                              str(departureDate), fare,
                                                                                              str(trainStatus),
                                                                                              numberOfSeats)
    q4= """INSERT INTO TRAINJOURNEYHOURS VALUES('{}','{}','{}',{})""".format(str(trainId), str(source),
                                                                             str(destination), journeyHours)

    try:
        cur.execute(q1)
        cur.execute(q2)
        cur.execute(q3)
        cur.execute(q4)
    except Exception as e:
        print(e)
        cur.execute('rollback')
        return -1
    cur.execute('commit')
    return 1



def insertHotel(hotelName,localityId,rating,streetAddress,isRoomService,contactNo,totalAvailableRooms,cost):
    q="INSERT INTO HOTEL VALUES"
    try:
        cur.execute(q,(str(hotelName),localityId,rating,str(streetAddress),isRoomService,str(contactNo),totalAvailableRooms,cost))
        cur.execute('commit')
        return 1
    except:
        cur.execute('rollback')
        return -1




def updateHotel(hotelName,localityId,rating,streetAddress,isRoomService,contactNo,totalAvailableRooms,cost):
    q = "UPDATE HOTEL SET HOTEL_NAME='{}',LOCALITY_ID={},RATING={},STREET_ADDRESS='{}',IS_ROOM_SERVICE={}," \
        "CONTACT_NO='{}',TOTAL_AVAILABLE_ROOMS={},COST={} WHERE HOTEL_NAME='{}'".format(str(hotelName),localityId,rating,str(streetAddress),isRoomService,str(contactNo),totalAvailableRooms,cost,str(hotelName))
    try:
        cur.execute(q)
        cur.execute('commit')
        return 1
    except:
        cur.execute('rollback')
        return -1




def updateBus(busId,busName,source,destination,acRating,fare,numberOfSeats,journeyHours,busServiceProvider,departureDate,departureTime,rating,seat_type):
    q1="UPDATE BUS SET BUS_ID='{}',BUS_SERVICE_PROVIDER='{}',IS_AC={},RATING={} " \
       "WHERE BUS_ID='{}'".format(str(busId),str(busServiceProvider),acRating,rating,str(busId))

    q2= "UPDATE BUSDEPARTURETIME SET BUS_ID='{}',SOURCE_CITY='{}',TIME_OF_DEPARTURE='{} " \
        "WHERE BUS_ID='{}''".format(str(busId),str(source),str(departureTime),str(busId))

    q3= "UPDATE BUSRESERVATION SET BUS_ID='{}',SOURCE_CITY='{}',DESTINATION='{}',DEPARTURE_DATE='{}',SEAT_TYPE='{}'," \
        "COST={},TOTAL_AVAILABLE_SEATS={} WHERE BUS_ID='{}'".format(str(busId), str(source), str(destination), str(departureDate), str(seat_type), fare, numberOfSeats,str(busId))

    q4= "UPDATE BUSJOURNEYHOURS SET BUS_ID='{}',SOURCE_CITY='{}',DESTINATION='{}',JOURNEY_HOURS={} " \
        "WHERE BUS_ID='{}'".format(str(busId), str(source), str(destination), journeyHours,str(busId))
    try:
        cur.execute(q1)
        cur.execute(q2)
        cur.execute(q3)
        cur.execute(q4)
        cur.execute('commit')
        return 1
    except:
        cur.execute('rollback')
        return -1




def updatePlane(planeId,planeName,source,destination,fare,numberOfSeats,journeyHours,departureDate,departureTime,plane_class):
    q1="UPDATE PLANE SET PLANE_ID='{}',PLANE_NAME='{}' " \
       "WHERE PLANE_ID='{}'".format(str(planeId),str(planeName),str(planeId))

    q2 = "UPDATE PLANEDEPARTURETIME SET PLANE_ID='{}',SOURCE_CITY='{}',DEPARTURE_TIME='{}' " \
         "WHERE PLANE_ID='{}'".format(str(planeId),str(source), str(departureTime),str(planeId))

    q3 = "UPDATE PLANERESERVATION SET PLANE_ID='{}',CLASS='{}',SOURCE_CITY='{}',DESTINATION='{}',DEPARTURE_DATE='{}',FARE={},NO_OF_SEATS={} " \
         "WHERE PLANE_ID='{}'".format(str(planeId), str(plane_class), str(source), str(destination), str(departureDate), fare, numberOfSeats,str(planeId))

    q4="UPDATE PLANEJOURNEYHOURS SET PLANE_ID='{}',SOURCE_CITY='{}',DESTINATION='{}',JOURNEY_HOURS={} " \
       "WHERE PLANE_ID='{}'".format(str(planeId), str(source), str(destination), journeyHours,str(planeId))
    try:
        cur.execute(q1)
        cur.execute(q2)
        cur.execute(q3)
        cur.execute(q4)
        cur.execute('commit')
        return 1
    except:
        cur.execute('rollback')
        return -1



def updateTrain(trainId,trainName,source,destination,fare,numberOfSeats,journeyHours,trainStatus,departureDate,departureTime,train_class):
    q1="UPDATE TRAIN SET TRAIN_ID='{}',TRAIN_NAME='{}' WHERE TRAIN_ID='{}'".format(str(trainId),str(trainName),str(trainId))

    q2= "UPDATE TRAINDEPARTURETIME SET TRAIN_ID='{}',SOURCE_CITY='{}',DEPARTURE_TIME='{}' " \
        "WHERE TRAIN_ID='{}'".format(str(trainId),str(source), str(departureTime),str(trainId))

    q3= "UPDATE TRAINJOURNEYHOURS SET TRAIN_ID='{}',SOURCE_CITY='{}',DESTINATION='{}',JOURNEY_HOURS={} " \
        "WHERE TRAIN_ID='{}'".format(str(trainId), str(source), str(destination), journeyHours,str(trainId))

    q4="UPDATE TRAINRESERVATION SET TRAIN_ID='{}',CLASS='{}',SOURCE_CITY='{}',DESTINATION='{}',DEPARTURE_DATE='{}'," \
       "FARE={},TRAIN_STATUS='{}',NO_OF_SEATS={} WHERE TRAIN_ID='{}'".format(str(trainId), str(train_class), str(source), str(destination), str(departureDate), fare, str(trainStatus),numberOfSeats,str(trainId))
    try:
        cur.execute(q1)
        cur.execute(q2)
        cur.execute(q3)
        cur.execute(q4)
        cur.execute('commit')
        return 1
    except:
        cur.execute('rollback')
        return -1

