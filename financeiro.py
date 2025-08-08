from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Pessoa(db.Model):
    __tablename__ = 'pessoas'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    saldo = db.Column(db.Float, default=0.0)
    total_dividas = db.Column(db.Float, default=0.0)
    total_pagamentos = db.Column(db.Float, default=0.0)
    ultima_transacao = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamento com transações
    transacoes = db.relationship('Transacao', backref='pessoa_obj', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Pessoa {self.nome}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'saldo': self.saldo,
            'total_dividas': self.total_dividas,
            'total_pagamentos': self.total_pagamentos,
            'ultima_transacao': self.ultima_transacao.isoformat() if self.ultima_transacao else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class Transacao(db.Model):
    __tablename__ = 'transacoes'
    
    id = db.Column(db.Integer, primary_key=True)
    pessoa_nome = db.Column(db.String(100), db.ForeignKey('pessoas.nome'), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # 'divida' ou 'pagamento'
    descricao = db.Column(db.Text)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    timestamp = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Transacao {self.id}: {self.pessoa_nome} - {self.tipo} - R$ {self.valor}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'pessoa': self.pessoa_nome,
            'valor': self.valor,
            'tipo': self.tipo,
            'descricao': self.descricao,
            'data': self.data.isoformat() if self.data else None,
            'timestamp': self.timestamp,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

