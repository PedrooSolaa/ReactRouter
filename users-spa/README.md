# SPA de Gestión de Usuarios con React Router

Esta es una Single Page Application (SPA) construida con React, TypeScript y React Router v7.

## Características

- ✅ React Router v7 en modo declarativo
- ✅ Consumo de API REST (Python Backend)
- ✅ Separación de responsabilidades:
  - Services para peticiones HTTP
  - Custom hooks para lógica de estado
  - Componentes de presentación
- ✅ Navegación sin recarga de página
- ✅ Páginas de detalle con parámetros dinámicos

## Estructura del Proyecto

```
src/
 ├─ pages/           # Páginas de la aplicación
 │   ├─ Home.tsx
 │   ├─ Users.tsx
 │   └─ UserDetail.tsx
 ├─ components/      # Componentes reutilizables
 │   └─ Navbar.tsx
 ├─ services/        # Servicios para API
 │   └─ usersService.ts
 ├─ hooks/           # Custom hooks
 │   └─ useUsers.ts
 ├─ App.tsx          # Configuración de rutas
 └─ main.tsx         # Punto de entrada
```

## Requisitos Previos

- Node.js instalado
- Backend de Python corriendo en `http://127.0.0.1:8000/users`

## Instalación y Uso

1. Instalar dependencias:
```bash
npm install
```

2. Iniciar el servidor de desarrollo:
```bash
npm run dev
```

3. Abrir en el navegador: `http://localhost:5173`

## Rutas Disponibles

- `/` - Página de inicio
- `/users` - Lista de usuarios
- `/users/:id` - Detalle de usuario específico

## Tecnologías Utilizadas

- **React 18** - Biblioteca UI
- **TypeScript** - Tipado estático
- **React Router v7** - Navegación
- **Vite** - Build tool y dev server

## API Backend

La aplicación consume la siguiente API:

- `GET http://127.0.0.1:8000/users` - Obtiene lista de usuarios

Ejemplo de respuesta:
```json
[
  {
    "id": 1,
    "name": "Vicent",
    "surname": "Foo",
    "email": "vicent@example.com"
  }
]
```

## Desarrollo

El proyecto sigue las mejores prácticas:

- Separación de responsabilidades
- Custom hooks para lógica reutilizable
- Services para abstraer llamadas HTTP
- Tipado fuerte con TypeScript
- Estructura de carpetas organizada

