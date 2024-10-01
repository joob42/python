Algoritmo juegos_o
	Escribir 'Bienvenido a los JJOO'
	Escribir ''
	cont_oro_1 <- 0
	cont_oro_2 <- 0
	cont_oro_3 <- 0
	cont_oro_4 <- 0
	Escribir 'Ingrese su nombre'
	Leer nombre
	Mientras nombre!='x' Hacer
		Escribir 'Ingrese pais'
		Leer p
		Escribir 'Ingrese edad'
		Escribir e
		Escribir 'Ingrese puesto obtenido'
		Escribir pu
		Repetir
			Escribir 'Deporte'
			Escribir '1. futbol'
			Escribir '2.Basquetbol'
			Escribir '3.Voleybol'
			Escribir '4.Tenis'
			Escribir '5.Tiro al disco'
			Leer dep
		Hasta Que dep>=1 O dep<=5
		Si pos==1 Entonces
			Si dep==1 Entonces
				cont_oro_1 = cont_oro_1 + 1
			SiNo
				Si dep==2 Entonces
					cont_oro_2 = cont_oro_2+1
				SiNo
					Si dep==3 Entonces
						cont_oro_3 = cont_oro_3+1
					SiNo
						Si dep==4 Entonces
							cont_oro_4 = cont_oro_4+1
						SiNo
							Si dep==5 Entonces
								cont_oro_5 = cont_oro_5+1
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
		Repetir
			Escribir 'Genero'
			Escribir 'M para mujeres'
			Escribir 'H para hombres'
			Leer g
		Hasta Que g==M O g==H
	FinMientras
FinAlgoritmo

