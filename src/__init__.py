"""Paquete de la práctica STI Incidencias.

Este módulo expone la API pública del paquete y registra un alias
`sti_incidencias` para compatibilidad con los tests que importan
con ese nombre.
"""

import sys as _sys

# Registrar alias de paquete: permite hacer `import sti_incidencias`
# cuando el paquete está en el directorio `src` y se importa como `src`.
_sys.modules.setdefault("sti_incidencias", _sys.modules[__name__])

from .db import (
	DBConfig,
	load_config_from_env,
	get_connection,
	fetch_all,
	execute,
)
from .incidencias import (
	listar_incidencias_activas,
	listar_incidencias_sin_tecnico,
	crear_incidencia,
	asignar_tecnico,
	cerrar_incidencia,
	detalle_incidencias_join,
)

__all__ = [
	"DBConfig",
	"load_config_from_env",
	"get_connection",
	"fetch_all",
	"execute",
	"listar_incidencias_activas",
	"listar_incidencias_sin_tecnico",
	"crear_incidencia",
	"asignar_tecnico",
	"cerrar_incidencia",
	"detalle_incidencias_join",
]
