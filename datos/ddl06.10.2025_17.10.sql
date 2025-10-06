USE iec_170_n2;

CREATE TABLE carrera IF NOT EXISTS (
    cod_carrera VARCHAR(10) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    creditos_max_semestre INT NOT NULL,
    semestre_duracion INT NOT NULL,
    constraint pk_carrera primary key(cod_carrera) # definir la clave primaria 
);

CREATE TABLE CURSO_ESTUDIANTE IF NOT EXISTS (
    cod_curso VARCHAR(10) NOT NULL,
    cod_estudiante VARCHAR(10) NOT NULL,
    anio INT NOT NULL,
    semestre INT NOT NULL,
    nota_final DECIMAL(4,2),
    constraint pk_curso_estudiante primary key(cod_curso, cod_estudiante, anio, semestre), # definir la clave primaria 
    constraint fk_curso foreign key(cod_curso) references curso(cod_curso), # definir la clave foranea 
    constraint fk_estudiante foreign key(cod_estudiante) references estudiante(cod_estudiante) # definir la clave foranea 
);

CREATE TABLE CURSO_PROFESOR IF NOT EXISTS (
    id_profesor_curso INT NOT NULL AUTO_INCREMENT,
    codigo_curso VARCHAR(10) NOT NULL,
    id_profesor VARCHAR(10) NOT NULL,
    constraint pk_curso_profesor primary key(id_profesor_curso), # definir la clave primaria 
    constraint fk_curso foreign key(codigo_curso) references curso(codigo_curso), # definir la clave foranea 
    constraint fk_profesor foreign key(id_profesor) references profesor(id_profesor) # definir la clave foranea


CREATE TABLE CURSO IF NOT EXISTS (
    cod_curso VARCHAR(10) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    creditos INT NOT NULL,
    cod_carrera VARCHAR(10) NOT NULL,
    constraint pk_curso primary key(cod_curso), # definir la clave primaria 
    constraint fk_carrera foreign key(cod_carrera) references carrera(cod_carrera) # definir la clave foranea 
);

CREATE TABLE ESTUDIANTE IF NOT EXISTS (
    cod_estudiante VARCHAR(10) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    direccion VARCHAR(200),
    telefono VARCHAR(15),
    email VARCHAR(100),
    cod_carrera VARCHAR(10) NOT NULL,
    constraint pk_estudiante primary key(cod_estudiante), # definir la clave primaria 
    constraint fk_carrera foreign key(cod_carrera) references carrera(cod_carrera) # definir la clave foranea 
);

CREATE TABLE HORARIO IF NOT EXISTS (
    cod_horario VARCHAR(10) NOT NULL,
    cod_curso VARCHAR(10) NOT NULL,
    dia_semana INT NOT NULL, # 1= Lunes, 2= Martes, ..., 7= Domingo
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    aula VARCHAR(50) NOT NULL,
    constraint pk_horario primary key(cod_horario), # definir la clave primaria 
    constraint fk_curso foreign key(cod_curso) references curso(cod_curso) # definir la clave foranea 
);

CREATE TABLE PROFESOR IF NOT EXISTS (
    id_profesor VARCHAR(10) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100),
    constraint pk_profesor primary key(id_profesor) # definir la clave primaria 
);

CREATE TABLE RECURSOS IF NOT EXISTS (
    id_recurso INT NOT NULL AUTO_INCREMENT,
    codigo_curso VARCHAR(10) NOT NULL,
    id_profesor VARCHAR(10) NOT NULL,
    url VARCHAR(200) NOT NULL,
    constraint pk_recurso primary key(id_recurso), # definir la clave primaria 
    constraint fk_curso foreign key(codigo_curso) references curso(cod_curso), # definir la clave foranea 
    constraint fk_profesor foreign key(id_profesor) references profesor(id_profesor) # definir la clave foranea
);

