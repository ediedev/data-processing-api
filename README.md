# Data Processing API

A FastAPI backend system for uploading and cleaning CSV files automatically.

## Features

- Upload CSV files
- Remove duplicate rows
- Standardize column names
- Handle missing values
- Return cleaned JSON data

## Tech Stack

- Python
- FastAPI
- pandas
- Uvicorn

## Setup

```bash
conda create -n data-api python=3.10 -y
conda activate data-api

pip install fastapi uvicorn pandas python-multipart