import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "bd_notes")

cursor = db.cursor()
global resultsExportUsers
resultsExportUsers = []

def get_users():
    del resultsExportUsers[:]
    sql = "SELECT * FROM t_user"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            item = {
                "id_user": row[0],
                "public_id": row[1],
                "name": row[2],
                "password": row[3],
                "admin": row[4]
            }
            resultsExportUsers.append(item)
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()

def get_user(user, id_user):
    del resultsExportUsers[:]
    sql = "SELECT * FROM t_user WHERE id_user='%s'" % (id_user)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            item = {
                "id_user": row[0],
                "public_id": row[1],
                "name": row[2],
                "password": row[3],
                "admin": row[4]
            }
            resultsExportUsers.append(item)
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()

def create_user(user):
    sql = "INSERT INTO t_user(public_id, password, name, admin) values('%s', '%s', '%s', '%s')" % (user['public_id'], user['password'], user['name'], user['admin'])
    try:
        cursor.execute(sql)
        db.commit()
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            db.rollback()
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()

def update_user(user, id_user):
    #print ("update_user: %s" % user['public_id'])
    sql = "UPDATE t_user SET public_id='%s', password='%s', name='%s', admin='%s'WHERE id_user='%s'" % (user['public_id'], user['password'], user['name'], user['admin'], id_user)
    print ("update_user: %s" % str(sql))
    try:
        cursor.execute(sql)
        db.commit()
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            db.rollback()
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()

def delete_user(user, id_user):
    sql = "DELETE FROM t_user WHERE id_user='%s'" % (id_user)
    try:
        cursor.execute(sql)
        db.commit()
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            db.rollback()
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()

def delete_users():
    sql = "DELETE FROM t_user"
    try:
        cursor.execute(sql)
        db.commit()
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            db.rollback()
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()