from flask import Flask, render_template
from entidades.estudiante import Estudiante
from entidades.materias import Materia
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/estudiantes')
def estudiantes():
    # leer los estudiantes de la base de datos
    estudiantes = []
    with open('db/estudiantes.txt', 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            print(line)
            matricula, nombre, ap_paterno, ap_materno = line.split('|')
            estudiante = Estudiante(matricula, nombre, ap_paterno, ap_materno)
            estudiantes.append(estudiante)

    return render_template('estudiantes.html', data=estudiantes)

@app.route('/materias')
def materias():
    # leer las materias de la base de datos
    lista_materias = []
    with open('db/materias.txt', 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            print(line)
            datos_materias = line.split('|')
            materias = Materia(datos_materias)
            lista_materias.append(materias)

    return render_template('materias.html', data=lista_materias)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
    