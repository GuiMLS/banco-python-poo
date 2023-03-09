from abc import ABC, abstractmethod


class Conta: 
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    def saldo(self):
        pass

    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)


class ContaCorrente(Conta):
    def __init__(self, limite, limite_saques):
        self._limite = limite
        self.limite_saques = limite_saques


class Historico:
    def adicionar_tansacao(transacao):
        transacao.registrar()  # Transacao pode ser Deposito ou Saque
        return transacao


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        return conta


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        # ESCREVER AQUI A ROTINA DE DEPOSITO com seu devido return
        # return ?
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        # ESCREVER AQUI A ROTINA DE SAQUE com seu devido return
        # return ?
        pass


class Cliente:
    def __init__(self, endereco, contas):
        self._endereco = endereco
        self._contas = contas
    
    def realizar_transacao(conta, transacao):
        """Consulta o saldo do cliente especifico na classe Conta e passa
        como valor na funcao seguinte FETCH DO VALOR DE
        SALDO PARA AQUELE CLIENTE """
        # valor = saldo
        # transacao.registrar(valor)
        pass

    def adicionar_conta(conta):
        #
        pass
