def redondeo(numero):
    numero2=int(numero)
    if numero-numero2>=0.5:
        return numero2+1
    else:
        return numero2

