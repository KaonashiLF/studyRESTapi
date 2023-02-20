import sqlite3


class database:
    
    create_table = "CREATE TABLE IF NOT EXISTS hoteis\
    (\
        hotel_id text PRIMARY KEY,\
        nome text,\
        estrelas real,\
        diaria real,\
        cidade text\
    )"
    
    def __init__(self, database_name) -> None:
        self.database_name = database_name
        
    def create_database(self):
        conn = sqlite3.connect(f'GitHub/studyRESTapi/database/{self.database_name}.db')
        cursor = conn.cursor()
        
        cursor.execute(select_hotel)
        conn.commit()
        conn.close()

    def create_table(self,**kwargs):
        """
        kwargs syntax -> 'column name': 'data column type'
        """

    
    
conn = sqlite3.connect(f'GitHub/studyRESTapi/database/database.db')
cursor = conn.cursor()


hotel_id = 'alpha'

select_hotel = f"SELECT * FROM hoteis WHERE hotel_id = '{hotel_id}'"
create_hotel = "INSERT INTO hoteis VALUES ('alpha', 'Alpha Hotel', 4.3, 345.30, 'Rio de Janeiro')"
    
cursor.execute()
conn.close()
conn.commit()