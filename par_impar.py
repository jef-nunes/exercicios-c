class Escalas:
    @staticmethod
    def paresImpares(a:int,b:int):
        pares: int = 0
        impares: int = 0
        for i in range(a,b):
            if i%2 == 0:
                pares+= 1
            else:
                impares+= 1
        return pares,impares
