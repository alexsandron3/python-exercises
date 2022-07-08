class TV:
    def __init__(self, tamanho):
        self._volume = 50
        self._canal = 1
        self._tamanho = tamanho
        self._ligada = False

    def aumentar_volume(self):
        if self._volume < 99:
            self._volume += 1

    def diminuir_volume(self):
        if self._volume > 0:
            self._volume -= 1
