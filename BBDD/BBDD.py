# -*- coding: utf-8 -*-

import sqlite3 as sql
import os

from datetime import datetime

class BaseDatosPruebasRealizadas:
    def __init__(self, db_path):
        self.name = db_path
        exist = os.path.exists(self.name)

        self.connect()

        #if not exist:
        #    self.create_db()

    def connect(self):
        self.conn = sql.connect(self.name) # connection
        self.c = self.conn.cursor() # Cursor
        return

    def disconnect(self):
        self.conn.close()
        return

    def new_person(self, sujetoId, edad=None, sexo=None):
        self.c.execute(f'''INSERT INTO Sujetos (SujetoID, Edad, Sexo)
                    VALUES ({str(sujetoId)},{'NULL' if edad==None else str(edad)},
                    {'NULL' if sexo==None else sexo})''')
        self.conn.commit()
        return

    def get_person_details(self, personID):
        details = self.c.execute(f"SELECT * FROM Sujetos where SujetoID = {personID}").fetchone()
        return details

    def get_all_personId(self):
        all_personId = self.c.execute("SELECT SujetoID from Sujetos").fetchall()
        return [personId_tuple[0] for personId_tuple in all_personId]

    def new_session(self, personID, edfFilePath, dateTime=str(datetime.now())):
        self.c.execute(f"INSERT INTO PruebasRealizadas (SujetoID, PathArchivoEDF, FechaHora) VALUES ({personID},'{edfFilePath}','{dateTime}')")
        self.conn.commit()
        lastMovementID = self.c.execute("SELECT MovimientoID from Movimientos ORDER BY MovimientoID DESC").fetchone()[0]
        return lastMovementID

    def get_last_movementId(self):
        lastMovementID = self.c.execute("SELECT MovimientoID from Movimientos ORDER BY MovimientoID DESC").fetchone()[0]
        return lastMovementID

    def new_session_details(self, sessionID, score, testID):
        newDetailNumber = self.c.execute(f"SELECT COALESCE(MAX(TestRealizadoNumber),0)+1 FROM PruebasDetalles WHERE PruebaRealizadaID={sessionID}").fetchone()[0]
        self.c.execute(f"INSERT INTO PruebasDetalles (PruebaRealizadaID, TestRealizadoNumber, TestID, Puntuacion) VALUES ({sessionID},{newDetailNumber},{testID},{score})")
        self.conn.commit()
        return

    def new_test(self, name, description):
        self.c.execute(f"INSERT INTO Tests (TestNombre, TestDescripcion) VALUES ('{name}','{description}')")
        self.conn.commit()
        return

    def get_all_test(self):
        all_test = self.c.execute("SELECT TestID, TestNombre, TestDescripcion from Tests order by TestID").fetchall()
        return all_test
