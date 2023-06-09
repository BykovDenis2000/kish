# Деплой модели
### 1. Дообучить модель в коллабе

https://colab.research.google.com/drive/1DTSqx2VNgfE5qJ0h7XdkPzemH_I2f2FA?usp=sharing

### 2. Скачать полученную папку model/essays в папку проекта app/model

### 3. Склонировать и установить репозиторий transformers от huggingface

```bash
git clone https://github.com/huggingface/transformers
cd transformers
pip install .
```

### 4. Запустить проект из папки app

```bash
uvicorn main:app
```
### 5. Для запуска через Docker можно скачать образ из Docker Hub https://hub.docker.com/repository/docker/denbykov/kish/general
