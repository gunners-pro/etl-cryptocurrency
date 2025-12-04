import requests, json, os
import dotenv
from datetime import datetime, timezone
from azure.storage.blob import BlobServiceClient

dotenv.load_dotenv()
blob = BlobServiceClient(
    account_url="http://localhost:10000/devstoreaccount1",
    credential="Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw=="
)

def ingest():
    token = os.getenv("CRYPTO_API_TOKEN")

    if not token:
        print("ERRO: variável de ambiente CRYPTO_API_TOKEN não encontrada.")
        return

    headers = {
        "Authorization": f"Bearer {token}"
    }

    currency = ["BTC", "ETH", "LTC", "ETC", "DASH"]
    symbols = "%20".join(currency)

    url = f"https://api.freecryptoapi.com/v1/getData?symbol={symbols}"
    response = requests.get(url, headers=headers)

    try:
        data = response.json()
    except:
        print("ERRO: a resposta não é um JSON válido.")
        return
    
    if data.get("status") != "success":
        print("ERRO NA API:", data.get("error"))
        return

    now = datetime.now(timezone.utc).strftime("%d-%m-%Y_%H-%M-%S")
    blob_path = f"raw/crypto_{now}.json"

    container = blob.get_container_client("datalake")
    json_bytes = json.dumps(data).encode("utf-8")
    container.upload_blob(
        name=blob_path,
        data=json_bytes,
        blob_type="BlockBlob",
        overwrite=False
    )

    print("Bronze salvo: ", blob_path)

if __name__ == "__main__":
    ingest()
    