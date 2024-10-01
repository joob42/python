Algoritmo juegos_o
	// Crear un algoritmo en diagrama de flujo para los JJOO
	// Que realice lo siguiente
	// Ingresar nombre del deportista hasta que ingrese el nombre x
	// Debe ingresar pais, edad, deporte, genero y puesto obtenido
	// pais (Chile, Argentina, Brasil, Estados Unidos, Jamaica, China y Espa?a)
	// Deporte (Futbol, Basquetbol, Voleybol, Tenis, Tiro al disco)
	// Responder lo sgt:
	// 1) Cuantas medallas de oro tiene chile
	// 2) Cuantas medallas suman las mujeres
	// 3) Cual es el deporte que tiene mas medallas de oro
	// 4) Cual es el pais que tiene mas medallas 
	// 5) Mostr el podium del Tenis masculino 
	// (Nombre y pais de los tenistas prremiados)
	// 6) Deportista mas joven en ganar oro
	// (Mostrar nombre, edad, deporte y pais)
	Escribir 'Bienvenido a los JJOO'
	Escribir ''
	cont_oro_1 <- 0
	cont_oro_2 <- 0
	cont_oro_3 <- 0
	cont_oro_4 <- 0
	cont_oro_chile <- 0
	cont_mujeres <- 0
	Escribir 'Ingrese su nombre'
	Leer nombre
	Mientras nombre<>'x' Hacer
		Repetir
			Escribir 'Ingrese edad'
			Leer e
		Hasta Que e>=15 Y e<=40
		Repetir
			Escribir 'Ingrese puesto obtenido'
			Leer pos
		Hasta Que pos>=1 Y pos<=30
		Repetir
			Escribir 'Ingrese pais'
			Escribir 'Ingrese 1 para CHILE'
			Escribir 'Ingrese 2 para ARGENTINA'
			Escribir 'Ingrese 3 para BRASIL'
			Escribir 'Ingrese 4 para Estados Unidos'
			Escribir 'Ingrese 5 para ESPA?A'
			Escribir 'Ingrese 6 para JAMAICA'
			Escribir 'Ingrese 7 para CHINA'
			Leer p
			Si p=1 Entonces
				cont_oro_chile <- cont_oro_chile+1
			FinSi
		Hasta Que p>=1 Y p<=7
		Repetir
			Escribir 'Deporte'
			Escribir '1. futbol'
			Escribir '2.Basquetbol'
			Escribir '3.Voleybol'
			Escribir '4.Tenis'
			Escribir '5.Tiro al disco'
			Leer dep
		Hasta Que dep>=1 O dep<=5
		Repetir
			Escribir 'Genero'
			Escribir 'M para mujeres'
			Escribir 'H para hombres'
			Leer g
			Si g= M Entonces
				cont_mujeres <- cont_mujeres+1
			FinSi
		Hasta Que g==M O g==H
		// fin de la vuelta
		Si pos==1 Entonces
			Si dep==1 Entonces
				cont_oro_1 <- cont_oro_1+1
			SiNo
				Si dep==2 Entonces
					cont_oro_2 <- cont_oro_2+1
				SiNo
					Si dep==3 Entonces
						cont_oro_3 <- cont_oro_3+1
					SiNo
						Si dep==4 Entonces
							cont_oro_4 <- cont_oro_4+1
						SiNo
							Si dep==5 Entonces
								cont_oro_5 <- cont_oro_5+1
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
		Si cont_oro_1>cont_max_oro Entonces
			cont_max_oro <- con_oro_1
			dep_mas_oro <- 'FUTBOL'
		SiNo
			Si cont_oro_2>cont_max_oro Entonces
				cont_max_oro <- cont_oro_2
				dep_max_oro <- 'BASQUETBOL'
			SiNo
				Si cont_oro_3>cont_oro_max Entonces
					cont_max_oro <- cont_oro_3
					dep_max_oro <- 'VOLEYBOL'
				SiNo
					Si cont_oro_4>cont_oro_max Entonces
						cont_max_oro <- cont_oro_4
						dep_max_oro <- 'TENIS'
					SiNo
						cont_max_oro <- cont_oro5
						dep_max_oro <- 'TIRO AL DISCO'
					FinSi
				FinSi
			FinSi
		FinSi
	FinMientras
	// RESPUESTAS
FinAlgoritmo
