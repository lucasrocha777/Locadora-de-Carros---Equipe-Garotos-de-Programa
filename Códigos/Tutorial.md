# Como executar o projeto 🚀

Este repositório contém versões compactadas do projeto em arquivos `.zip`. Abaixo estão instruções simples para descompactar e configurar corretamente o ambiente do projeto.

## 📦 Descompactando o arquivo ZIP

1. Baixe o arquivo `.zip` desejado do repositório.
2. Após baixar, localize o arquivo no seu computador.
3. Clique com o botão direito no arquivo `.zip` e escolha:
   - **Windows:** `Extrair Aqui` ou `Extract Here`.
   - **Linux/macOS:** Utilize o terminal:
     ```bash
     unzip nome_do_arquivo.zip
     ```

Após descompactar, você terá uma pasta contendo todos os arquivos do projeto.

## ⚙️ Criando o Ambiente Virtual (`venv`)

Para manter as dependências organizadas e isoladas, utilize um ambiente virtual.

### Abra o terminal dentro da pasta descompactada do projeto e execute:

```bash
# Criar ambiente virtual (venv)
python -m venv venv
```
# Ative o ambiente virtual:
- Windows (CMD):
```
venv\Scripts\activate.bat
```
- Windows (PowerShell):
```
.\venv\Scripts\Activate.ps1
```
- Linux/macOS:
```
source venv/bin/activate
```
Após ativar, você verá (venv) antes do prompt no terminal.

# 📌 Instalando as dependências (Flask e Flask_SQLAlchemy)
Agora, instale as bibliotecas necessárias para executar o projeto:
```
pip install flask flask_sqlalchemy
```
💡 Dica: Você pode verificar as dependências instaladas utilizando:
```
pip freeze
```

# 🚧 Executando o Projeto
Para executar o projeto, geralmente utilize:
```
python app.py
```
(Certifique-se de ajustar este comando para corresponder ao nome do arquivo principal do projeto.)

# 🎉 Pronto! Agora seu ambiente está configurado corretamente para executar o projeto localmente.
