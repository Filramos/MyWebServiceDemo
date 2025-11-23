# Train!fy - Activity Provider
**Aluno:** Filipe Ramos - 2501446  
**Disciplina:** Arquitetura e Padrões de Software

## 🌐 URL do Web Service
https://mywebservicedemo-uxwl.onrender.com

## 📡 Endpoints Disponíveis (Semana 1 - Versão Teste)

### 1. Página Inicial
- **Método:** GET
- **URL:** `https://mywebservicedemo-uxwl.onrender.com/`
- **Descrição:** Verifica se o serviço está ativo

### 2. Visualizar Treino (Exemplo)
- **Método:** GET
- **URL:** `https://mywebservicedemo-uxwl.onrender.com/api/treino/teste`
- **Descrição:** Retorna exemplo de treino configurado

### 3. Analytics (Exemplo)
- **Método:** GET
- **URL:** `https://mywebservicedemo-uxwl.onrender.com/api/analytics/teste`
- **Descrição:** Retorna dados analíticos de exemplo

### 4. Configurar Treino
- **Método:** POST
- **URL:** `https://mywebservicedemo-uxwl.onrender.com/api/configurar_treino`
- **Headers:** `Content-Type: application/json`
- **Body (exemplo):**
```json
{
  "nome_treino": "Treino A - Peito/Tríceps",
  "foco_principal": "hipertrofia",
  "tempo_estimado_minutos": 60
}
```

## 📝 Parâmetros Suportados

Conforme especificação do projeto Train!fy:
- `nome_treino` (text/plain)
- `foco_principal` (text/plain): "hipertrofia", "forca_maxima", "resistencia", "mobilidade"
- `instrucoes_gerais` (text/plain) - opcional
- `tempo_estimado_minutos` (integer)
- `plano_exercicios_json` (text/plain) - opcional nesta versão

## ⚠️ Notas
- Esta é a versão "Olá Mundo" para a Semana 1
- O serviço está no plano gratuito do Render (pode hibernar após 15 min de inatividade)
- A primeira requisição pode demorar 30-60 segundos (reativação)
