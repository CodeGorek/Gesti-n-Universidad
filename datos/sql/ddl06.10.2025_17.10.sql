USE iec_170_n2;

CREATE TABLE IF NOT EXISTS carreras(
    cod_carrera VARCHAR(30) NOT NULL,
    carrera VARCHAR(200) NOT NULL,
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

CREATE TABLE IF NOT EXISTS cursos(
    cod_curso VARCHAR(20) NOT NULL,
    curso VARCHAR(30) NOT NULL,
    creditos INT NOT NULL,
    cod_carrera VARCHAR(30) NOT NULL,
    pre_requisitos VARCHAR(30) NOT NULL,
    constraint pk_cursos primary key(cod_curso), # definir la clave primaria 
    constraint fk_carreras foreign key(cod_carrera) references carreras(cod_carrera) # definir la clave foranea
);

CREATE TABLE IF NOT EXISTS ESTUDIANTE (
    matricula_estudiante INT NOT NULL AUTO_INCREMENT,
    estudiante VARCHAR(100) NOT NULL,
    correo_estudiante VARCHAR(40) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    direccion_estudiante: VARCHAR(40), NOT NULL
    constraint pk_estudiante primary key(matricula_estudiante), # definir la clave primaria 
    constraint uq_correo unique(correo_estudiante) # definir la restricción de unicidad
);

CREATE TABLE IF NOT EXISTS PROFESOR(
    cod_profesor INT NOT NULL, AUTO_INCREMENT
    profesor VARCHAR(30) NOT NULL,
    correo_profesor VARCHAR(30) NOT NULL,
    especialidad VARCHAR(30),
    constraint pk_profesor primary key(cod_profesor) # definir la clave primaria 
    constraint uq_correo unique(correo_profesor) # definir la restricción de unicidad
);
CREATE TABLE IF NOT EXISTS CARRERA_CURSOS (
    cod_carrera_curso INT NOT NULL AUTO_INCREMENT,
    cod_curso VARCHAR(20) NOT NULL,
    cod_carrera INT NOT NULL,
    constraint pk_carrera_curso primary key(cod_carrera_curso), # definir la clave primaria 
    constraint fk_curso foreign key(cod_curso) references curso(cod_curso), # definir la clave foranea 
    constraint fk_carrera foreign key(cod_carrera) references profesor(cod_carrera) # definir la clave foranea
);
/* Para asociar muchas carreras y muchos cursos*/ 