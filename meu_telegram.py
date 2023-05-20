import requests
import telegram
import asyncio

def tele_msg(token,id_,msg):
    """
    Envia uma mensagem de texto para um chat no Telegram.

    Args:
        token (str): O token de autenticação do bot do Telegram.
        id_ (str): O ID do chat para onde a mensagem será enviada.
        msg (str): A mensagem de texto a ser enviada.

    Returns:
        None
    """
    token = token
    chat_id = id_
    mensagem = msg
    bot = telegram.Bot(token=token)
    async def send_message():
        await bot.send_message(chat_id=chat_id, text=mensagem)
    asyncio.run(send_message())
    url = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text="+mensagem
    resposta = requests.get(url)
    print(resposta.json())


def tele_img(token,id_,msg,cam_img):
    """
    Envia uma mensagem de texto e uma imagem para um chat no Telegram.

    Args:
        token (str): O token de autenticação do bot do Telegram.
        id_ (str): O ID do chat para onde a mensagem e a imagem serão enviadas.
        msg (str): A mensagem de texto a ser enviada.
        cam_img (str): O caminho da imagem a ser enviada.

    Returns:
        None
    """
    token = token
    chat_id = id_
    mensagem = msg
    bot = telegram.Bot(token=token)
    async def send_image():
        await bot.send_photo(chat_id=chat_id, photo=open(rf'{cam_img}', 'rb'))
    asyncio.run(send_image())
    url = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text="+mensagem
    resposta = requests.get(url)
    print(resposta.json())

