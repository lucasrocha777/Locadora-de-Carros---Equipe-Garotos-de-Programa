class Locadora:
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.veiculos_disponiveis = []
        self.lista_clientes = []
        self.funcionarios = []

    def listar_veiculos_disponiveis(self):
        return [veiculo.modelo for veiculo in self.veiculos_disponiveis]

    def reservar_veiculo(self, cliente, veiculo, data_inicio, data_fim):
        if veiculo not in self.veiculos_disponiveis:
            raise ValueError("Veículo não disponível para reserva.")
        reserva = Reserva(cliente, veiculo, data_inicio, data_fim)
        self.veiculos_disponiveis.remove(veiculo)
        return reserva

class Funcionario:
    def __init__(self, id_func, nome, cpf, cargo):
        self.id_func = id_func
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo

    def cadastrar_cliente(self, locadora, cliente):
        locadora.lista_clientes.append(cliente)
    
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.historico_alugueis = []
    
    def alugar_veiculo(self, veiculo, locadora):
        if veiculo not in locadora.veiculos_disponiveis:
            raise ValueError("Veículo não disponível para aluguel.")
        locadora.veiculos_disponiveis.remove(veiculo)
        self.historico_alugueis.append(veiculo)

class Veiculo:
    def __init__(self, tipo, marca, modelo, placa, ano, cor, status, valor_aluguel, documentacao):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.status = status
        self.valor_aluguel = valor_aluguel
        self.documentacao = documentacao
    
    def calcular_aluguel(self, dias):
        if dias <= 0:
            raise ValueError("O número de dias deve ser positivo.")
        return self.valor_aluguel * dias
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cor, status, valor_aluguel, documentacao, cilindradas, bau):
        super().__init__('Moto', marca, modelo, placa, ano, cor, status, valor_aluguel, documentacao)
        self.cilindradas = cilindradas
        self.bau = bau
    
    def calcular_aluguel(self, dias):
        if dias <= 0:
            raise ValueError("O número de dias deve ser positivo.")
        return (self.valor_aluguel * dias) * 0.9  

class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cor, status, valor_aluguel, documentacao, portas, tipo):
        super().__init__('Carro', marca, modelo, placa, ano, cor, status, valor_aluguel, documentacao)
        self.portas = portas
        self.tipo = tipo
    
    def calcular_aluguel(self, dias):
        if dias <= 0:
            raise ValueError("O número de dias deve ser positivo.")
        taxa = 1.1 if self.tipo == 'Relampago_Marquinhos' else 1.0  
        return (self.valor_aluguel * dias) * taxa
    
class Reserva:
    def __init__(self, cliente, veiculo, data_inicio, data_fim):
        self.id = id(self)
        self.cliente = cliente
        self.veiculo = veiculo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = 'Pendente'
        self.valor_total = self.veiculo.calcular_aluguel(self.calcular_duracao())
    
    def confirmar_reserva(self):
        self.status = 'Confirmada'
    
    def cancelar_reserva(self):
        self.status = 'Cancelada'
    
    def calcular_duracao(self):
        return (self.data_fim - self.data_inicio).days
