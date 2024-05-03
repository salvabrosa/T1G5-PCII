from datafile import filename

from classes.fatura import Fatura
from classes.hotel import Hotel
from classes.quarto import Quarto
from classes.reservaquarto import ReservaQuarto
from classes.fatura_reserva import Fatura_Reserva


Fatura.read(filename + 'hotel.db')  
Hotel.read(filename + 'hotel.db')
Quarto.read(filename + 'hotel.db')
ReservaQuarto.read(filename + 'hotel.db')
Fatura_Reserva.read(filename + 'hotel.db')

cname = "Fatura"
cl = eval(cname)

obj = cl.from_string("Fat9;12/2/2024;eee")

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("Fat9;12/2/2024;eee")
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos onjetos gravados " ,cl.lst)


# alterar
obj = cl.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "WORD11"
Fatura.update(getattr(obj, cl.att[0]))

cl.read(filename + 'hotel.db')

print("\nobjectos gravados")    
for code in cl.lst:
    print(cl.obj[code])