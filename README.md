# Selenium-Python-2023
ALGUNOS DE LOS PASOS QUE FUI HACIENDO EN EL CURSO:

-Verificar que se tiene instalado python y el pip:

                                                  -> python --version

                                                  -> pip --version o pip list (contiene las librerias)
-Instalar  -> pip install selenium

-Instalar  -> pip install pytest

-Instalar  -> pip install allure-behave (para leer reportes)

-Instalar  -> pip install behave (para los test BDD)

-Instalar  -> pip install allure-pytest (para leer reportes)

-Instalar  -> pip install pillow (para insertar imagenes reportes)

-Instalar  -> pip install unittest-xml-reporting (para insertar imagenes reportes .xml)

-pip freeze  > requirements.txt  (es para saber q librerias se instaló en ese momento por las dudas q haya alguna actualizacion)

-Instalar selenium -> pip install virtualenv (para despues crear un entorno virtual)
-python -m virtualenv enviroment (para crear entorno)

-cuando se quiera usar las librerias  -> pip install -r .\requirements.txt

-Se elige como IDE -> pycharm
-primer test creado -> unitest-> tst_001_py.py
-UNit testing : *se trata de un método para determinar si un módulo o conj de móduloa funciona correctamente. Por lo general lo hace el desarrollador, nosotros evaluamos que el resultado esta bien o esta mal
                *Assertion (assert): es similar a lanzar una excepción si una condición dada no es verdadera
-libreria pytest -> para correr por consola te posicionas donde está el proyecto 
                    y luego ejacutar esto:  ej: python -m pytest .\test_002.py
                 -> para correr por consola lotes de test, se hace: te posicionas donde está el proyecto 
                    y luego ejacutar esto:  ej: python -m pytest .\test_002.py, .\tst_001.py 
                 -> para guardar loas corridas en un reporte, colocar en la consola: python -m pytest .\test_002.py, .\tst_001_py.py --junitxml=results.xml