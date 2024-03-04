# morpCRIPT

> Este repo deve apresentar uma sequência de desafios na codificação e decodificação de texto usando a linguagem Python, sendo um caminho 
para iniciantes que buscam aprender algumas técnicas e alcançar o NLP(Natural Processing Language) no processamento de texto.

## Preparando ambiente

Para uma execução do projeto é necessária a clonagem do repo para um diretório local. Alguns dos conceitos sobre virtualização de ambiente devem ser seguidos neste processo para o gerenciamento do ambiente.

### Usando SSH
```powershell
git clone git@github.com:rodrigmars/morpCRIPT.git
```
### Acessando pasta criada
Windows PowerShell
```powershell
cd .\morpCRIPT\
```
## Criando ambiente virtual
Windows PowerShell
```powershell
python -m venv env-morpcript
```
## Ativando o ambiente virtual
Windows PowerShell
```powershell
.\env-morpcript\Scripts\activate
```
## Instalando dependências
> Obs: Antes de instalar qualquer biblioteca no projeto é necessário ativação do ambiente virtual.
```powershell
pip install -r requirements.txt
```
## Atualizando requirements
> Obs: Mantenha o aquivo *Requirements.txt* atualizado sempre que uma biblioteca for adicionada ou removida do projeto.
```powershell
upgrade-requirements
```
