from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Sally', 'Brown') == 'Brown; Sally'
    assert make_full_name('Efraín', 'Gómez') == 'Gómez; Efraín'
    assert make_full_name('Daniel Alejandro', 'Ramirez Ramirez') == 'Ramirez Ramirez; Daniel Alejandro'

def test_extract_family_name():
    assert extract_family_name('Brown; Sally') == 'Brown'
    assert extract_family_name('Gómez; Efraín') == 'Gómez'
    assert extract_family_name('Ramirez Ramirez; Daniel Alejandro') == 'Ramirez Ramirez'

def test_extract_given_name():
    assert extract_given_name('Brown; Sally') == 'Sally'
    assert extract_given_name('Gómez; Efraín') == 'Efraín'
    assert extract_given_name('Ramirez Ramirez; Daniel Alejandro') == 'Daniel Alejandro'

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__]) 