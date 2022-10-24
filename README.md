# Projeto Final - EY Machine Learning
### EY Fast Track Specialist - Machine Learning projeto final

O objetivo deste projeto é criar as bases de um sistema capaz de auxiliar deficientes visuais na identificação de objetos no mundo à sua volta.

A princípio, a ideia básica é apontar a câmera do dispositivo na direção desejada. A partir daí o sistema realiza a identificaçao dos objetos na imagem e informa ao usuário.

## Notebooks

O notebook final é o Projeto Final - EY Machine Learning.ipynb. O outro arquivo é um notebook de desenvolvimento dos algorítmos usados.

## Instalação

- Clone este projeto na sua máquina
    - git clone https://github.com/diegommir/ey-ml.git

- Crie um ambiente virtual para o projeto
    - python3 -m venv .venv

- Ative o ambiente virtual
    - No mac: source .venv/bin/activate

- Atualize o PIP
    - pip install -U pip

- Instale o Jupyter Lab
    - pip install jupyterlab

- Crie uma referência ao ambiente para o Jupyter
    - pip install ipykernel
    - python -m ipykernel install --user --name=.venv                     

- Instale as dependências
    - pip install -r requirements.txt

- Execute o Lab
    - jupyter-lab
