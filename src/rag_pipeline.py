import os
import tqdm
from dotenv import load_dotenv
from src.utils.loader import load_documents_from_directory
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
load_dotenv()

model_name_embedding = os.getenv("EMBEDDING_MODEL")
data_dir = os.getenv("DATA_DIR")
db_dir = os.getenv("DB_DIR")


def create_vector_store(db_dir):
    """
    Crea un almacén de vectores utilizando Chroma y embeddings de HuggingFace.

    Args:
        db_dir (str): Directorio donde se almacenarán los datos persistentes.

    Returns:
        Chroma: Instancia del almacén de vectores creado o None si falla.
    """
    try:

         # Leer los documento de data
        docs = load_documents_from_directory(data_dir)
        if not docs or not isinstance(docs, list):
            raise ValueError("La lista de documentos está vacía o no es válida.")

        print(f"✅ Iniciando creación de vector store con {len(docs)} documentos...")

        # Chequeamos el directorio
        os.makedirs(db_dir, exist_ok=True)

        embedding_model = HuggingFaceEmbeddings(model_name=model_name_embedding)

        for i, doc in enumerate(tqdm.tqdm(docs, desc="Procesando documentos", ncols=80)):
            if not hasattr(doc, "page_content"):
                print(f"⚠️ Documento {i} no tiene contenido.")

        # Inicializar el modelo de embeddings. 
        # Automaticamente me crea la base en db, no es necesario vector.persist()
        vector_store = Chroma.from_documents(docs, embedding=embedding_model,persist_directory=db_dir)

        print(f"✅ Vector store creado y guardado en: {os.path.abspath(db_dir)}")
        
        return vector_store

    except Exception as e:
        print(f"❌ Error durante la creación del vector store: {e}")
        return None


if __name__ == "__main__":
    create_vector_store(db_dir)
