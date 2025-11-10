#para que el script siempre se ejecute desde su propio directorio
Set-Location -Path $PSScriptRoot

& .\venv\Scripts\Activate.ps1

python .\main.py

deactivate