from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def conf_selenium(caminho_d,url):
    """
    Configura e retorna uma instância do navegador Selenium para automação e testes.
    
    Args:
        caminho_d (str): O caminho do diretório onde os arquivos serão baixados.
        url (str): A URL que o navegador deve abrir.
    
    Returns:
        selenium.webdriver.Chrome: A instância do navegador Selenium configurada.
    """
    options = Options()
    options.add_experimental_option("prefs", {
    "download.default_directory":  rf'{caminho_d}',
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "plugins.always_open_pdf_externally": True,
    "plugins.plugins_disabled": ["Chrome PDF Viewer"] 
    })
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=options)
    navegador.maximize_window()
    navegador.implicitly_wait(2)

    navegador.get(url)

    return navegador


def click_(nav, value, locator=None):
    """
    Localiza um elemento na página usando diferentes estratégias de localização e realiza um clique nele.
    
    Args:
        nav (selenium.webdriver.Chrome): A instância do navegador Selenium.
        value (str): O valor do elemento a ser localizado (ex: ID, XPath, nome, classe, etc.).
        locator (selenium.webdriver.common.by.By, optional): O tipo de estratégia de localização a ser utilizado. 
            Se não for fornecido, serão tentadas todas as estratégias disponíveis.
    
    Returns:
        None
    
    Raises:
        NoSuchElementException: Se o elemento não for encontrado usando nenhuma das estratégias de localização.
    """
    strategies = {
        By.ID: "id",
        By.XPATH: "xpath",
        By.NAME: "name",
        By.CLASS_NAME: "class",
        By.TAG_NAME: "tag",
        By.LINK_TEXT: "text",
        By.PARTIAL_LINK_TEXT: "partial_text",
        By.CSS_SELECTOR: "css"  
    }

    if locator is None:
        locators = strategies.keys()
    else:
        locators = [locator]
    
    for locator_strategy in locators:
        strategy_name = strategies.get(locator_strategy)
        try:
            nav.find_element(locator_strategy, value).click()
            print(f"Elemento encontrado usando o seletor '{strategy_name}'")
            break
        except:
            pass
    else:
        print("Elemento não encontrado")


def input_(nav, value, texto, locator=None):
    """
    Localiza um elemento de input em uma página web e insere um texto nele.

    Args:
        nav (selenium.webdriver): A instância do navegador Selenium.
        value (str): O valor do atributo usado para localizar o elemento.
        texto (str): O texto a ser inserido no elemento de input.
        locator (str, optional): O seletor usado para localizar o elemento. Os valores
            possíveis são: "id", "xpath", "name", "class", "tag", "text", "partial_text" e "css".
            Se não for especificado, todos os locators serão tentados.

    Returns:
        None
    """
    strategies = {
        By.ID: "id",
        By.XPATH: "xpath",
        By.NAME: "name",
        By.CLASS_NAME: "class",
        By.TAG_NAME: "tag",
        By.LINK_TEXT: "text",
        By.PARTIAL_LINK_TEXT: "partial_text",
        By.CSS_SELECTOR: "css"  
    }

    if locator is None:
        locators = strategies.keys()
    else:
        locators = [locator]
    
    for locator_strategy in locators:
        strategy_name = strategies.get(locator_strategy)
        try:
            nav.find_element(locator_strategy, value).send_keys(texto)
            print(f"Elemento de input encontrado usando o seletor '{strategy_name}'")
            break
        except:
            pass
    else:
        print("Elemento de input não encontrado")


def texto_(nav, value, locator=None):
    """
    Localiza um elemento usando diferentes estratégias de localização e retorna o texto do elemento encontrado.

    Args:
        nav (selenium.webdriver.remote.webdriver.WebDriver): A instância do navegador Selenium.
        value (str): O valor usado para localizar o elemento.
        locator (selenium.webdriver.common.by.By, opcional): A estratégia de localização do elemento.
            Os elementos possíveis são: "id", "xpath", "name", "class", "tag", "text", "partial_text" e "css".
            Se não for especificado, todos os locators serão tentados.

    Returns:
        str or None: O texto do elemento encontrado, ou None se o elemento não for encontrado.
    """
    strategies = {
        By.ID: "id",
        By.NAME: "name",
        By.CLASS_NAME: "class",
        By.TAG_NAME: "tag",
        By.LINK_TEXT: "text",
        By.PARTIAL_LINK_TEXT: "partial_text",
        By.CSS_SELECTOR: "css",
        By.XPATH: "xpath"
    }

    if locator is None:
        locators = strategies.keys()
    else:
        locators = [locator]
    
    for locator_strategy in locators:
        strategy_name = strategies.get(locator_strategy)
        try:
            element = nav.find_element(locator_strategy, value)
            text = element.text
            print(f"Texto do elemento encontrado usando o seletor '{strategy_name}': {text}")
            break
        except:
            pass
    else:
        print("Elemento não encontrado")
        return None
    
    return text