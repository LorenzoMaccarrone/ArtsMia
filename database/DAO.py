from database.DB_connect import DBConnect
from model.opera import Opera
from model.connessioni import Connessione

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllOpere():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from objects o"""

        cursor.execute(query,)

        for row in cursor:
            result.append(Opera(**row))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getAllConnessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select eo.object_id as o1 ,eo2.object_id as o2 , count(*) as peso
                    from exhibition_objects eo, exhibition_objects eo2 
                    where eo.exhibition_id=eo2.exhibition_id 
                    and eo.object_id<eo2.object_id 
                    group by eo.object_id, eo2.object_id 
                    order by peso desc"""

        cursor.execute(query,)

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result

