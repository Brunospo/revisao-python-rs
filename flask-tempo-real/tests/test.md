# O pytest tem um comportamento especial com o arquivo conftest.py

## ▶️ Rodando testes

Na raiz do projeto:

```bash
pytest -v --cov=app
```

## 🔎 Como funciona

Quando você roda ``pytest``, ele varre os diretórios de testes procurando arquivos que comecem com ``test_*.py``.

- Para cada diretório que contém testes, se existir um ``conftest.py``, o ``pytest`` carrega ele automaticamente.

- Dentro desse conftest.py, você pode definir fixtures (funções marcadas com @pytest.fixture).

- Essas fixtures ficam disponíveis para todos os testes do diretório e subdiretórios, sem precisar importar manualmente.

Essas fixtures ficam disponíveis para todos os testes do diretório e subdiretórios, sem precisar importar manualmente.

## ✅ Exemplo simples

### 📄 ``tests/conftest.py``

```python
import pytest

@pytest.fixture
def sample_data():
    return {"id": 1, "name": "Pix"}
```

### ``📄 tests/test_example.py``

```python
def test_sample(sample_data):
    assert sample_data["id"] == 1
    assert sample_data["name"] == "Pix"
```

### ➡️ O ``pytest`` já sabe usar a fixture ``sample_data`` porque ela está no ``conftest.py.`` Você não precisa importar nada

```bash
pytest -v
```

## Exemplo desse codigo

```python
with app.app_context():
    db.create_all()
    yield app
    db.session.remove()
    db.drop_all()
```

## 🔎 O que acontece aqui

1.``with app.app_context()``:

- O Flask precisa de um application context para saber qual aplicação está ativa (quem fornece configs, extensões etc.).

- Nos testes (fora do run.py), esse contexto não existe por padrão.

- Então usamos app.app_context() para criar manualmente.

- Sem isso, se você chamasse db.create_all(), daria erro:

```bash
RuntimeError: Working outside of application context
```

2.``db.create_all()``

- Cria todas as tabelas definidas nos seus modelos (``Payment``, ``User`` etc.).

- Como no ``conftest.py`` geralmente configuramos um banco em memória (``sqlite:///:memory:``), isso cria o schema limpo para cada teste.

3.``yield app``

- Essa linha é o coração da fixture do ``pytest``.

- O ``yield`` pausa aqui → entrega a ``app`` para o teste usar.

- O código abaixo do ``yield`` só roda depois que o teste acabar (teardown).

4.``db.session.remove()``

- Limpa a sessão atual do SQLAlchemy (fecha transações abertas, conexões pendentes).

- Evita que “sujeira” de um teste afete outro.

5.``db.drop_all()``

- Remove todas as tabelas criadas com create_all().

- Garante que cada teste começa com banco zerado.

### 🎯 Resumindo

Esse bloco garante que cada teste roda em um banco limpo e isolado:

1. Entra no contexto do Flask.

2. Cria as tabelas (``db.create_all``).

3. Roda o teste (``yield app``).

4. Depois do teste, limpa conexões (``db.session.remove``).

5. Apaga todas as tabelas (``db.drop_all``).

Assim você nunca tem “lixo” de um teste interferindo no outro.

## 🔎 ``app.test_client()``

- Esse método do Flask cria um cliente de teste HTTP.

- Ele permite simular requisições HTTP (GET, POST, etc.) para sua aplicação sem subir servidor real.

- Por baixo dos panos, ele chama diretamente o Flask WSGI, não abre socket na porta 5000.

### Exemplo

```python
client = app.test_client()
resp = client.post("/payments/pix", json={"value": 100})
print(resp.status_code)   # 201
print(resp.get_json())    # {"message": "...", "payment": {...}}
```

Isso faz o mesmo que se você usasse requests.post("<http://127.0.0.1:5000/payments/pix>", json={"value": 100})
➡️ Só que mais rápido e sem precisar rodar o servidor de verdade.
