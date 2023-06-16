try:#inicio de try por cualquier tipo de bug
        logpalabra=len(input("ingrese una palabra: "))#asignacion de variable con el valor numerico de la longitud de la palabra
        if logpalabra<=8 and logpalabra>=4 :#condicional if si es menor que 8 o mayor que 4
            print ("la palabra es correcta, tiene ", logpalabra, " letras")
        elif logpalabra<4:#condicional si es menor que cuatro
            print ("Me hacen falta letras, solo tiene ", logpalabra, " letras")
        elif logpalabra>8:#condicional si es mayor a 8
            print("A caray, aqui sobran letras, tenemos ", logpalabra, " letras")
except ValueError:
    print ("debe ingresar una plabra")#retorno del try invalido 


#inicio programa plano carteciano


try:#inicio de try por detectar cualquier mal entrada de teclado 
     x=float(input("POR FAVOR INGRESE LA COORDENADA X: "))
     y=float(input("POR FAVOR INGRESE LA COORDENADA Y: "))
     if x>=1 and y>=1: #condicional cuadrante 1 
        print("la coordenada ", x,",",y," se encuentra en el cuadrante 1")
     elif x<= -1 and y>=1: #condicional cuadrante 2
        print ("la coordenada ", x,",",y," se encuentra en el cuadrante 2")
     elif x<= -1 and y<= -1: #condicional cuadrante 3
         print ("la coordenada ", x,",", y, " se encuentra en el cuadrante 3")
     elif x<=1 and y>=-1: #condicional cuadrante 4
         print ("la coordenada ", x,",",y," se encuentra en el cuadrante 4 :D")   
     
except ValueError:#via que se toma por si existe algun error
     print("ERROR: no ingreso un valor correcto D:")