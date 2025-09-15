## MLOps - TP 1

### Exercice 4 - Level 4 (Bonus)

Level 4 builds upon previous work from [this Kaggle project](https://www.kaggle.com/code/toutane/gh-navires-2025). The goal is to deploy a **Keras image classifier** for boat types using **FastAPI**, enabling inference through an HTTP API.

##### Description

This project implements a FastAPI server that:

- Loads a pre-trained Keras model (`model_2025-05-28_10-54_valacc0.8134.keras`) capable of classifying images of boats.
- Exposes an endpoint `/predict` to predict the class of an uploaded image.
- Supports 13 boat classes:  
  `coastguard`, `containership`, `corvette`, `cruiser`, `cv`, `destroyer`, `ferry`, `methanier`, `sailing`, `smallfish`, `submarine`, `tug`, `vsmallfish`.

The FastAPI server runs by default on **port 5042**. The input images are expected in RGB format and resized to **32x32 pixels** (matching the model input).

This work was completed as part of the **Introduction to Neural Networks course** at **EPITA (2nd year)**. The project was done in pairs; my co-member was **Armand Thibaudon**. The original Kaggle page explains the **Keras architecture** and preprocessing steps in detail.

#### Usage

Once the FastAPI server is running, you can make a prediction request using `curl`:

```bash
curl -X POST "http://{host}:{port}/predict" \
  -F "file=@/path/to/image.jpg" | jq

