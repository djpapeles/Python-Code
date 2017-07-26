Proceso sin_titulo
	Definir Edad, Edad2, Edad3 Como Entero;
	Definir Nota Como Real;
	Definir LetraDNI Como Caracter;
	Definir NombreYApellido Como Cadena;
	Definir Encontrado como Logico;
	
	Edad <- 10;
	Nota <- 9.5;
	LetraDNI <- 'L'
	NombreYApellido <- 'Javier Ruiz'
	Encontrado <- FALSO;
	
	Escribir  'Introduce la nota';
	Leer Nota;
	Escribir 'Introduce la letra de dni';
	Leer LetraDNI;
	Escribir  'Introduce el nombre y apellido';
	Leer NombreYApellido
	
	Escribir 'La nota es ', Nota;
	Escribir 'La letra de dni es ', LetraDNI;
	Escribir 'El nombre y apellido es ', NombreYApellido;
FinProceso
