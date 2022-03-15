# importando bibiotecas
import mongoengine
from mongoengine import *
import json

# Definindo documentos - CREATE -

class Cliente (Document):
    nome = StringField(required=True)
    cpf = IntField(unique=True, required=True, max_length=12)
    end = StringField(required=True, max_length=100)
    tel = IntField(required=True, max_length=9)

    def json(self):
        cliente_dict = {
            "nome": self.nome,
            "cpf": self.cpf,
            "end": self.end,
            "tel": self.tel
        }
        return json.dumps(cliente_dict)
    meta = {
        "indexes": ["cpf"]
    }

class Editora (Document):
    nome = StringField(required=True)
    end = StringField(required=True, max_length=100)
    cnpj = StringField(required=True, max_length=20)
    tel = IntField(required=True, max_length=8)
    nome_gerente = StringField(required=True)

    def json(self):
        editora_dict = {
            "nome": self.nome,
            "end": self.end,
            "cnpj": self.cnpj,
            "tel": self.tel,
            "nome_gerente": self.nome_gerente,
        }
        return json.dumps(editora_dict)

    meta = {
        "indexes": ["nome","cnpj"]
    }

class Livro(DynamicDocument):
        título = StringField(required=True)
        isbn = StringField(unique=True,required=True)
        autor = StringField(required=True)
        ano = IntField(required=True)
        editora_ref = ReferenceField(Editora, reverse_delete_rule=CASCADE)

        meta = {
            "indexes": ["título", "isbn"]
        }


