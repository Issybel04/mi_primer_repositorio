from flask import Flask, render_template
from entidades.estudiante import Estudiante
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/estudiantes')
def estudiantes():
    # leer los estudaintes de la base de datos
    estudiantes = []
    with open('db/estudiantes.txt', 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            print(line)
            matricula, nombre, ap_paterno, ap_materno = line.split('|')
            estudiante = Estudiante(matricula, nombre, ap_paterno, ap_materno)
            estudiantes.append(estudiante)

    return render_template('estudiantes.html', data=estudiantes)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)