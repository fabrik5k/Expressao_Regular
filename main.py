import re


def validar_email(email):
    pattern = r'^[a-z0-9+._-]{1,64}[@][a-z0-9-]{1,63}(\.[a-z0-9-]{1,63})+$'
    return re.match(pattern, email) is not None


def ler_e_validar_emails(arquivo):
    try:
        with open(arquivo, 'r') as f:
            emails = f.readlines()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return

    for email in emails:
        email = email.strip()
        if validar_email(email):
            print(f"Válido: {email}")
        else:
            print(f"Inválido: {email}")


ler_e_validar_emails('emails.txt')
