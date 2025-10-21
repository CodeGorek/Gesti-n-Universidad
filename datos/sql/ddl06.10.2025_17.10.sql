USE iec_170_n2;

CREATE TABLE IF NOT EXISTS carreras(
    cod_carrera VARCHAR(30) NOT NULL,
    descripción VARCHAR(200) NOT NULL,
    creditos_max_semestre INT NOT NULL,
    semestre_duracion INT NOT NULL,
    constraint pk_carrera primary key(cod_carrera)    
);

CREATE TABLE IF NOT EXISTS ESTUDIANTE_CURSO(
    cod_estudiante_curso INT NOT NULL, AUTO_INCREMENT
    matricula_estudiante INT NOT NULL, AUTO_INCREMENT
    cod_curso VARCHAR(20) NOT NULL,
    constraint pk_estudiante_curso primary key(cod_estudiante_curso), # definir la clave primaria 
    constraint fk_curso foreign key(cod_curso) references curso(cod_curso), # definir la clave foranea 
    constraint fk_estudiante foreign key(matricula_estudiante) references estudiante(matricula_estudiante) # definir la clave foranea 
);

CREATE TABLE IF NOT EXISTS PROFESOR_CURSO (
    cod_profesor_curso INT NOT NULL AUTO_INCREMENT,
    cod_curso VARCHAR(20) NOT NULL,
    cod_profesor INT NOT NULL,
    constraint pk_profesor_curso primary key(cod_profesor_curso), # definir la clave primaria 
    constraint fk_curso foreign key(cod_curso) references curso(cod_curso), # definir la clave foranea 
    constraint fk_profesor foreign key(cod_profesor) references profesor(cod_profesor) # definir la clave foranea
);

CREATE TABLE CURSO IF NOT EXISTS (
    cod_curso VARCHAR(20) NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    creditos INT NOT NULL,
    cod_carrera VARCHAR(30) NOT NULL,
    pre_requisitos VARCHAR(30),NOT NULL
    cod_horario INT NOT NULL,
    constraint pk_curso primary key(cod_curso), # definir la clave primaria 
    constraint fk_carrera foreign key(cod_carrera) references carrera(cod_carrera) # definir la clave foranea
);

CREATE TABLE IF NOT EXISTS ESTUDIANTE (
    matricula_estudiante INT NOT NULL AUTO_INCREMENT,
    nombre_estudiante VARCHAR(100) NOT NULL,
    correo_estudiante VARCHAR(40) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    direccion_estudiante: VARCHAR(40), NOT NULL
    constraint pk_estudiante primary key(matricula_estudiante), # definir la clave primaria 
    constraint uq_correo unique(correo_estudiante) # definir la restricción de unicidad
);

<<<<<<< HEAD:datos/sql/ddl06.10.2025_17.10.sql

CREATE TABLE PROFESOR IF NOT EXISTS (
=======
CREATE TABLE IF NOT EXISTS PROFESOR(
>>>>>>> 2cef96508dc6e4e3e2fa05c6e9d5654b677595e2:datos/ddl06.10.2025_17.10.sql
    cod_profesor INT NOT NULL, AUTO_INCREMENT
    nombre_profesor VARCHAR(30) NOT NULL,
    correo_profesor VARCHAR(30) NOT NULL,
    especialidad VARCHAR(30),
    constraint pk_profesor primary key(cod_profesor) # definir la clave primaria 
    constraint uq_correo unique(correo_profesor) # definir la restricción de unicidad
);
<<<<<<< HEAD:datos/sql/ddl06.10.2025_17.10.sql


=======
>>>>>>> 2cef96508dc6e4e3e2fa05c6e9d5654b677595e2:datos/ddl06.10.2025_17.10.sql
