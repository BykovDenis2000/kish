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
### 4. зависимости
1. torch==2.0.0
2. numpy==1.20.1
3. scikit-learn==1.0.2
4. https://github.com/huggingface/transformers
5. FastApi
### 5. Запустить проект из папки app

```bash
uvicorn main:app
```
### 6. Для запуска через Docker можно скачать образ из Docker Hub https://hub.docker.com/repository/docker/denbykov/kish/general
