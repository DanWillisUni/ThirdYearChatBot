import PartTwo.Helpers.DB as db
import appSettings


def get_all_data_on_station(station):
    """
    Runs the GetAllInfoOnStationTimes stored procedure with the parameters

    :param station:
    Station name to get all the data on
    :return:
    The results for the SP
    """
    conn_str = appSettings.get_conn_str()
    query = "EXEC GetAllInfoOnStationTimes @station = '" + station + "'"  # sets the query string
    result = db.run_query(conn_str, query,True)  # execute the stored procedure
    return result


def get_lateness_from_stations(from_station, to_station, range_start, range_end):
    """
    Runs the GetLatenessFromStations stored procedure with the parameters

    :param from_station:
    The station A
    :param to_station:
    The station B
    :param range_start:
    The range of late by start
    :param range_end:
    The range of late by end
    :return:
    String array of all the rows from the query
    """
    conn_str = appSettings.get_conn_str()
    query = "EXEC GetLatenessFromStations @FromStation = '" + from_station + "',@ToStation = '" + to_station + "',@LateByRangeStart = " + str(range_start) + ",@LateByRangeEnd = " + str(range_end)  # generate query
    result = db.run_query(conn_str, query,True)  #run the query
    return result


def get_lateness_of_both(from_station, to_station):
    """
    Executes the GetLatenessOfBoth stored procedure

    :param from_station:
    The Station A name
    :param to_station:
    The station B name
    :return:
    String array of the result rows
    """
    conn_str = appSettings.get_conn_str()
    query = "EXEC GetLatenessOfBoth @FROM = '" + from_station + "',@TO = '" + to_station + "'"  # generate the query string
    result = db.run_query(conn_str, query,True)  # run the query on the database
    return result


def compare_stations(a, b):
    """
    Executes the CompareStations stored procedure with parameters

    :param a:
    Station Name A
    :param b:
    Station Name B

    :return:
    String array of the rows of results
    """
    conn_str = appSettings.get_conn_str()
    query = "EXEC CompareStations @A = '" + a + "',@B = '" + b + "'"  # generate the query
    result = db.run_query(conn_str, query,True)  # run the query
    return result[0][:-2]


def get_lateness_from_rid(rid):
    """
    Execute the GetLatenessFromRID stored procedure

    :param rid:
    Route ID to search

    :return:
    String array of the result rows
    """
    conn_str = appSettings.get_conn_str()
    query = "EXEC GetLatenessFromRID @rid = '" + rid + "'"  # get the query string
    result = db.run_query(conn_str, query,True)  # run the query
    return result


def insertIntoConversation(message,userID,isHuman):
    conn_str = appSettings.get_conn_str()
    query = "INSERT INTO [AIChatBot].[dbo].[Conversation_Record] ([userID],[message],[fromUser],[dateTimeID]) VALUES ('" + str(userID) + "',(CASE WHEN '" + message + "' = '' THEN null ELSE '" + message + "' END) ," + str(int(isHuman)) + ",GETDATE())"  # get the query string
    db.run_query(conn_str, query,False)  # run the query


def get_last_user_id():
    conn_str = appSettings.get_conn_str()
    query = "SELECT TOP(1) [userID] FROM [dbo].[Conversation_Record] WHERE [fromUser] = 1 ORDER BY [dateTimeID] desc"
    return int(db.run_query(conn_str, query,True)[0].replace(", ","").replace("'",""))  # run the query

def get_last_message(user_id):
    conn_str = appSettings.get_conn_str()
    query = "SELECT TOP(1) message FROM Conversation_Record WHERE userID = '" + str(user_id) + "' AND [fromUser] = 1 ORDER BY [dateTimeID] desc"
    return db.run_query(conn_str, query,True)[0].replace(", ", "").replace("'", "") # run the query
