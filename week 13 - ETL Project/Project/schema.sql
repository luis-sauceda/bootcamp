drop table wine_csv;

CREATE TABLE wine_csv (
    ID SERIAL PRIMARY KEY,
    pais VARCHAR  NOT NULL,
   descripcion VARCHAR   NOT NULL,
    puntaje INTEGER NOT NULL,
    precio INTEGER NOT NULL,
    provincia VARCHAR NOT NULL,
    variedad VARCHAR NOT NULL,
    casa VARCHAR NOT NULL,
    calidad_precio FLOAT NOT NULL
    );
	
drop table wine_json;
    CREATE TABLE wine_json (
    ID SERIAL PRIMARY KEY,
    pais VARCHAR   NOT NULL,
    descripcion VARCHAR   NOT NULL,
    puntaje INTEGER NOT NULL,
    precio INTEGER NOT NULL,
    provincia VARCHAR NOT NULL,
    catador VARCHAR NOT NULL,
    nombre VARCHAR NOT NULL,
    variedad VARCHAR NOT NULL,
    casa VARCHAR NOT NULL,
    calidad_precio FLOAT NOT NULL    
    );
	
select * from wine_json;