
from mongoengine import connect
from odm.classes import Cliente
from odm.classes import Editora
from odm.classes import Livro

# conexão com o banco
connect(db='livraria', host='localhost', port=27017)

# Salvando documentos 
# - CREATE -

cliente= Cliente(
    nome="José",
    cpf=10435678967,
    end="Av.Caxangá, Recife - PE",
    tel=987654321
)

try:
   cliente.save()
   print("Cliente salvo")
except :
   print("cpf não é único")

editora= Editora(
        nome="Abril SA",
        end= "Av. Paulista",
        cnpj="25.660.700/1334-78",
        tel=32557880,
        nome_gerente="Marcos"
)
editora.save()
print("Editora salva")

# Salvar a editora antes de salvar um livro #

livro = Livro(
    título ="A Culpa é das estrelas",
    isbn ="754-51-72895-90-0",
    autor ="John Green",
    ano=2012,
)
livro.editora_ref = editora
livro.save()
print("Livro salvo")


# - READ -
clientes = Cliente.objects()
editoras = Editora.objects()
livros =   Livro.objects()

for cliente in clientes:
    print(cliente.nome, cliente.cpf, cliente.tel, cliente.end)

for editora in editoras:
    print(editora.nome, editora.cnpj, editora.end, editora.tel, editora.nome_gerente)

for livro in livros:
    print(livro.título,livro.autor,livro.ano,livro.isbn)


# - UPDATE -
clientes2 = Cliente.objects(id='602c4dfbef9bc938fc7bcb8b') # <-- indexes ou id
fields = {
       "nome": "José da Silva",
       "cpf": 10435678961
   }
clientes2.update(**fields)
print("Campo(s) atualizado(s)")

editoras2 = Editora.objects(id='602d3e47bc59fcfa15036d31')
fields = {
       "nome":"Cia. dos Livros",
   }
editoras2.update(**fields)
print("Campo(s) atualizado(s)")

livros2 = Livro.objects(id='602d80817d1caee03710cab8')
fields = {
    "nome": "Culpa Estrelas",
  }
livros2.update(**fields)
print("Campo(s) atualizado(s)")


# - DELETE -
c = Cliente.objects(id='602d4f614bbb9802ceeaaaa3') # <-- indexes ou id
c.delete()
print("Cliente deletado")

e = Editora.objects(id='602d3e47bc59fcfa15036d31')
e.delete()
print("Editora deletada")

l = Livro.objects(id='602d80817d1caee03710cab8')
l.delete()
print("Livro deletado")