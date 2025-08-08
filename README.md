# 💰 Gerenciador Financeiro com Banco de Dados

## 🎯 Sobre o Projeto

Este é um gerenciador financeiro completo que permite controlar dívidas e recebimentos com **persistência total dos dados** através de um banco de dados SQLite. A aplicação foi desenvolvida com Flask (backend) e HTML/CSS/JavaScript (frontend).

## ✨ Principais Funcionalidades

### 🔐 **Sistema de Segurança**
- **Senha de acesso:** `Matheus2025`
- Tela de login protegida
- Botão de logout seguro

### 💾 **Persistência de Dados**
- **Banco de dados SQLite** para armazenamento permanente
- **Dados nunca se perdem** ao fechar o aplicativo
- **Backup e restauração** manual disponível
- **Indicador de status** da conexão (Online/Offline)

### 📊 **Funcionalidades Principais**
- ✅ **Registro de transações** (valores + e -)
- ✅ **Cálculo automático de saldos**
- ✅ **Gestão de pessoas** (devedores/credores)
- ✅ **Histórico completo** de transações
- ✅ **Relatórios financeiros** detalhados
- ✅ **Sistema de busca e filtros**
- ✅ **Edição e exclusão** com confirmação
- ✅ **Quitação automática** de pessoas
- ✅ **Interface responsiva** (mobile e desktop)

## 🚀 Como Executar

### 1. **Pré-requisitos**
- Python 3.11+
- Ambiente virtual (venv)

### 2. **Instalação**
```bash
# Navegar para o diretório do projeto
cd gerenciador_financeiro_backend

# Ativar o ambiente virtual
source venv/bin/activate

# Instalar dependências (já incluídas)
pip install -r requirements.txt
```

### 3. **Executar a Aplicação**
```bash
# Iniciar o servidor Flask
python src/main.py
```

### 4. **Acessar a Aplicação**
- Abra o navegador em: `http://localhost:5000`
- Digite a senha: `Matheus2025`
- Comece a usar!

## 📱 Como Usar

### **Registrar Transações**
1. Na aba "Nova", preencha:
   - **Nome da pessoa**
   - **Valor:** Use `-80` para dívidas, `+100` para pagamentos
   - **Descrição** (opcional)
2. Clique em "Registrar Transação"

### **Exemplos Práticos**
- `João Silva -150` → "João te deve R$ 150"
- `João Silva +50` → "João pagou R$ 50 (ainda deve R$ 100)"
- `Ana -80` → "Ana te deve R$ 80"

### **Gerenciar Pessoas**
- **Aba Pessoas:** Visualize todos os saldos
- **Quitar:** Zera o saldo de uma pessoa
- **Excluir:** Remove pessoa e todas suas transações

### **Relatórios e Histórico**
- **Aba Relatório:** Estatísticas e resumos financeiros
- **Aba Histórico:** Todas as transações com opções de editar/excluir

## 🗄️ Estrutura do Banco de Dados

### **Tabela: pessoas**
- `id` - Identificador único
- `nome` - Nome da pessoa
- `saldo` - Saldo atual (+ = te deve, - = você deve)
- `total_dividas` - Total emprestado
- `total_pagamentos` - Total recebido
- `ultima_transacao` - Data da última movimentação

### **Tabela: transacoes**
- `id` - Identificador único
- `pessoa_nome` - Nome da pessoa (chave estrangeira)
- `valor` - Valor da transação
- `tipo` - 'divida' ou 'pagamento'
- `descricao` - Descrição da transação
- `data` - Data e hora da transação

## 🔒 Backup e Segurança

### **Backup Automático**
- Dados salvos automaticamente no banco SQLite
- Arquivo do banco: `src/database/app.db`

### **Backup Manual**
1. Na aba "Relatório", clique em "Fazer Backup"
2. Arquivo JSON será baixado automaticamente
3. Para restaurar: "Restaurar Backup" → selecionar arquivo

### **Proteções Implementadas**
- ✅ Confirmação dupla para exclusões
- ✅ Validação de dados de entrada
- ✅ Tratamento de erros da API
- ✅ Indicador de status da conexão

## 🛠️ Tecnologias Utilizadas

### **Backend**
- **Flask** - Framework web Python
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados embutido

### **Frontend**
- **HTML5/CSS3** - Interface responsiva
- **JavaScript** - Interatividade e comunicação com API
- **Fetch API** - Requisições HTTP

## 📁 Estrutura do Projeto

```
gerenciador_financeiro_backend/
├── src/
│   ├── models/
│   │   └── financeiro.py      # Modelos do banco de dados
│   ├── routes/
│   │   └── financeiro.py      # Rotas da API
│   ├── static/
│   │   └── index.html         # Frontend da aplicação
│   ├── database/
│   │   └── app.db            # Banco de dados SQLite
│   └── main.py               # Arquivo principal
├── venv/                     # Ambiente virtual
├── requirements.txt          # Dependências Python
└── README.md                # Esta documentação
```

## 🔧 API Endpoints

### **Pessoas**
- `GET /api/pessoas` - Listar todas as pessoas
- `DELETE /api/pessoa/<nome>` - Excluir pessoa
- `POST /api/pessoa/<nome>/quitar` - Quitar pessoa

### **Transações**
- `GET /api/transacoes` - Listar transações
- `POST /api/transacao` - Criar transação
- `PUT /api/transacao/<id>` - Atualizar transação
- `DELETE /api/transacao/<id>` - Excluir transação

### **Dados Gerais**
- `GET /api/dados` - Obter todos os dados
- `POST /api/dados` - Restaurar backup
- `DELETE /api/limpar` - Limpar todos os dados

## 🎨 Características da Interface

### **Design Responsivo**
- ✅ Funciona em desktop e mobile
- ✅ Interface moderna com gradientes
- ✅ Animações suaves
- ✅ Cores intuitivas (vermelho = dívida, verde = pagamento)

### **Experiência do Usuário**
- ✅ Feedback visual para todas as ações
- ✅ Confirmações para ações destrutivas
- ✅ Loading indicators
- ✅ Mensagens de erro e sucesso
- ✅ Busca e filtros em tempo real

## 🔄 Vantagens do Banco de Dados

### **Antes (localStorage)**
- ❌ Dados perdidos ao limpar navegador
- ❌ Não funciona em modo privado
- ❌ Limitado a um navegador
- ❌ Sem backup automático

### **Agora (SQLite + Flask)**
- ✅ **Dados permanentes** no servidor
- ✅ **Funciona em qualquer navegador**
- ✅ **Backup automático** do banco
- ✅ **Múltiplos usuários** (com senha)
- ✅ **Escalável** para futuras funcionalidades

## 🚀 Próximas Melhorias Possíveis

- 📊 Gráficos e estatísticas avançadas
- 📧 Notificações por email
- 👥 Sistema multi-usuário
- 📱 App mobile nativo
- 🔄 Sincronização em nuvem
- 💳 Integração com bancos

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique se o servidor Flask está rodando
2. Confirme que a porta 5000 está disponível
3. Verifique o indicador de status (🟢 Online / 🔴 Offline)
4. Em caso de erro, recarregue a página

---

**Desenvolvido com ❤️ para garantir que seus dados financeiros nunca se percam!**

