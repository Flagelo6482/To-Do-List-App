from datetime import datetime


class Tarea:
    ERROR_TEXTO = "El campo {} debe ser una palabra no vacía"
    ERROR_ESTADO = "Una tarea no puede estar en estado '{}' y '{}' simultáneamente"

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

        # Validamos los atributos en formato string/carácter
        for campo, valor in [
            ("nombre", nombre),
            ("apellido", apellido),
            ("asunto", asunto),
            ("descripcion", descripcion)
        ]:
            if not isinstance(valor, str) or not valor.strip():
                raise ValueError(self.ERROR_TEXTO.format(campo))
            setattr(self, campo, valor.strip())  # Asingación automática y dinámica

        # Validamos los estados boleanos
        if completado and terminado:
            raise ValueError(self.ERROR_ESTADO.format("completado", "terminado"))
        if proceso and terminado:
            raise ValueError(self.ERROR_ESTADO.format("proceso", "terminado"))
            # Validamos las fechas lógicas
        if fechaActualizacion != fechaActualizacion < fechaCreacion:
            raise ValueError("La fecha de actualización no puede ser anterior a la creación")
        if fechaEliminacion and not terminado:
            raise ValueError("No se puede eliminar una tarea no terminada")

        self.completado = completado
        self.proceso = proceso
        self.terminado = terminado
        self.fechaCreacion = fechaCreacion
        self.fechaActualizacion = fechaActualizacion
        self.fechaEliminacion = fechaEliminacion