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
	
	Escribir 'La nota es ', Nota;
	Escribir 'La letra de dni es ', LetraDNI;
	Escribir 'El nombre y apellido es ', NombreYApellido;
FinProceso
```

## Operadores Algebraicos, relacionales y logicos

Algebraicos

```
Proceso Operadores
	
	Definir A, B como Enteros;
	A <- 5;
	
	Escribir A+5;
	Escribir A-5;
	Escribir A*5;
	Escribir A/5;
	Escribir A^5;
	Escribir A%5;
	
	B <- 2;
	
	Escribir A*5+10/B;
	Escribir 2*A^2+10*A+B;
	
FinProceso
```

Relacionales

```
Proceso Operadores
	
	Definir A, B como Enteros;
	A <- 5;
	B <- 2;
	
	Escribir A = B;
	Escribir A <> B;
	Escribir A < B;
	Escribir A > B;
	Escribir A <= B;
	Escribir A >= B;
	
	Escribir VERDADERO = VERDADERO;
	Escribir FALSO <> VERDADERO;
	
FinProceso
```

Relacionales

```
Proceso Operadores
	
	Definir A, B como Enteros;
	A <- 5;
	B <- 2;
	
	Escribir A = B;
	Escribir A <> B;
	Escribir A < B;
	Escribir A > B;
	Escribir A <= B;
	Escribir A >= B;
	
	Escribir VERDADERO = VERDADERO;
	Escribir FALSO <> VERDADERO;
	
FinProceso
```

Logicos

```
Proceso OperadoresLogicos

	Definir A, B como Logicos;
	
	A <- VERDADERO;
	B <- FALSO;
	
	//Escribir NO A;
	//Escribir NO B;
	
	Escribir A Y B;
	
	Escribir A O B;
	
	Escribir NO A Y NO B;
	
	Escribir NO A O NO B;
	
FinProceso
```

## Comparacion de caracteres

```
Proceso sin_titulo
	
	Escribir 'A'>'b';
	Escribir 'A'>'a';
	Escribir 'A'>'h';
	Escribir 'A'>'z';
	
FinProceso
```
## Valores de caracteres

Para saber la posicion que ocupan en el codigo ASCII Extendido
```
Proceso CaracteresANumeros

	Escribir  ConvertirANumero(' ');
	Escribir  ConvertirANumero('A');
	Escribir  ConvertirANumero('a');
	Escribir  ConvertirANumero('Z');
	Escribir  ConvertirANumero('z');
	Escribir  ConvertirANumero('~');
	Escribir  ConvertirANumero('á');
	Escribir  ConvertirANumero('ñ');
	
FinProceso
```
## Condicional Si-Entonces
```
Proceso sin_titulo
	
	Definir Numero1 como Entero;
	Escribir "Escribe un número entero";
	Leer Numero1;
	Escribir "La resta de ", Numero1, " entre 2 es ", Numero1%2;
	Escribir "Es par?";
	
	//Escribir Numero1%2 = 0;
	
	Si Numero1%2 = 0 Entonces
		Escribir Numero1, ' es par';
	FinSi
	
	Si Numero1%2 <> 0 Entonces
		Escribir Numero1, ' es impar';
	FinSi
	
FinProceso
```
## Condicional Si-Segun
```
Proceso sin_titulo
	Definir NumeroA, NumeroB, Operacion como Numericos;
	
	Escribir Sin Saltar "Escribe el número A";
	Leer NumeroA;
	
	Escribir Sin Saltar "Escribe el número B";
	Leer NumeroB;
	
	Escribir "Operaciones Disponibles";
	Escribir "1: Suma";
	Escribir "2: Resta";
	Escribir "3: Multiplicación";
	
	Escribir Sin Saltar "¿Qué operación queres ejecutar?";
	Escribir Sin Saltar "Escribe la letra en mayúscula o mínuscula";
	
	Leer Operacion;
	
	Segun Operacion Hacer
		1:
			// aqui la suma
			Escribir "Has elegido la suma";
			Escribir NumeroA, '+', NumeroB;
			Escribir NumeroA+NumeroB;
		2:
			// aqui la resta
			Escribir "Has elegido la resta";
			Escribir NumeroA, '-', NumeroB;
			Escribir NumeroA-NumeroB;
		3:
			// aqui la multiplicacion
			Escribir "Has elegido la multiplicación";
			Escribir NumeroA, '*', NumeroB;
			Escribir NumeroA*NumeroB;
		De Otro Modo:
			Escribir "No has elegido la operación correcta";
	FinSegun
	
FinProceso
```
