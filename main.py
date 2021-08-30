from Cliente import Cliente
from Loja import Loja

lojaRV = Loja("Rio Vermelho", 13)
diolan = Cliente("Diolan")
diolan.solicitaEmprestimo(lojaRV, 2, "Hora")
diolan.devolveBicicletas(lojaRV)
diolan.pagaEmprestimo(2000, lojaRV)

lojaBV = Loja("Boa Viagem", 18)
victor = Cliente("Victor")
victor.solicitaEmprestimo(lojaBV, 4, "Semana")
victor.devolveBicicletas(lojaBV)
# cliente.pagaEmprestimo(2000, lojaBV)

brian = Cliente("Brian")
brian.solicitaEmprestimo(lojaRV, 1, "Dia")
brian.devolveBicicletas(lojaRV)