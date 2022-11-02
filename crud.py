import sqlite3


class CRUD():
    conn = sqlite3.connect('data copy.db')

    def InsertData(self, name, areaNumber):
        try:
            cursor = self.conn.cursor()
            query = """
                        INSERT INTO States (Name, AreaNumber)
                        VALUES
                        (?,?);
                    """
            data = (name, areaNumber)
            cursor.execute(query, data)
            self.conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print("Failed to insert data", e)
        finally:
            if self.conn:
                self.conn.close()
                print("Database Connection closed")
    
    def SelectFromDatabase(self):
        try:
            cursor = self.conn.cursor()
            query = """
                        SELECT StateID, AreaNumber FROM States;
                    """            
            cursor.execute(query)
            records = cursor.fetchall()            
            cursor.close()
            return records
        except sqlite3.Error as e:
            print("Failed to read data", e)
        finally:
            if self.conn:
                self.conn.close()
                print("Database Connection closed")