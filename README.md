# morpCRIPT
> Este repo deve apresentar uma sequência de desafios na codificação e decodificação de texto usando a linguagem Python, sendo um caminho 
para iniciantes que buscam aprender algumas técnicas e alcançar o NLP(Natural Processing Language) no processamento de texto.

## Preparando ambiente
Para uma execução é necessária a clonagem do repo para um diretório local. Alguns dos conceitos sobre virtualização serão abortados e pontuados entre os envolvidos como práticas para solucionar problemas de dependências no projeto.

### Clonagem baseada em SSH
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
> Obs: Mantenha o aquivo *requirements.txt* atualizado sempre que uma biblioteca for adicionada ou removida do projeto. Este projeto adota o método *pip freeze* para a listagem de dependências.
```powershell
pip freeze > requirements.txt
```
