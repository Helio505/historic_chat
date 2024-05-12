import os
from dotenv import load_dotenv
from colorama import Fore, Style, init
import google.generativeai as genai
import pathlib
from sys import exit
import pathlib
import PIL.Image
import random
from system_instructions import instructions

init(autoreset=True)
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def get_random_instruction():
    return random.choice(instructions)


personalidade = get_random_instruction()


generation_config = {
    "temperature": 1,
    "top_p": 1,
    'top_k': 1,
}

model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=personalidade.get("instrucoes")
)


class SocratesChat:
    def __init__(self):
        self.model = model
        self.chat = self.model.start_chat(history=[])

    def get_response(self, message, image_path=None):
        if image_path:
            image = PIL.Image.open(image_path)
            response = self.chat.send_message(
                content=[message, image],
                stream=True,
            )
        else:
            response = self.chat.send_message(
                content=[message],
                stream=True
            )
        return response

    def start_chat(self):
        nome_personalidade = personalidade.get("nome")
        print(Fore.GREEN + f"Você está agora conversando com {nome_personalidade.capitalize(
        )}. Digite 'sair' para terminar a conversa." + Style.RESET_ALL)
        while True:
            # Promp usuário
            print(f"{Fore.BLUE}Você: {Style.RESET_ALL}", end="")
            user_message = input()
            print()
            if user_message.lower() in ["sair", "exit", "quit"]:
                break
            elif user_message == "imagem":
                # Print instrução
                print(f"{Fore.MAGENTA}Sistema: {Fore.RED}")
                # Input do caminho da imagem, removidos ""
                image_path = input(
                    "Digite o caminho da imagem que será inserida na mensagem: ").strip('"').strip("'")
                # Verificar se o caminho da imagem é válido
                if not pathlib.Path(image_path).exists():
                    print(f"{Fore.MAGENTA}Sistema: {Fore.RED}")
                    print("Caminho da imagem inválido, tente novamente.")
                    print(Style.RESET_ALL)
                    print()
                    continue
                # Input para a mensagem
                print(f"{Fore.MAGENTA}Sistema: {Fore.RED}")
                user_message = input("Digite a mensagem que será enviada: ")
                print(Style.RESET_ALL)
                print()

                # Inserir mensagem e imagem no modelo
                response = self.get_response(user_message, image_path)
                # Print resposta do modelo
                print(f"{Fore.GREEN}{nome_personalidade.capitalize()}: {
                      Fore.RED}", end="")
                try:
                    for chunk in response:
                        print(f"{chunk.text}", end="", flush=True)
                except ValueError as e:
                    print(f"{Fore.MAGENTA}Sistema: {Fore.RED}", end="")
                    print("Erro na conexão com o sistema, tente novamente.")
                print(Style.RESET_ALL)
                print()
                continue

            # Resposta do modelo
            response = self.get_response(user_message)

            # Print resposta do modelo
            print(f"{Fore.GREEN}{nome_personalidade.capitalize()}: {
                  Fore.RED}", end="")
            try:
                for chunk in response:
                    print(f"{chunk.text}", end="", flush=True)
            except ValueError as e:
                print(f"{Fore.MAGENTA}Sistema: {Fore.RED}", end="")
                print("Erro na conexão com o pergaminho mágico, tente novamente.")
            print(Style.RESET_ALL)
            print()

        # Mensagem de despedida
        print(Fore.GREEN + nome_personalidade.capitalize() +
              ": " + Fore.RED, end="")
        print(Fore.RED, end="")
        print("Até a próxima, adeus!")
        print(Style.RESET_ALL)
        exit(0)


if __name__ == "__main__":
    chat = SocratesChat()
    chat.start_chat()
