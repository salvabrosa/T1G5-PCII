from classes.gclass import Gclass
from classes.hotel import Hotel
from classes.tiposquarto import TiposQuarto
import datetime

class Quarto(Gclass):
    obj = dict()
    lst =list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_codigo','_cod_hotel','_preco_noite','_tipoquarto','_estado_reserva']
    header = 'Quarto'
    des = ['Codigo do quarto','Codigo do hotel','_tipoquarto','Estado da reserva']
    
    def __init__(self, codigo, cod_hotel, preco_noite, tipoquarto,  estado_reserva):
        super().__init__()
        
        if cod_hotel in Hotel.lst:
            if tipoquarto in TiposQuarto.lst:
            
                self._codigo = codigo
                self._cod_hotel = cod_hotel
                self._preco_noite = preco_noite
                self._tipoquarto = tipoquarto
                self._estado_reserva=estado_reserva
        
                Quarto.obj[codigo] = self
                Quarto.lst.append(codigo)
            else:
                print('Tipos ', tipoquarto, ' not found')
        else:
            print('Hotel ', cod_hotel, ' not found')
            
    @property 
    def codigo(self):
        return self._codigo
    @property 
    def cod_hotel(self):
        return self._cod_hotel
    @property 
    def preco_noite(self):
        return self._preco_noite
    @property
    def tipoquarto(self):
        return self._tipoquarto
    @property 
    def estado_reserva(self):
        return self._estado_reserva
    
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
    @cod_hotel.setter
    def cod_hotel(self, cod_hotel):
        if cod_hotel in Hotel.lst:
            self._cod_hotel = cod_hotel
        else:
            print('Hotel ', cod_hotel, ' not found')
    @preco_noite.setter 
    def preco_noite(self, preco_noite):
        self._preco_noite = preco_noite
    @tipoquarto.setter
    def tipoquarto(self, tipoquarto):
        if tipoquarto in TiposQuarto.lst:
            self._tipoquarto = tipoquarto
        else:
            print('Tipos ', tipoquarto, ' not found')
    @estado_reserva.setter 
    def estado_reserva(self, estado_reserva):
        self._estado_reserva = estado_reserva