from flask import Flask, request, jsonify

app = Flask(__name__)

# ============================================
# PÁGINA INICIAL
# ============================================
@app.route('/')
def home():
    return jsonify({
        "mensagem": "Train!fy Activity Provider - Sistema Ativo (Versão Teste Semana 1)",
        "aluno": "Filipe Ramos - 2501446",
        "versao": "1.0 - Olá Mundo",
        "endpoints": {
            "configuracao": "/api/configurar_treino [POST]",
            "visualizar": "/api/treino/teste [GET]",
            "analytics": "/api/analytics/teste [GET]"
        }
    })

# ============================================
# TESTE POST - Configuração de Treino
# ============================================
@app.route('/api/configurar_treino', methods=['POST'])
def configurar_treino():
    """
    Endpoint POST de teste - recebe parâmetros do treino
    e retorna confirmação (versão "Olá Mundo")
    """
    data = request.get_json()
    
    return jsonify({
        "status": "sucesso",
        "mensagem": "Olá Mundo! Pedido POST recebido com sucesso! ✅",
        "parametros_recebidos": {
            "nome_treino": data.get('nome_treino', 'não fornecido'),
            "foco_principal": data.get('foco_principal', 'não fornecido'),
            "tempo_estimado_minutos": data.get('tempo_estimado_minutos', 'não fornecido')
        },
        "nota": "Esta é a versão de teste da Semana 1"
    }), 200

# ============================================
# TESTE GET - Visualizar Treino
# ============================================
@app.route('/api/treino/teste', methods=['GET'])
def visualizar_treino_teste():
    """
    Endpoint GET de teste - retorna exemplo de treino
    (versão "Olá Mundo")
    """
    return jsonify({
        "mensagem": "Olá Mundo! Pedido GET recebido com sucesso! ✅",
        "atividade_id": "teste_123",
        "exemplo_treino": {
            "nome_treino": "Treino A - Peito/Tríceps (EXEMPLO)",
            "foco_principal": "hipertrofia",
            "instrucoes_gerais": "Realizar 10 minutos de cardio antes de começar",
            "tempo_estimado_minutos": 60,
            "plano_exercicios": [
                {
                    "exercicio": "Supino Plano",
                    "series_alvo": 3,
                    "repeticoes_alvo": "8-12",
                    "intensidade_alvo": "80kg"
                }
            ]
        },
        "nota": "Esta é a versão de teste da Semana 1"
    })

# ============================================
# TESTE GET - Analytics
# ============================================
@app.route('/api/analytics/teste', methods=['GET'])
def obter_analytics_teste():
    """
    Endpoint GET de teste - retorna exemplo de analytics
    (versão "Olá Mundo")
    """
    return jsonify({
        "mensagem": "Olá Mundo! Analytics GET recebido com sucesso! ✅",
        "atividade_id": "teste_123",
        "quantAnalytics": [
            {
                "name": "Tempo total de treino",
                "type": "float",
                "value": 55.5,
                "unit": "minutos"
            },
            {
                "name": "Taxa de conclusão do plano",
                "type": "float",
                "value": 90.0,
                "unit": "%"
            }
        ],
        "qualAnalytics": [
            {
                "name": "Feedback do cliente sobre a sessão",
                "type": "text/plain",
                "value": "Treino desafiante mas bom! (EXEMPLO)"
            }
        ],
        "nota": "Esta é a versão de teste da Semana 1"
    })

# ============================================
# EXECUÇÃO
# ============================================
if __name__ == '__main__':
    app.run(debug=True)