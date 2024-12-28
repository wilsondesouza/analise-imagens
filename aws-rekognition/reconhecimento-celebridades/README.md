# 🎉 Reconhecimento de Celebridades

Um projeto Python que utiliza AWS Rekognition para identificar celebridades em imagens e desenhar caixas ao redor de seus rostos.

## 🎯 Objetivo

Automatizar o reconhecimento de celebridades em imagens usando o serviço Amazon Rekognition, destacando visualmente as celebridades identificadas.

## 🛠️ Tecnologias Utilizadas

- Python 3.13+
- AWS Rekognition
- boto3
- mypy-boto3-rekognition
- Pillow

## 📋 Pré-requisitos

- Conta AWS configurada com credenciais de acesso
- Python 3.13 ou superior
- Gerenciador de pacotes `uv` ou `pip`

## 🔧 Instale as dependências:

```bash
uv pip install -e .
# ou
pip install -e .
```

## 🚀 Como usar

1.Coloque sua imagem na pasta [images](images/)

2. Execute o script principal:
 ```bash
 python main.py
 ```
 ![Código](prints/code.png)

3. As imagens com as caixas desenhadas ao redor das celebridades serão salvas na pasta images com o sufixo -resultado.jpg.

## 🔍 Como funciona

O projeto utiliza três funções principais:

`get_path(file_name: str) -> str`
 - Retorna o caminho completo de um arquivo na pasta images.

`recognize_celebrities(photo: str) -> RecognizeCelebritiesResponseTypeDef`
 - Utiliza o cliente Rekognition para reconhecer celebridades em uma imagem.

`draw_boxes(image_path: str, output_path: str, face_details: list[CelebrityTypeDef])`
 - Desenha caixas ao redor dos rostos das celebridades reconhecidas e salva a imagem resultante.

## 💡 Insights

### Casos de Uso

1. Eventos e Mídia:
 - Identificação de celebridades em fotos de eventos, facilitando a catalogação e publicação.

2. Segurança:
 - Monitoramento de locais públicos para identificar celebridades ou pessoas de interesse.

### Otimização

1. Interface Gráfica:
 - Desenvolvimento de uma interface gráfica para facilitar o upload de imagens e a visualização dos resultados.
  
2. Suporte a Múltiplos Formatos de Imagem:
 - Adicionar suporte para diferentes formatos de imagem (PNG, TIFF, etc.) além do JPEG.

### Formas Práticas de Uso

1. Serviço Web:
 - Transformar a aplicação em um serviço web onde os usuários podem fazer upload de imagens e receber os resultados via API.

2. Aplicativo Móvel:
 - Desenvolver um aplicativo móvel que permita aos usuários tirar fotos e identificar celebridades instantaneamente.