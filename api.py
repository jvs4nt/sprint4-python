from flask import Flask, jsonify, request
import oracledb
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

def conecta_BD():
    try:
        dnStr = oracledb.makedsn("oracle.fiap.com.br", "1521", "ORCL")
        conn = oracledb.connect(user="rm554328", password="fiap24", dsn=dnStr)
        inst_SQL = conn.cursor()
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
        inst_SQL = None
        conn = None
    else:
        print("Conexão bem-sucedida ao banco de dados.")
    return conn, inst_SQL

def executar_consulta(inst_SQL, query):
    try:
        inst_SQL.execute(query)
        dados = inst_SQL.fetchall()
        colunas = [col[0] for col in inst_SQL.description]
        return dados, colunas
    except Exception as e:
        return None, str(e)

@app.route('/')
def home():
    return 'API de Consulta ao Banco de Dados Oracle'

@app.route('/clientes', methods=['GET'])
def consulta_clientes():
    conn, inst_SQL = conecta_BD()
    if conn is None:
        return jsonify({"error": "Erro ao conectar ao banco de dados."}), 500

    query = "SELECT * FROM clientes"
    dados, colunas = executar_consulta(inst_SQL, query)

    if dados is None:
        return jsonify({"error": colunas}), 500

    resultados = [dict(zip(colunas, linha)) for linha in dados]
    return jsonify(resultados)

@app.route('/funcionarios', methods=['GET'])
def consulta_funcionarios():
    conn, inst_SQL = conecta_BD()
    if conn is None:
        return jsonify({"error": "Erro ao conectar ao banco de dados."}), 500

    query = "SELECT * FROM funcionarios"
    dados, colunas = executar_consulta(inst_SQL, query)

    if dados is None:
        return jsonify({"error": colunas}), 500

    resultados = [dict(zip(colunas, linha)) for linha in dados]
    return jsonify(resultados)

@app.route('/chatbots', methods=['GET'])
def consulta_chatbots():
    conn, inst_SQL = conecta_BD()
    if conn is None:
        return jsonify({"error": "Erro ao conectar ao banco de dados."}), 500

    query = "SELECT * FROM chatbots"
    dados, colunas = executar_consulta(inst_SQL, query)

    if dados is None:
        return jsonify({"error": colunas}), 500

    resultados = [dict(zip(colunas, linha)) for linha in dados]
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
