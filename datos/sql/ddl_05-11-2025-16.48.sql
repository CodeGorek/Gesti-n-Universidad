Alter TABLE carreras add Column habilitado Tinyint default 1 not null;
Alter TABLE estudiantes add Column habilitado Tinyint default 1 not null;
Alter TABLE cursos add Column habilitado Tinyint default 1 not null;
alter table profesores add Column habilitado Tinyint default 1 not null;
Alter table carrera_cursos add Column habilitado Tinyint default 1 not null;
alter table profesor_curso add column habilitado Tinyint default 1 not null;
alter table estudiante_curso add Column habilitado Tinyint default 1 not null;

