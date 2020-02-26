import Tarea_micros

def test_PrimeraFuncion():
    Result = Tarea_micros.PrimeraFuncion("mama")
    assert Result == "MAMA"
    
def test_SegundaFuncion():
    Result = Tarea_micros.SegundaFuncion("man")
    assert Result == "False"

def test_TerceraFuncion():
    Result = Tarea_micros.TerceraFuncion(5,4)
    assert Result == 1




def test_PrimeraFuncionError():
    Result = Tarea_micros.PrimeraFuncion("m2ama")
    assert Result == "Error 1"

def test_SegundaFuncionError():
    Result = Tarea_micros.SegundaFuncion("2wan")
    assert Result == "Error 1"

def test_TerceraFuncionError():
    Result = Tarea_micros.TerceraFuncion(3,4)
    assert Result == "Error 3"  
