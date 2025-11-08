from flask import Flask, request, jsonify
import pandas as pd
import pickle

# Carregar modelo e dataset
model = pickle.load(open("modelo.pkl", "rb"))
df = pd.read_csv("comandos.csv")

app = Flask(__name__)

@app.route("/")
def home():
    return "API de Navegação por Voz do HC está ativa!"

@app.route("/voz", methods=["POST"])
def voz():
    data = request.get_json()
    comando = data.get("comando", "").strip().lower()

    if not comando:
        return jsonify({"erro": "Comando vazio"}), 400

    # Predizer intenção
    pred_intencao = model.predict([comando])[0]

    # Buscar ação associada
    acao = df[df["intencao"] == pred_intencao]["acao"].iloc[0]

    return jsonify({
        "comando": comando,
        "intencao": pred_intencao,
        "acao": acao
    })

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

