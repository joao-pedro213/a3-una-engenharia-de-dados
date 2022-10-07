from datetime import datetime


class Logger:
    def log_mensagem(self, mensagem: str) -> None:
        """
        Realiza o print customizado
        """
        print(f"{datetime.utcnow()} - {mensagem}")
