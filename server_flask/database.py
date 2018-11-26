import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "bd_notes")

cursor = db.cursor()
global resultsExportEtudiants
resultsExportEtudiants = []

def get_studients():
    del resultsExportEtudiants[:]
    sql = "SELECT * FROM t_etudiant"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            item = {
                "id_etudiant": row[0],
                "matricule": row[1],
                "prenom": row[2],
                "nom": row[3]
            }
            resultsExportEtudiants.append(item)
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

def get_studient(etudiant, id_etudiant):
    del resultsExportEtudiants[:]
    sql = "SELECT * FROM t_etudiant WHERE id_etudiant='%s'" % (id_etudiant)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            item = {
                "id_etudiant": row[0],
                "matricule": row[1],
                "prenom": row[2],
                "nom": row[3]
            }
            resultsExportEtudiants.append(item)
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

def create_studient(etudiant):
    sql = "INSERT INTO t_etudiant(matricule, nom, prenom) values('%s', '%s', '%s')" % (etudiant['matricule'], etudiant['nom'], etudiant['prenom'])
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

def update_studient(etudiant, id_etudiant):
    #print ("update_studient: %s" % etudiant['matricule'])
    sql = "UPDATE t_etudiant SET matricule='%s', nom='%s', prenom='%s' WHERE id_etudiant='%s'" % (etudiant['matricule'], etudiant['nom'], etudiant['prenom'], id_etudiant)
    print ("update_studient: %s" % str(sql))
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

def delete_studient(etudiant, id_etudiant):
    sql = "DELETE FROM t_etudiant WHERE id_etudiant='%s'" % (id_etudiant)
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

def delete_studients():
    sql = "DELETE FROM t_etudiant"
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