# Torrentio Indexer Update (Prowlarr)

## ¿Qué se cambió?

### 1) Mejoras en la configuración del indexer
- Se agregaron campos de tipo `info` para que la UI de Prowlarr muestre:
  - Que la clave de Real-Debrid es obligatoria (`rdkey_label`)
  - Qué IDs de IMDB usar para validar el indexer en Sonarr/Radarr (`validation_label`, `validate_imdb_movie_label`)
- Se ajustaron las etiquetas y valores por defecto para que sean más claros.
- Ahora los campos de validación IMDB (película y serie) se dejan vacíos por defecto para evitar que búsquedas genéricas siempre retornen el mismo contenido (p.ej., Fight Club).

### 2) Compatibilidad con AllDebrid / RealDebrid (hash de torrent en URL)
- Torrentio, cuando se usa con proveedores como AllDebrid/RealDebrid, puede devolver streams donde **no hay campo `infoHash`**, solo una URL.
- Se agregó una extracción (`regexp`) desde `url` para obtener el hash de 40 caracteres y alimentar correctamente a Prowlarr.

### 3) Otros ajustes
- Se añadió el campo `leechers` con valor estático `0` para evitar que el indexer devuelva un valor vacío (algunos clientes esperan el campo).

## Cómo validar localmente
1. Validar el YAML contra el esquema v9:
   ```bash
   python validate_schema.py
   ```
2. Si necesitas comprobar que la configuración retorna datos válidos, lanza un contenedor de Prowlarr apuntando a este archivo (`torrentio.yml`) y prueba la integración en la UI.

## Próximos pasos (Docker)
- Montar el archivo `torrentio.yml` dentro del contenedor de Prowlarr (o reemplazarlo) y reiniciar Prowlarr.
- En Prowlarr, agregar el indexer “Torrentio” y verificar que los tests de conexión / búsqueda funcionen.
