from flask import Flask, render_template

# Contruccion de la aplicacion
app = Flask(__name__)

# Rutas que tendra la aplicacion
@app.route('/')
def index():
    return render_template('index.html')


# Un debuggeador para que, cada vez que se realice cambios
# se actualize solo
if __name__ == "__main__":
    app.run(debug=True)
