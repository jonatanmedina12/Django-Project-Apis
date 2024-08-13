# Proyecto API REST con Django

Este proyecto es una API RESTful construida utilizando Django y Django REST Framework. La API proporciona endpoints para gestionar recursos (como usuarios, productos, órdenes, etc.) y sigue los principios REST para la comunicación entre cliente y servidor.

## Características

- **Django**: Framework principal del proyecto.
- **Django REST Framework**: Herramienta utilizada para construir la API REST.
- **Autenticación**: Implementada utilizando tokens (JWT) o autenticación básica.
- **Endpoints CRUD**: Operaciones de creación, lectura, actualización y eliminación para los diferentes recursos.
- **Filtros y Búsquedas**: Soporte para filtrar y buscar en los endpoints.
- **Paginación**: Soporte para paginación de grandes conjuntos de datos.
- **Permisos y Autorización**: Control de acceso a los recursos basado en roles de usuario.

## Requisitos Previos

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados en tu máquina:

- Python 3.8+
- Pipenv o virtualenv para gestionar entornos virtuales
- PostgreSQL (opcional, dependiendo de la base de datos elegida)

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/jonatanmedina12/proyecto-django-api.git
   cd proyecto-django-api
