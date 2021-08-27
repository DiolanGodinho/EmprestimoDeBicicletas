from Cliente import Cliente
from Loja import Loja

loja = Loja("Bikes", 13)
cliente = Cliente("Diolan")
cliente.solicitaEmprestimo(loja, 2, "Hora")
cliente.devolveBicicletas(loja)
cliente.pagaEmprestimo(2000, loja)