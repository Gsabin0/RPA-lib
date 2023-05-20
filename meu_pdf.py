import PyPDF2
import os 
import shutil
import glob


def pdf(cam_arq, start_page=None, end_page=None):
    """
    Extrai o texto de um arquivo PDF especificado.

    Args:
        cam_arq (str): O caminho do arquivo PDF a ser processado.
        start_page (int, opcional): O número da primeira página a ser extraída. Se não especificado, a primeira página será a página inicial.
        end_page (int, opcional): O número da última página a ser extraída. Se não especificado, a última página será a página final.

    Returns:
        str: O texto extraído do arquivo PDF.

    Raises:
        FileNotFoundError: Se o arquivo PDF especificado não for encontrado.
        PyPDF2.utils.PdfReadError: Se ocorrer um erro ao ler o arquivo PDF.

    """
    with open(cam_arq, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)
        
        if start_page is None:
            start_page = 0
        
        if end_page is None:
            end_page = total_pages
        
        start_page = max(0, min(start_page, total_pages))
        end_page = max(start_page, min(end_page, total_pages))
        
        txt = ""
        for page_number in range(start_page, end_page):
            page = pdf_reader.pages[page_number]
            txt += page.extract_text()
    
    return txt

