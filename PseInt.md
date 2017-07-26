## Comandos para PseInt

Utilizaremos el comando Escribir para mostrar algo por la terminal, por ejemplo:

```
Proceso HolaMundo
	Escribir '¡Hola Mundo!';	
FinProceso
```

Para declarar variables se escribira como sigue:

```
Proceso sin_titulo
	Definir Edad, Edad2, Edad3 Como Entero;
	Definir Nota Como Real;
	Definir LetraDNI Como Caracter;
	Definir NombreYApellido Como Cadena;
	Definir Encontrado como Logico;
FinProceso
```

Definir seguido del nombre de la variable luego "Como" mas el tipo de variable que pueden ser "Entero", "Real", "Caracter", "Cadena" y "Logico", para asignar un tipo de dato a varias variables a la vez usaremos por ejemplo "Definir Edad, Edad2, Edad3 Como Entero;"

Para asignar un valor a esas variables seria:

```
Proceso sin_titulo
	Definir Edad Como Entero;
	Definir Nota Como Real;
	Definir LetraDNI Como Caracter;
	Definir NombreYApellido Como Cadena;
	Definir Encontrado como Logico;
	
	Edad <- 10;
	Nota <- 9.5;
	LetraDNI <- 'L'
	NombreYApellido <- 'Javier Ruiz'
	Encontrado <- FALSO;
	
FinProceso
```

Nombre de la variable seguido de "<-" y el valor que queremos asignarle, que tendra que ser un valor valido para el tipo de dato con el que la declaramos.

Para asignar un valor a una variable desde el teclado usaremos el comando "Leer" seguido del nombre de la variable, y para escribir en pantalla el valor de una variable usaremos el comando "Escribir" seguido del nombre de la variable, o incluso podemos usar Escribir con una cadena de tecto entre comillas para dar instrucciones al usuario:

```
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
	
	Escribir Nota;
	Escribir LetraDNI;
	Escribir NombreYApellido;
FinProceso
```

O a la hora de escribir en pantalla podemos concatenar varias entradas en una sola linea:


