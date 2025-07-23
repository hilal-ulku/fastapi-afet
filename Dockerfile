FROM python:3.10-slim

# Sistem paketlerini ve build araçlarını yükle
RUN apt-get update && apt-get install -y git build-essential python3-dev

# pip ve setuptools'u güncelle
RUN pip install --upgrade pip setuptools wheel

# Gerekli Python paketlerini yükle
RUN pip install twint pandas
