from langchain_community.document_loaders import TextLoader, DirectoryLoader

def load_documents_from_directory(path):
    """
    Carga documentos de texto desde un directorio especificado.

    Args:
        directory_path (str): La ruta del directorio que contiene los archivos de texto.

    Returns:
        list: Una lista de documentos cargados.
    """
    # Configurar el cargador de directorios para archivos .txt
    loader = DirectoryLoader(path, glob="*.txt", loader_cls=TextLoader)

    # Se crea el loader con la configuración correcta (qué carpeta y qué tipo de archivos).
    # Luego, simplemente se retorna la lista de Document ya cargados.
    # Así, desde otro módulo (por ejemplo, rag_pipeline.py), podés hacer:

    return loader.load()
    
