Algoritmo impar_par
	cont_par <- 0
	cont_primo <- 0
	cont_impar <- 0
	suma <- 0
	cont_num <- 0
	Repetir
		Escribir 'Ingrese un numero'
		Leer n
		Si n MOD 2=0 Entonces
			Escribir n, ' Es un numero par'
			cont_par <- cont_par+1
			cont_num <- cont_num+1
		SiNo
			Escribir n, ' No es un numero par'
			cont_impar <- cont_impar+1
			cont_num <- cont_num+1
		FinSi
		suma <- suma+n
	Hasta Que n=0
	// promediio
	promedio <- suma/cont_num
	// respuestas
	Escribir 'Cantidad de numeros pares: ', cont_par
	Escribir 'Cantidad de numeros impares: ', cont_impar
	Escribir 'El promedio es: ', promedio
FinAlgoritmo
