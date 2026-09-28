#  Capstone Web - Plataforma de Contratación de Servicios

> **Curso:** Capstone
> **Institución:** Duoc Uc (San Bernardo) 
> **Semestre / Año:** Segundo Semestre 2026

---

##  Descripción del Proyecto

Capstone Web es una aplicación web desarrollada con Django diseñada para conectar usuarios con diversos servicios profesionales y técnicos. La plataforma permite a los visitantes explorar el catálogo de servicios disponibles, registrarse e iniciar sesión, contratar servicios a través de una pasarela integrada y dejar reseñas y calificaciones sobre las experiencias obtenidas. Su objetivo principal es facilitar la gestión y contratación de servicios en un entorno centralizado y seguro.

---

##  Integrantes del Equipo

* **[Angelo Sepulveda Diaz]** -- [@usuario_github](https://github.com/usuario)
* **[Nombre Integrante 2]** -- [@usuario_github](https://github.com/usuario)

---

##  Tecnologías Utilizadas

* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, Django Templates
* **Backend:** Python (Django Web Framework)
* **Base de Datos:** SQLite / PostgreSQL (Django ORM)
* **Control de Versiones:** Git & GitHub

---

##  Estructura del Repositorio

```text
Capstone-Web/
├── capstone_web/          # Configuración principal del proyecto Django (settings, urls, wsgi)
├── servicios/             # Aplicación Django (modelos, vistas, formularios y URLs)
│   ├── templates/         # Plantillas HTML (index, login, registro, perfil, pasarela, etc.)
│   ├── static/            # Archivos estáticos (CSS, JS, imágenes)
│   ├── models.py          # Modelos de Servicios, Reseñas, Transacciones
│   ├── views.py           # Lógica de negocio y manejo de peticiones
│   ├── forms.py           # Formularios de autenticación y reseñas
│   └── urls.py            # Enrutamiento interno de la aplicación
├── docs/                  # Documentación, diagramas ER y entregables del curso
├── manage.py              # Script ejecutable para la gestión de Django
├── db.sqlite3             # Base de datos local de desarrollo
├── .gitignore             # Archivos excluidos del control de versiones
└── README.md              # Presentación principal del repositorio