import json
from pathlib import Path

import boto3
from botocore.exceptions import ClientError
from mypy_boto3_textract.type_defs import DetectDocumentTextResponseTypeDef

def detect_file_text() -> None:
    client = boto3.client("textract")

    file_path = str(Path(__file__).parent / "images" / "lista-material-escolar.jpeg")
    print(f"Iniciando a extração de texto da imagem '{file_path}'...")

    with open(file_path, "rb") as f:
        document_bytes = f.read()

    try:
        response = client.detect_document_text(Document={"Bytes": document_bytes})
        with open("response.json", "w") as response_file:
            response_file.write(json.dumps(response))
        print("Salvando a resposta completa em 'response.json'...")
    except ClientError as e:
        print(f"Erro processando documento: {e}")

def get_lines() -> list[str]:
    try:
        with open("response.json", "r") as f:
            data: DetectDocumentTextResponseTypeDef = json.loads(f.read())
            blocks = data["Blocks"]
        return [block["Text"] for block in blocks if block["BlockType"] == "LINE"]  # type: ignore
    except IOError:
        detect_file_text()
    return []

if __name__ == "__main__":
    lines = get_lines()
    if lines:
        print("\nTexto extraído:")
        for line in lines:
            print(line)
        print("\nProcesso concluído com sucesso!")
    else:
        print("Nenhum texto foi extraído.")