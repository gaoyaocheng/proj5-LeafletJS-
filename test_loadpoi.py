from load_poi import Poi

def test_load():
    file  = 'data/poi.txt'
    assert Poi(file)
    assert isinstance(Poi(file).as_list(), list)
