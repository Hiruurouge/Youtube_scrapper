import pytest
import main


pytest.my_symbol = main.scrap('https://youtu.be/fmsoym8I-3o')
def test_get_url():
    assert main.get_url('input.json')==['https://youtu.be/fmsoym8I-3o', 'https://youtu.be/JhWZWXvN_yo']
def test_scrap_title():
    assert pytest.my_symbol['title']=="Pierre Niney : L’interview face cachée par HugoDécrypte"
def test_scrap_description():
	assert pytest.my_symbol['description'][0:15]==" L'acteur Pierr"
def test_scrap_view():
	assert int(pytest.my_symbol['views']) >=735588
def test_scrap_id():
	assert pytest.my_symbol['id']=='fmsoym8I-3o'
def test_scrap_author():
	assert pytest.my_symbol['author']=='HugoDécrypte'
def test_scrap_likes():
    assert pytest.my_symbol['likes']=='30\xa0k'
def test_scrap_comm():
    assert pytest.my_symbol['comm'][0][0:15]=='Pensez à vous a'