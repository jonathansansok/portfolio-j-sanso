CREATE TABLE Lectores(
id serial,
nombre varchar(100),
apellido varchar(100),
email varchar(100),
nacimiento date,
PRIMARY KEY (id)
);
--insertar lectores 
INSERT INTO Lectores (nombre, apellido, email, nacimiento) values
		('Juan Alberto', 'Cortéz', 'juancortez@gmail.com', '20/06/1983');
INSERT INTO Lectores (nombre, apellido, email, nacimiento) values
		('Antonia', 'de los Rios', 'antoniarios_23@yahoo.com', '24/11/1978');
INSERT INTO Lectores (nombre, apellido, email, nacimiento) values
		('Nicolás', 'Martin', 'nico_martin@gmail.com', '11/07/1986');
INSERT INTO Lectores (nombre, apellido, email, nacimiento) values
		('Néstor', 'Casco', 'nestor_casco2331@hotmail.com', '11/02/1981');
INSERT INTO Lectores (nombre, apellido, email, nacimiento) values
		('Lisa', 'Perez', 'lisperez@hotmail.com', '11/08/1994');
INSERT INTO Lectores (nombre, apellido, email, nacimiento) values
		('Ana Rosa', 'Estagnoli', 'anros@abcdatos.com', '15/10/1974');
INSERT INTO Lectores (nombre, apellido, email, nacimiento) values
		('Milagros', 'Pastoruti', 'mili_2231@gmail.com', '22/01/2001');
INSERT INTO Lectores (nombre, apellido, email, nacimiento) values
		('Pedro', 'Alonso', 'alonso.pedro@impermeabilizantesrosario.com', '05/09/1983');
INSERT INTO Lectores (nombre, apellido, email, nacimiento) values
		('Arturo Ezequiel', 'Ramírez', 'artu.rama@outlook.com', '29/03/1998');
INSERT INTO Lectores (nombre, apellido, email, nacimiento) values
		('Juan Ignacio', 'Altarez', 'juanaltarez@yahoo.com', '24/08/1975');
	SELECT * FROM Lectores;

CREATE TABLE Libros(
id serial,
nombre varchar(100),
editorial varchar(100),
autor varchar(100),
isbn int,
PRIMARY KEY (id)
);
--insertamos libros
INSERT INTO Libros (nombre, editorial, autor, isbn) values
		('Cementerio de animales', 'Ediciones de Mente', 'Stephen King', '4568874');
INSERT INTO Libros (nombre, editorial, autor, isbn) values
		('En el nombre de la rosa', 'España', 'Umberto Eco', '44558877');
INSERT INTO Libros (nombre, editorial, autor, isbn) values
		('Cien años de soledad', 'Sudamericana', 'Gabriel García Márquez', '7788845');
INSERT INTO Libros (nombre, editorial, autor, isbn) values
		('El diario de Ellen Rimbauer', 'Maine', 'Stephen King', '45699874');
INSERT INTO Libros (nombre, editorial, autor, isbn) values
		('La hojarasca', 'Sudamericana', 'Gabriel García Márquez', '2564111');
INSERT INTO Libros (nombre, editorial, autor, isbn) values
		('El amor en tiempos de cólera', 'Sudamericana', 'Gabriel García Márquez', '2564111');
INSERT INTO Libros (nombre, editorial, autor, isbn) values
		('La casa de los espíritus', 'Ediciones Chile', 'Isabel Allende', '5544781');
INSERT INTO Libros (nombre, editorial, autor, isbn) values
		('Paula', 'Ediciones Chile', 'Isabel Allende', '225455447	');
INSERT INTO Libros (nombre, editorial, autor, isbn) values
		('La tregua', 'Alfa', 'Mario Benedetti', '2225412');
INSERT INTO Libros (nombre, editorial, autor, isbn) values
		('Gracias por el fuego', 'Alfa', 'Mario Benedetti', '88541254');
		
SELECT * FROM Libros;

CREATE TABLE lectoresLibros(
id_lectores int,
id_libros int,
CONSTRAINT lectoresLibros_idLectores FOREIGN KEY(id_lectores) REFERENCES Lectores(id),
CONSTRAINT lectoresLibros_idLibros FOREIGN KEY(id_libros) REFERENCES Libros(id),
PRIMARY KEY(id_lectores, id_libros)
);

SELECT * FROM lectoresLibros;
--4lectores en prestamo a 5 libros;
INSERT INTO lectoresLibros (id_lectores, id_libros) values (1,6);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (1,2);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (1,3);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (1,4);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (1,5);


INSERT INTO lectoresLibros (id_lectores, id_libros) values (2,2);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (2,4);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (2,7);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (2,8);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (2,9);

INSERT INTO lectoresLibros (id_lectores, id_libros) values (3,4);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (3,2);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (3,5);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (3,8);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (3,6);

INSERT INTO lectoresLibros (id_lectores, id_libros) values (4,7);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (4,1);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (4,3);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (4,5);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (4,8);

