from pickle import FALSE
from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    braz = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    print('braz', braz[0])
    print('braz222', braz[0].get('titulo'))
    # assert braz[0].get('titulo') == 'Maquinista'
    assert braz[0].get('title', 'key not found') == 'Maquinista'
