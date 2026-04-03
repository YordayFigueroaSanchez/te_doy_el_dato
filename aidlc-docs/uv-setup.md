**Uso de `uv` para gestión de entornos virtuales**

Breve: he creado un virtualenv llamado `.venv_uv` en la raíz del proyecto y he instalado `uv` dentro. Este documento muestra cómo activar, verificar e usar el entorno.

Estado actual

- Virtualenv: `.venv_uv` (creado)
- Paquete `uv`: instalado en `.venv_uv` (verificado)

Comandos (desde la raíz del repositorio)

1) Crear el virtualenv (ya ejecutado):

```powershell
C:/Users/yfigueroa/.local/bin/python3.12.exe -m venv .venv_uv
```

1) Actualizar pip e instalar `uv` (ya ejecutado):

```powershell
.venv_uv\Scripts\python.exe -m pip install --upgrade pip
.venv_uv\Scripts\python.exe -m pip install uv
```

Activación del entorno

- PowerShell (recomendado):

```powershell
. .venv_uv\Scripts\Activate.ps1
```

- CMD (Windows):

```cmd
.venv_uv\Scripts\activate.bat
```

- Git Bash / WSL / macOS / Linux:

```bash
source .venv_uv/bin/activate
```

Ejecutar comandos con el intérprete del venv (sin activar)

```powershell
.venv_uv\Scripts\python.exe tools/parse_guiones.py
.venv_uv\Scripts\python.exe -m pip show uv
```

Comprobaciones útiles

- Ver paquete `uv` instalado:

```powershell
.venv_uv\Scripts\python.exe -m pip show uv
```

- Ver la ayuda de `uv` (tras activar el entorno):

```powershell
uv --help
# o, si no se pudo activar:
.venv_uv\Scripts\uv.exe --help
```

Uso recomendado

- Activa el entorno y luego usa `python` y `pip` normalmente.
- Si PowerShell bloquea la activación por políticas, utiliza el ejecutable del venv (`.venv_uv\Scripts\python.exe`) para ejecutar scripts.

Fichero de dependencias

- `requirements-uv.txt` contiene la dependencia `uv` usada aquí.

Soporte y próximos pasos

- ¿Quieres que ejecute ahora `tools/parse_guiones.py` con este entorno y genere `aidlc-docs/units/guiones/manifest.csv`? (puedo hacerlo y añadir el manifest al repo)
