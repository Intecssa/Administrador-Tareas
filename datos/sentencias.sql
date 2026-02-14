CREATE TABLE IF NOT EXISTS tabla_tarea(realizador TEXT,
                                        nombre TEXT,
                                        estado TEXT,
                                        fecha_vencimiento DATE)

INSERT INTO tabla_tarea(realizador,nombre,estado,fecha_vencimiento) VALUES (?,?,?,?)

SELECT * FROM tabla_tarea

SELECT * FROM tabla_tarea WHERE nombre = ""
SELECT * FROM tabla_tarea WHERE realizador = ''

UPDATE tabla_tarea SET realizador=?,nombre=?,estado=?,fecha_vencimiento=?
                       WHERE  realizador=? and nombre=? and estado=? and fecha_vencimiento=?

DELETE FROM tabla_tarea WHERE nombre = ""