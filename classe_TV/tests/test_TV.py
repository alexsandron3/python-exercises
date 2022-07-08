from src.TV import TV


def test_if_class_initialize_with_corrects_attrs():
    tv = TV(10)
    assert tv._volume == 50
    assert tv._canal == 1
    assert tv._tamanho == 10
    assert tv._ligada == False


def test_if_increase_volume_work_as_expected():
    tv = TV(10)
    tv.aumentar_volume()

    assert tv._volume == 51

    for _ in range(9):
        tv.aumentar_volume()

    assert tv._volume == 60

    for _ in range(500):
        tv.aumentar_volume()
    assert tv._volume == 99
