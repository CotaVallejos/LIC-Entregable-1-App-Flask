from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas inicial
tareas = ["Aprender Python", "Crear un entregable", "Practicar Flask"]

# Plantilla HTML
html_template = """
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>Lista de Tareas</title>
  </head>
  <body>
    <h1>Lista de Tareas</h1>
    <ul>
      {% for tarea in tareas %}
        <li>
            {{ tarea }}
            <a href="{{ url_for('eliminar', indice=loop.index0) }}">[Eliminar]</a>
            <a href="{{ url_for('editar', indice=loop.index0) }}">[Editar]</a>
        </li>
        {% endfor %}
    </ul>

    <h2>Añadir Tarea</h2>
    <form method="POST" action="{{ url_for('agregar') }}">
        <input type="text" name="tarea" required>
        <input type="submit" value="Agregar">
    </form>
    
    {% if editar_tarea is not none %}
    <h2>Editar Tarea</h2>
    <form method="POST" action="{{ url_for('actualizar', indice=indice_editar) }}">
        <input type="text" name="tarea" value="{{ editar_tarea }}" required>
        <input type="submit" value="Actualizar">
    </form>
    {% endif %}

  </body>
</html>
"""

# Ruta principal: mostrar tareas
@app.route("/")
def home():
    return render_template_string(html_template, tareas=tareas, editar_tarea=None)

# Agregar tarea
@app.route("/agregar", methods=["POST"])
def agregar():
    nueva = request.form["tarea"]  # obtenemos el valor del formulario
    tareas.append(nueva)            # agregamos la tarea a la lista
    return redirect(url_for("home"))  # volvemos a la página principal

# Eliminar tarea
@app.route("/eliminar/<int:indice>")
def eliminar(indice):
    if 0 <= indice < len(tareas):
        tareas.pop(indice)  # elimina la tarea de la lista
    return redirect(url_for("home"))

# Editar tarea, mostrar formulario con la tarea seleccionada
@app.route("/editar/<int:indice>")
def editar(indice):
    if 0 <= indice < len(tareas):
        return render_template_string(html_template, tareas=tareas, editar_tarea=tareas[indice], indice_editar=indice)
    return redirect(url_for("home"))

# Actualizar tarea
@app.route("/actualizar/<int:indice>", methods=["POST"]) # recibe el formulario y actualiza la tarea en la lista
def actualizar(indice):
    if 0 <= indice < len(tareas):
        tareas[indice] = request.form["tarea"]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
