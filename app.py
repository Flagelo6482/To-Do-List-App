from flask import Flask, render_template
from models.models import Tarea

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    tarea1 = Tarea(
        nombre="Francisco",
        apellido="Sono Calla",
        asunto="Postulaciones semanales",
        descripcion="Enviar las postulaciones pendientes a Mildred esta semana"
    )
    print(f"Ultima actualización: {tarea1.fechaCreacion}")
    app.run(debug=True)