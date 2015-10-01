from main import *
import pytest


class TestSistema():

    def setup_method(cls, method):
        cls.base = Base()
        cls.ramos = list()
        cls.alumno = Alumno(cls.base, 0, "Felipe")

        cls.alumno.tomar_ramo("ICS3902")  # 30 creditos
        cls.alumno.tomar_ramo("ICT2213")  # 10 creditos quedan 10

    def test_vacantes(cls):
        cls.base.db[0].vacantes = 0
        sigla = cls.base.db[0].sigla
        assert not cls.base.inscribir(sigla, cls.alumno)

    def test_vacantes2(cls):
        cls.base.db[0].vacantes = 19
        sigla = cls.base.db[0].sigla
        assert cls.base.inscribir(sigla, cls.alumno)

    def test_tomar_repetido(cls):
        assert not cls.alumno.tomar_ramo("ICT2213")

    def test_tomar_exceso_creditos(cls):
        assert not cls.alumno.tomar_ramo("ICT3442")  # False por creditos

    def test_tomar_repeticion_creditos(cls):
        # Falla por repeticion y creditos
        assert not cls.alumno.tomar_ramo("ICS3902")

    def test_tomar_true(cls):
        assert cls.alumno.tomar_ramo("ICS2523")  # Pasa

    def test_botar_ramo_no_tomado(cls):
        # False porque no esta tomado
        assert not cls.alumno.botar_ramo("ICT3352")

    def test_botar_ramo_tomado(cls):
        # Pasa porque el ramo esta tomado
        assert cls.alumno.botar_ramo("ICS3902")

    def test_botar_ramo_botado(cls):
        cls.alumno.botar_ramo("ICS3902")
        assert not cls.alumno.botar_ramo("ICS3902")  # Ya se boto el ramo

    def test_creditos(cls):
        cls.alumno.botar_ramo("ICS3902")
        for ramodb in cls.base.db:
            if ramodb.sigla == "ICS3902":
                ramo = ramodb
                break
        assert ramo.vacantes == 30

    def test_repeticion_repetido(cls):
        cls.alumno.agregar_ramo("ICS3902")  # Forzamos la toma de un ramo
        assert not cls.alumno.chequear_repeticion(
            "ICS3902")  # EL ramo esta dos veces ya

    def test_repeticion_no_repetido(cls):
        assert cls.alumno.chequear_repeticion(
            "IIC2233")  # El ramo no esta

if __name__ == "__main__":
    pass
