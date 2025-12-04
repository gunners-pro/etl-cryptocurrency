from azure.storage.blob import BlobServiceClient

connection = BlobServiceClient(
    account_url="http://localhost:10000/devstoreaccount1",
    credential="Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw=="
)

container_name = "datalake"
connection.create_container(container_name)
print("Container criado: ", container_name)