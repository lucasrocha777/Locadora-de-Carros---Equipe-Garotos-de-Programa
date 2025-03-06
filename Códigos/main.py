from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from classes import Locadora, Cliente, Carro, Moto

app = Flask(__name__)
app.secret_key = "chave_secreta"  # Necessário para exibir mensagens flash

# Criando a locadora
locadora = Locadora("Midnight Car Rent", "12.345.678/0001-99", "Rua das Locações, 123")

# Adicionando veículos
carro1 = Carro("Toyota", "Corolla", "ABC-1234", 2022, "Prata", "Disponível", 150, "OK", 4)
carro2 = Carro("Jeep", "Renegade", "XYZ-5678", 2023, "Vermelho", "Disponível", 180, "OK", 4)
moto1 = Moto("Honda", "CB500", "DEF-9012", 2021, "Preta", "Disponível", 90, "OK", 500, True)

locadora.veiculos_disponiveis.extend([carro1, carro2, moto1])

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para listar veículos
@app.route('/veiculos')
def listar_veiculos():
    locadora.devolver_veiculo()  # Atualiza a lista de veículos disponíveis
    veiculos = locadora.listar_veiculos_disponiveis()
    return render_template('veiculos.html', veiculos=veiculos)

# Rota para reservar veículos
@app.route('/reserva', methods=['GET', 'POST'])
def reservar_veiculo():
    if request.method == 'POST':
        cliente_index = int(request.form['cliente'])
        veiculo_index = int(request.form['veiculo'])
        data_inicio = datetime.strptime(request.form['data_inicio'], "%Y-%m-%d").date()
        data_fim = datetime.strptime(request.form['data_fim'], "%Y-%m-%d").date()

        if data_inicio >= data_fim:
            flash("Erro: A data de fim deve ser posterior à data de início.", "danger")
            return redirect(url_for('reservar_veiculo'))

        cliente = locadora.lista_clientes[cliente_index]
        veiculo = locadora.veiculos_disponiveis[veiculo_index]

        try:
            reserva = locadora.reservar_veiculo(cliente, veiculo, data_inicio, data_fim)
            flash(f"Reserva realizada: {veiculo.descricao()} de {data_inicio} a {data_fim}. Valor: R$ {reserva.valor_total:.2f}", "success")
        except ValueError:
            flash("Erro: Veículo não está disponível.", "danger")

        return redirect(url_for('listar_veiculos'))

    return render_template('reserva.html', clientes=locadora.lista_clientes, veiculos=locadora.veiculos_disponiveis)

# Rota para o histórico de aluguéis
@app.route('/historico/<int:cliente_id>')
def ver_historico(cliente_id):
    cliente = locadora.lista_clientes[cliente_id]
    return render_template('historico.html', cliente=cliente, historico=cliente.historico_alugueis)

# Rota para a página "Sobre"
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota para o cadastro de clientes
@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']
        novo_cliente = Cliente(nome, cpf)
        novo_cliente.email = email  # Adicionando email ao cliente
        novo_cliente.telefone = telefone  # Adicionando telefone ao cliente
        locadora.lista_clientes.append(novo_cliente)
        flash(f"Cliente {nome} cadastrado com sucesso!", "success")
        return redirect(url_for('home'))
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)