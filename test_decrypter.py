import pytest
from decrypter import cypher_decryption

def test_cypher_decryption_with_no_input():
    with pytest.raises(ValueError, match="No user input provided"):
        cypher_decryption()

def test_cypher_decryption_with_single_string():
    results = cypher_decryption("NGVVE")
    assert results == "'NGVVE' decrypts to 'happy' with '6' as the encryption key"
    
def test_cypher_decryption_with_multiple_strings():
    results = cypher_decryption("Uy tmbbk zai")
    assert results == "'Uy tmbbk zai' decrypts to 'im happy now' with '12' as the encryption key"
 
@pytest.mark.parametrize("encrypted_string, results", [
    (("+@NGV()+V3E"), "'+@NGV()+V3E' decrypts to 'happy' with '6' as the encryption key"),
    (("U3y () @t!!@mbbk za&i"), "'U3y () @t!!@mbbk za&i' decrypts to 'im happy now' with '12' as the encryption key")
]) 
   
def test_cypher_decryption_with_special_characters(encrypted_string, results):
    assert cypher_decryption(encrypted_string) == results
    
def test_cypher_decryption_with_non_string_input():
    with pytest.raises(TypeError, match="User input should be text"):
        cypher_decryption(123)