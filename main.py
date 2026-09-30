"""
Qualifica Hub
Ponto de entrada para execução com PyScript.
"""

from pyscript import document

from src.banco import criar_banco
from src.models import Sistema
from src.menus import menu_principal


def atualizar_status(mensagem):
    """Exibe mensagens na interface HTML."""
    elemento = document.querySelector("#status")
    elemento.textContent = mensagem


def main():
    """Inicializa o sistema Qualifica Hub."""

    try:
        atualizar_status("Inicializando Qualifica Hub...")

        # Inicializar banco de dados
        criar_banco()

        # Instanciar o sistema
        sistema = Sistema()

        atualizar_status("Sistema inicializado!")

        # Executar o menu principal
        menu_principal(sistema)

    except Exception as erro:
        atualizar_status(
            f"Erro ao inicializar: {erro}"
        )
        raise


main()
