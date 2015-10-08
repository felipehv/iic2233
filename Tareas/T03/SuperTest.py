import pytest
from jugador import *
from main import *
from ataques import *
from classes import *

class Test:
    
    def test_verificar_opcion_menu_true(cls):
        juego = Juego()
        assert juego.verificar_opcion('1')
        
    def test_verificar_opcion_menu_true2(cls):
    	juego = Juego()
    	assert juego.verificar.opcion(' 12  ')

    def test_verificar_opcion_menu_false(cls):
    	juego = Juego()
    	assert juego.verificar.opcion(' veinte')
        
    
