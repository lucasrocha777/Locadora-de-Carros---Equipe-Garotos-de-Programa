from datetime import datetime

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

    def descricao(self):
        return f"{self.tipo} {self.marca} {self.modelo} ({self.ano})"

    def esta_disponivel(self):
        return self.status == "Disponível"

class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cor, status, valor_aluguel, documentacao, cilindradas, bau):
        super().__init__('moto', marca, modelo, placa, ano, cor, status, valor_aluguel, documentacao)
        self.cilindradas = cilindradas
        self.bau = bau
    
    def calcular_aluguel(self, dias):
        return (self.valor_aluguel * dias) * 0.9  # 10% de desconto para motos

class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cor, status, valor_aluguel, documentacao, portas):
        super().__init__('carro', marca, modelo, placa, ano, cor, status, valor_aluguel, documentacao)
        self.portas = portas
        
    
    def calcular_aluguel(self, dias):
        taxa = 1.1 if self.tipo == 'SUV' else 1.0  # SUVs têm 10% de taxa extra
        return (self.valor_aluguel * dias) * taxa

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.email = None  # Adicionando campo email
        self.telefone = None  # Adicionando campo telefone
        self.historico_alugueis = []

class Reserva:
    def __init__(self, cliente, veiculo, data_inicio, data_fim):
        self.cliente = cliente
        self.veiculo = veiculo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = 'Ativa'
        self.valor_total = self.veiculo.calcular_aluguel(self.calcular_duracao())

    def calcular_duracao(self):
        return (self.data_fim - self.data_inicio).days

    def finalizar_reserva(self):
        self.status = 'Finalizada'

class Locadora:
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.veiculos_disponiveis = []
        self.lista_clientes = []
        self.reservas_ativas = []

    def listar_veiculos_disponiveis(self):
        """Retorna a lista de veículos disponíveis"""
        return [veiculo for veiculo in self.veiculos_disponiveis if veiculo.esta_disponivel()]

    def reservar_veiculo(self, cliente, veiculo, data_inicio, data_fim):
        """Reserva um veículo para um cliente"""
        if not veiculo.esta_disponivel():
            raise ValueError("Veículo não disponível para reserva.")
        
        reserva = Reserva(cliente, veiculo, data_inicio, data_fim)
        self.veiculos_disponiveis.remove(veiculo)
        self.reservas_ativas.append(reserva)
        cliente.historico_alugueis.append(reserva)
        veiculo.status = "Reservado"  # Atualiza o status do veículo
        return reserva

    def devolver_veiculo(self):
        """Verifica se alguma reserva foi finalizada e devolve os veículos ao estoque."""
        hoje = datetime.today().date()
        for reserva in self.reservas_ativas:
            if reserva.data_fim <= hoje and reserva.status == 'Ativa':
                reserva.finalizar_reserva()
                self.veiculos_disponiveis.append(reserva.veiculo)
                reserva.veiculo.status = "Disponível"
                print(f"\n{reserva.veiculo.modelo} foi devolvido à locadora.")