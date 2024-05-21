import smtplib
from email.mime.text import MIMEText

# Define la información del servidor SMTP
smtp_server = "smtp.gmail.com"
port = 587

# Define la información del remitente y destinatario
sender_email = "rac0912@gmail.com"
password = "Rabaroq.0912"
recipient_email = "rafael.antequera@gmail.com"

# Crea el mensaje
message = MIMEText("¡Hola! Este es un correo electrónico de prueba.")
message["Subject"] = "Prueba de correo electrónico"
message["From"] = sender_email
message["To"] = recipient_email

# Inicia la sesión SMTP
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient_email, message.as_string())

print("Correo electrónico enviado correctamente.")
