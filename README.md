# Manipulador de Dados EAN13

Ferramenta desenvolvida para facilitar o manejo, conversão e busca de códigos EAN13, principalmente voltada para uso em Fábricas e Indústrias. A aplicação fornece uma interface gráfica amigável para conversão de códigos EAN para NX e vice-versa, além de funcionalidades para agrupamento de arquivos de bipagens e localização de itens específicos em arquivos.

## Funcionalidades

- **Conversão de Códigos**: Converta códigos EAN13 para NX e vice-versa utilizando dicionários predefinidos. O NX representa o nome das peças da fábrica e pode ser qualquer nome definido pela fábrica.
> **Nota**: O banco de dados NX fornecido no código é apenas um exemplo. Você pode substituir pelo banco de dados específico da sua Indústria, ajustando os dicionários `substituicoes_ean_para_nx` e `substituicoes_nx_para_ean` conforme necessário.

- **Agrupamento de Arquivos**: Agrupe vários arquivos de texto em um único arquivo, facilitando a organização dos dados coletados.

- **Busca de Termos**: Localize termos específicos em arquivos de texto, agilizando a verificação de itens.

- **Geração de Códigos de Barras**: Gere imagens de códigos de barras EAN13 para visualização.

## Interface do Usuário

IMAGEM AQUI

## Uso

- Crie uma Pasta e coloque o Script dentro, junto com os arquivos que irá trabalhar, tudo no mesmo diretório.

## Estrutura do Projeto

- `main.py`: Arquivo principal que contém todo o código da aplicação.


## Requisitos

- Python 3.x
- Bibliotecas:
  - `tkinter`
  - `Pillow`
  - `python-barcode`

Você pode instalar as bibliotecas necessárias utilizando pip:

```bash
pip install Pillow python-barcode

