from datetime import datetime

#Clase para el modelo de la Tarea para crear una "tarea"
class Tarea:
    def __init__(self,
                 nombre: str,
                 apellido: str,
                 asunto: str,
                 descripcion: str,
                 completado: bool = False,
                 proceso: bool = False,
                 terminado: bool = False,
                 fechaCreacion: datetime = datetime.now(),
                 fechaActualizacion: datetime = None,
                 fechaEliminacion: datetime = None
                 ):
        self.nombre = nombre
        self.apellido = apellido
        self.asunto = asunto
        self.descripcion = descripcion
        self.completado = completado
        self.proceso = proceso
        self.terminado = terminado
        self.fechaCreacion = fechaCreacion
        self.fechaActualizacion = fechaActualizacion
        self.fechaEliminacion = fechaEliminacion