# SPACERIDERS API

## ⚠️ REQUIREMENTS

- Docker
- Python
- Poetry

## ⚙️ INSTALLATION

Before you start with this installation, you need to have running [spaceriders-smartcontracts](https://github.com/redigaffi/spaceriders-smartcontracts) project.

Clone the project's repository. 

```bash
git clone git@github.com:redigaffi/spaceriders-apiv2.git
```
Inside the project's folder, set up docker's cache and db container. The -d option will execute the command without a shell.

```bash
docker-compose up -d cache
docker-compose up -d db
```

Create a virtual enviroment with poetry and install project dependencies.

```bash
poetry shell
poetry install
```

Here, copy the env vars file `.env.eg` to another one called `.env`.

```bash
cp .env.example .env
```

## 🚀 USAGE

Execute the project using these scripts.

```bash
./scripts/start_local.sh
./scripts/start_websockets.sh
```

You can check if the api works accessing through the browser to `localhost:8010/docs`.
