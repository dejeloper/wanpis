# Script de Compilación - El viaje hacia la libertad

## Uso

Desde la carpeta `script/`, ejecuta:

```powershell
python compile.py
```

## Configuración

Edita las variables al inicio de `compile.py`:

```python
PROJECT_NAME = "El viaje hacia la libertad"    # Nombre de tu proyecto
CHAPTERS_PER_FILE = 20                         # Capítulos por archivo compilado
```

### Ejemplos de configuración:

- **20 capítulos por archivo:** Si tienes 32 capítulos, genera 2 archivos (1-20, 21-40)
- **10 capítulos por archivo:** Si tienes 32 capítulos, genera 4 archivos (1-10, 11-20, 21-30, 31-40)

## Cómo funciona

1. **Limpia** la carpeta `resumen/` (elimina todos los .txt antiguos)
2. **Genera un listado de fechas** (`Extras/fechas_capitulos.txt`) con la fecha de creación de cada capítulo
3. Busca todos los archivos `Capítulo_*.txt` dentro de la carpeta `Chapters/`
4. Los ordena por número
5. Los agrupa en lotes según `CHAPTERS_PER_FILE`
6. Crea archivos compilados en `resumen/` con nombres como:
   - `El viaje hacia la libertad 1-20.txt`
   - `El viaje hacia la libertad 21-40.txt`
   - etc.
7. Los rangos siempre son múltiplos de `CHAPTERS_PER_FILE` (ej: 31-40 aunque solo tengas 32 capítulos)
8. **Agrega un título al inicio** de cada archivo: `PROJECT_NAME + rango` (ej: "El viaje hacia la libertad 1-20")
9. Separa capítulos con `--`

## Actualizar compilados

El script **regenera todos los archivos cada vez que lo ejecutas**. Si cambias un capítulo en `Chapters/`, simplemente ejecuta el script de nuevo y se actualizará automáticamente.

## Estructura de capítulos

Los capítulos **deben** estar en la carpeta `Chapters/` con este formato:

```
Chapters/
├── Capítulo_001.txt
├── Capítulo_002.txt
├── Capítulo_003.txt
└── ...
```

**Importante:** El patrón debe ser exactamente `Capítulo_XXX.txt` (con acento y guion bajo).

El número se extrae automáticamente para el ordenamiento y los rangos de compilación.

## Listado de fechas

El script genera automáticamente un archivo `fechas_capitulos.txt` en la carpeta `Extras/` con las fechas de creación de cada capítulo:

```
LISTADO DE FECHAS DE CREACIÓN DE CAPÍTULOS
==================================================

Capítulo 001: 25/Oct/2025
Capítulo 002: 27/Oct/2025
Capítulo 003: 28/Oct/2025
...
```

Perfecto para mantener un registro antes de eliminar los archivos originales.

## Estructura de archivo compilado

Cada archivo compilado tiene esta estructura:

```
El viaje hacia la libertad 1-20

--

Capítulo 1
[contenido del capítulo 1]

--

Capítulo 2
[contenido del capítulo 2]

--

[... más capítulos ...]
```

## Estructura del proyecto

```
proyecto/
├── Chapters/
│   ├── Capítulo_001.txt
│   ├── Capítulo_002.txt
│   └── ...
├── Extras/
│   └── fechas_capitulos.txt
├── resumen/
│   ├── El viaje hacia la libertad 1-20.txt
│   └── El viaje hacia la libertad 21-40.txt
└── script/
    ├── compile.py
    └── README.md
```

## Notas

- El script regenera **todos** los archivos compilados cada ejecución (elimina los viejos)
- El listado de fechas también se regenera automáticamente en `Extras/`
- Los rangos en los nombres de archivo respetan múltiplos de `CHAPTERS_PER_FILE`
- El título al inicio de cada archivo facilita identificar su contenido
- Ideal para actualizaciones: si cambias cualquier capítulo, ejecuta el script y todo se actualiza automáticamente
- Las fechas en `fechas_capitulos.txt` son la fecha de creación del archivo (útil para mantener registro antes de borrar)
