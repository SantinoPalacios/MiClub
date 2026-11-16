from pathlib import Path
# ── Identidad del club ─────────────────────────────────────────
NOMBRE_CLUB = "RIVER PLATE"
LEMA_CLUB = "Vivir y jugar con Grandeza"
SUBTITULO = "Sistema de gestión del club"
ETIQUETA = "Socios | Cuotas | Clubes"

# ── Colores ────────────────────────────────────────────────────
PRIMARIO = "#6B0504"           # color principal: encabezado y botones
PRIMARIO_HOVER = "#8A1010"     # versión más clara del principal
PANEL = "#F4F4F9"              # fondo del menú lateral y del contenido
FONDO = "#F2F2F2"              # fondo gris detrás de todo
TEXTO = "#0B0A0A"              # texto oscuro sobre fondos claros
TEXTO_CLARO = "#F4F4F9"        # texto claro sobre el color principal
FILA_PAR = "#EAEAF2"           # rayado suave de las tablas
ESTADO_ACTIVO = "#1E7A1E"      # verde para socios/cuotas activas
ESTADO_SUSPENDIDO = "#B00020"  # rojo para socios suspendidos
ESTADO_VENCIDO = "#B00020"     # rojo para cuotas vencidas
ESTADO_PENDIENTE = "#F57E00"   # naranja para cuotas pendientes

# ── Fuentes ────────────────────────────────────────────────────
FUENTE_TITULO = ("Arial", 20, "bold")
FUENTE_GRANDE = ("Arial", 30, "bold")
FUENTE_SUBTITULO = ("Arial", 16, "bold")
FUENTE = ("Arial", 11)
FUENTE_NEGRITA = ("Arial", 11, "bold")
FUENTE_CHICA = ("Arial", 10)
FUENTE_MENU = ("Arial", 11)
FUENTE_TABLA = ("Arial", 10)

# ── Logo ───────────────────────────────────────────────────────
# Cada grupo guarda su logo como club/logo.png; si el archivo no
# existe, la interfaz muestra el nombre del club en texto.
RUTA_LOGO = Path(__file__).parent.parent / "multimedia" / "imagenes" / "river_logo.png"