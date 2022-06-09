## CUSTOMER REGISTRATION

# Como começar

Primeiro passo:
  Criar sua virtualenv
```bash
  python3 -m venv venv
```

Segundo passo:
  Ativar sua vitualenv
```bash 
  source ./venv/bin/activate
```

Terceiro passo:
  Rode o arquivo run
```bash
  python run.py
```

### END POINTS
http://127.0.0.1:5006

```bash
[GET] /persons -> Get all persons
```
```bash
[POST] /persons/search -> Get unique person by name 
```
```json
body: {"name": "José"}
```
```bash
[POST] /persons/create -> Create unique person 
```
```json
body: {"name": "José", "age": 25, "district": "Guajuviras", "profession": "Developer"}
```
```bash
[PUT] /persons/update -> Update unique person by name 
```
```json
body: {"name": "José", "age": 25, "district": "", "profession": ""}
```
```bash
[POST] /persons/delete -> Delete unique person by name 
```
```json
body: {"name": "José"}
```
