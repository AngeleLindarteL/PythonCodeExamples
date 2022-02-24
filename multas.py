distanciaEP = int(input("Cuanto es la distancia entre el Punto A y el Punto B en KM: "))
limiteVelocidad = int(input("Cual es el límite de velocidad en KM/H: "))
tiempoRecorrido = int(input("Cuanto se demoro el carro en recorrer la distancia en HORAS: "))

kilometrosPorHora = distanciaEP / tiempoRecorrido

if kilometrosPorHora >= limiteVelocidad:
    print("Alto ahí rufian son 10,120,000")
else:
    print("Que gran ciudadano, nunca cambies, pte :D")

print("Fin del programa :D")