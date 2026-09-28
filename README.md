#  Capstone Web - Plataforma de Contratación de Servicios

> **Curso:** Capstone
> **Institución:** Duoc Uc (San Bernardo) 
> **Semestre / Año:** Segundo Semestre 2026

---

##  Descripción del Proyecto

Easy Office es una empresa que busca una aplicación web dinámica, escalable y segura. Por lo que de momento vamos a desarrollar un proyecto que automatiza el proceso de contratación y gestión de oficinas virtuales para emprendedores y empresas. En donde la plataforma permite a los usuarios explorar planes de servicios digitales (dirección tributaria, atención telefónica, uso de salas de reunión, entre otros), registrar sus empresas, realizar contrataciones en tiempo real y gestionar sus servicios activos desde un panel personalizado.

El sistema cuenta con una arquitectura basada en el patrón MVT (Modelo-Vista-Template) y un esquema de control de acceso por roles diferenciados, brindando una experiencia adaptada tanto para los clientes finales como para el personal ejecutivo/administrativo.

---

##  Integrantes del Equipo

* **[Angelo Sepulveda Diaz]** -- [@jack1626](https://github.com/jack1626)
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