from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import zipfile
import smtplib
import os 

def email_simples(quem,msg):
    """
    Envia um e-mail simples para o destinatário especificado.
    
    Args:
        quem (str): O endereço de e-mail do destinatário.
        msg (str): A mensagem a ser enviada.
    Returns:
        None
    """
    sender_email = "ic.paranoa@gmail.com"
    receiver_email = f"{quem}"
    password = "dtocpjphwsworesl"
    message = MIMEMultipart()
    message["Subject"] = "Relatorio de reclamações"
    message["From"] = sender_email
    message["To"] = receiver_email
    text = f"""    
    <html>
        <body>
            <p>Ola</p>
            <p>{msg}</p>
        </body>
    </html>
    """
    
    text_part = MIMEText(text, "html")
    message.attach(text_part)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Configura a criptografia TLS
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("E-mail enviado com sucesso!")


def email_zip(quem,msg,pasta):
    """
    Envia um e-mail com um arquivo ZIP anexado para o destinatário especificado.
    
    Args:
        quem (str): O endereço de e-mail do destinatário.
        msg (str): A mensagem a ser enviada.
        pasta (str): O nome da pasta que será compactada e anexada ao e-mail.
    Returns:
        None
    """
    sender_email = "ic.paranoa@gmail.com"
    receiver_email = f"{quem}"
    password = "dtocpjphwsworesl"
    message = MIMEMultipart()
    message["Subject"] = "Relatorio de reclamações"
    message["From"] = sender_email
    message["To"] = receiver_email
    text = f"""    
    <html>
        <body>
            <p>Ola</p>
            <p>{msg}</p>
        </body>
    </html>
    """
    
    text_part = MIMEText(text, "html")
    message.attach(text_part)
    zip_file = zipfile.ZipFile(f"{pasta}.zip", "w", zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(f"{pasta}"):
        for file in files:
            zip_file.write(os.path.join(root, file))
    zip_file.close()
    # Adiciona o arquivo zip como anexo
    with open(f"{pasta}.zip", "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="zip")
        attachment.add_header("Content-Disposition", "attachment", filename=f"{pasta}.zip")
        message.attach(attachment)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Configura a criptografia TLS
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    os.remove(f"{pasta}.zip")
    print("E-mail enviado com sucesso!")
 

def email_imagem(quem, msg, cam_img, no_img):
    """
    Envia um e-mail com uma imagem anexada.

    Args:
        quem (str): O endereço de e-mail do destinatário.
        msg (str): A mensagem a ser incluída no corpo do e-mail.
        cam_img (str): O caminho do diretório onde a imagem está localizada.
        no_img (str): O nome do arquivo de imagem a ser anexado.

    Returns:
        None
    """
    sender_email = "ic.paranoa@gmail.com"
    receiver_email = f"{quem}"
    password = "dtocpjphwsworesl"
    message = MIMEMultipart()
    message["Subject"] = "Relatorio de reclamações"
    message["From"] = sender_email
    message["To"] = receiver_email
    text = f"""
    <html>
        <body>
            <p>Ola</p>
            <p>{msg}</p>
        </body>
    </html>
    """

    text_part = MIMEText(text, "html")
    message.attach(text_part)

    with open(f"{cam_img}\\{no_img}", "rb") as f:
        img_data = f.read()

    _, img_extension = os.path.splitext(no_img)
    image_part = MIMEImage(img_data, name=no_img, _subtype=img_extension[1:])
    message.attach(image_part)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Configura a criptografia TLS
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("E-mail enviado com sucesso!")


