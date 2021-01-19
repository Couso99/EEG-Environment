BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Sujetos" (
	"SujetoID"	INTEGER NOT NULL UNIQUE,
	"Edad"	INTEGER NOT NULL,
	"Sexo"	TEXT NOT NULL,
	PRIMARY KEY("SujetoID")
);
CREATE TABLE IF NOT EXISTS "PruebasRealizadas" (
	"PruebaRealizadaID"	INTEGER NOT NULL UNIQUE,
	"SujetoID"	INTEGER NOT NULL,
	"FechaHora"	TEXT NOT NULL,
	"PathArchivoEDF"	TEXT NOT NULL,
	PRIMARY KEY("PruebaRealizadaID"),
	FOREIGN KEY("SujetoID") REFERENCES "Sujetos"("SujetoID")
);
CREATE TABLE IF NOT EXISTS "Tests" (
	"TestID"	INTEGER NOT NULL UNIQUE,
	"TestNombre"	TEXT NOT NULL,
	"TestDescripcion"	TEXT NOT NULL,
	PRIMARY KEY("TestID")
);
CREATE TABLE IF NOT EXISTS "PruebasDetalles" (
	"PruebaRealizadaID"	INTEGER NOT NULL,
	"TestRealizadoNumber"	INTEGER NOT NULL,
	"Puntuacion"	INTEGER NOT NULL,
	"TestID"	INTEGER NOT NULL,
	PRIMARY KEY("PruebaRealizadaID","TestRealizadoNumber"),
	FOREIGN KEY("TestID") REFERENCES "Tests"("TestID"),
	FOREIGN KEY("PruebaRealizadaID") REFERENCES "PruebasRealizadas"("PruebaRealizadaID")
);
COMMIT;
