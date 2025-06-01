import os

class Paths:
    """
    Classe responsável por armazenar e fornecer caminhos
    de arquivos e pastas utilizados no sistema.
    """
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_AGENTS = os.path.join(ROOT_DIR,'book_agents')
    ROOT_IMAGES = os.path.join(ROOT_DIR,'images')
    TEMP = os.path.join(ROOT_DIR,'temp')
