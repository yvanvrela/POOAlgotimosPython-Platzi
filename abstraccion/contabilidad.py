
class Contabilidad:
    def __init__(self) -> None:
        pass

    def liquidacion_de_documentos(self, mes_presentacion: str):
        self._despachar_documentos(mes_presentacion)
        self._ordenar_documentos()
        self._cargar_documentos()
        self._resumir_montos_documentos()
        self._llenar_formulario_presentacion()
        self._presentar_documentos_hacienda()

    def _despachar_documentos(self, mes_presentacion):
        print(f'Despachando documentos de {mes_presentacion}')

    def _ordenar_documentos(self):
        print('Ordenando documentos')

    def _cargar_documentos(self):
        print('Cargando documentos')

    def _resumir_montos_documentos(self):
        print('Realizando resumen de montos de los documentos')

    def _llenar_formulario_presentacion(self):
        print('Llenando formulario de presentación')

    def _presentar_documentos_hacienda(self):
        print('Presentando formulario a hacienda')
