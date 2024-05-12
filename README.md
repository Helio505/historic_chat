# Historic Chat

## Descrição

Converse com personalidades históricas importantes e aprenda mais sobre a história de uma forma divertida e interativa.

## Instalação e Execução

1. Verifique se atende aos requerimentos:

- Python instalado (utilizei 3.12.2 e Windows 11)
- Pip instalado
- Git instalado
- Google API Key
- Conexão com a internet

2. Clone o repositório:

```bash
git clone https://github.com/Helio505/historic_chat.git
```

3. Entre na pasta do projeto:

```bash
cd historic_chat
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Crie um arquivo `.env` na raiz do projeto e adicione a sua Google API Key:

```
GEMINI_API_KEY="YOUR_API_KEY"
```

6. Execute o arquivo `main.py`:

```bash
python main.py
```

## Uso

![alt text](<assets/Animação Historic Chat.gif>)

1. Para iniciar o chat, basta executar o arquivo `main.py` e seguir as instruções.
2. Para enviar uma imagem, basta inserir 'imagem' no chat e enviar. Isso abrirá um local para
   colocar o caminho da imagem e o prompt que irá junto (inserir 'imagem' sozinha).
3. Para sair do chat, basta inserir 'sair','exit' ou 'quit'.
