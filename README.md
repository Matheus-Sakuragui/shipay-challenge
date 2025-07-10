# Como rodar


---

## Crie e ative um ambiente virtual

### No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### No Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Instale as dependências

As dependências estão no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

## Inicialize o banco de dados

Este comando cria as tabelas e cria alguns dados de teste.

```bash
flask inicializar_db
```

---

## Execute a aplicação


```bash
flask run
```

---

## Documentação das rotas

A documentação interativa das rotas disponível em:

[http://localhost:5000/swagger-ui](http://localhost:5000/swagger-ui)

---