SELECT * FROM lectoresLibros;
--3 lectores tienen prestamos 3 libros

INSERT INTO lectoresLibros (id_lectores, id_libros) values (5,1);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (5,3);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (5,6);

INSERT INTO lectoresLibros (id_lectores, id_libros) values (6,2);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (6,6);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (6,8);

INSERT INTO lectoresLibros (id_lectores, id_libros) values (7,9);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (7,8);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (7,3);

--2 lectores tienen prestamos 2 libros
INSERT INTO lectoresLibros (id_lectores, id_libros) values (8,2);
INSERT INTO lectoresLibros (id_lectores, id_libros) values (9,5);

--lectores tiene un libro en prestamos
---prestamo al octavo lector
--INSERT INTO lectoresLibros (id_lectores, id_libros) values (8,3);

--prestamo al noveno lector
--INSERT INTO lectoresLibros (id_lectores, id_libros) values (9,5);

--consulta para saber cuantas veces se presta un determinado libro ordenado de mayor a menor 
SELECT id_libros, COUNT(id_libros) AS cantidad  FROM lectoresLibros GROUP BY id_libros ORDER BY cantidad DESC;

SELECT COUNT(id_libros) AS cantidad FROM lectoresLibros  WHERE id_libros = 2;


--consulta para saber cuantas veces , tiene en prestamos cada lector 
--lector1
SELECT COUNT(id_lectores) FROM lectoresLibros WHERE id_lectores = 1;
--lector2
SELECT COUNT(id_lectores) FROM lectoresLibros WHERE id_lectores = 2;
--lector3
SELECT COUNT(id_lectores) FROM lectoresLibros WHERE id_lectores = 3;
--lector9
SELECT COUNT(id_lectores) FROM lectoresLibros WHERE id_lectores = 8;

--con uno de los lectores que cargaste 5 libros ,simula que devolvio uno
DELETE FROM lectoresLibros WHERE id_lectores = 1 AND id_libros = 2;

SELECT * FROM lectoresLibros;

--obtene el promedio de edad de los lectores,

SELECT AVG (date_part('year', AGE(nacimiento))) AS promedioEdad FROM Lectores;

--obtener el lector con mas anios
SELECT MAX (date_part('YEAR', AGE(nacimiento))) AS mayorEdad FROM Lectores;

--obtener el lector con menos anios
SELECT MIN (date_part('YEAR', AGE(nacimiento))) AS menorEdad FROM Lectores;


--ordenar edades de mayor A MENOR
SELECT nombre, date_part('YEAR', AGE(nacimiento)) AS  edad FROM Lectores ORDER BY edad DESC;

ALTER TABLE pruebaLibros ALTER COLUMN nombre TYPE varchar(100);
ALTER TABLE pruebaLibros ADD COLUMN descripccion varchar(500);

CREATE OR REPLACE VIEW libros_prestados
AS
SELECT Lectores.apellido, Lectores.nombre, Libros.nombre as nombreLibro, Libros.editorial, Libros.autor, Libros.isbn
FROM Lectores
INNER JOIN lectoresLibros ON lectoresLibros.id_lectores  = Lectores.id
INNER JOIN libros ON lectoresLibros.id_libros = libros.id

drop view libros_prestados;

SELECT * from libros_prestados WHERE nombre = 'Pedro' AND apellido = 'Alonso'

-API 4.1
CREATE OR REPLACE FUNCTION 
devolverLibro(idLector int, idLibro int)
RETURNS void AS $$
BEGIN
DELETE FROM lectoresLibros WHERE lectoresLibros.id_lectores = idLector
and lectoresLibros.id_libros = idlibro;
end;
$$ LANGUAGE plpgsql
-- llamada a la funcion
SELECT * FROM lectoresLibros;
SELECT * FROM devolverLibro(3, 6)
SELECT * FROM devolucion_log
---4.2
CREATE TABLE devolucion_log(
id_lectores integer NOT NULL,
id_libros integer NOT NULL,
fecha timestamp
);
--funcion trigger
CREATE OR REPLACE FUNCTION funcion_tr_delete() RETURNS TRIGGER
AS $$

BEGIN

INSERT INTO devolucion_log(id_lectores, id_libros, fecha) VALUES (old.id_lectores, old.id_libros, now());

RETURN OLD;
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER trigger_delete BEFORE DELETE ON lectoresLibros
FOR EACH ROW
EXECUTE PROCEDURE funcion_tr_delete();
--return old 

--4.2 funcion que permite saber la cantidad de ejemplares prestados
--actualmente.
CREATE OR REPLACE FUNCTION retornar_cantidad_prestados(integer) RETURNS
bigint AS
'SELECT COUNT(id_libros) as cantidad FROM lectoresLibros  WHERE id_libros = $1;'

LANGUAGE SQL;
SELECT retornar_cantidad_prestados(5)