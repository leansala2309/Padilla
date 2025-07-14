# Sistema de pañol

Aplicación básica para controlar ingresos y egresos de productos mediante un lector de códigos de barras. Utiliza Flask y SQLite.

## Requisitos

- Python 3.10+
- Dependencias en `requirements.txt`

Instalación de dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecutar la aplicación:
```bash
python run.py
```

Abrir en el navegador `http://localhost:5000`.

La interfaz permite registrar nuevos productos, realizar ingresos o egresos y consultar el historial.

Los productos con stock por debajo del mínimo se muestran resaltados.
