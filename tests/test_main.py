import sys
import os

# Obtén la ruta al directorio del archivo actual (test_camel.py)
current_directory = os.path.dirname(__file__)

# Obtén la ruta al directorio raíz del proyecto (proyecto/)
project_root = os.path.abspath(os.path.join(current_directory, '..'))

# Agrega el directorio raíz del proyecto al PYTHONPATH
sys.path.insert(0, project_root)

from main import sumas

def test_sumas_with_positive_number():
    # Test with a positive number
    result = sumas(5)
    assert result == 15

def test_sumas_with_negative_number():
    # Test with a negative number
    result = sumas(-5)
    assert result == 5

def test_sumas_with_zero():
    # Test with zero
    result = sumas(0)
    assert result == 10