from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, Flask está funcionando! 🚀"

if __name__ == "__main__":
    app.run(debug=True)

# GET Para pedir información, ej. ver una página
@app.route('/datos', methods=['GET'])
def obtener_datos():
    return "Esto es un GET"

# POST Para enviar info, ej. cuando mandas datos desde un formulario
@app.route('/enviar', methods=['POST'])
def enviar_datos():
    return "Esto es un POST"

# Ruta dinámica, recibe variables en la URL, ej. como un buzón que recibe cartas con distintos nombres
@app.route('/hola/<nombre>')
def saludar(nombre):
    return f"¡Hola, {nombre}!"
