# 📚 Base de Datos - Guía Simple

## 🎯 No necesitas saber SQLite

Todo está configurado para que **no tengas que preocuparte** por los detalles técnicos.

---

## 📁 Archivos

- `connection.py` - Conexión a la base de datos (automático)
- `models.py` - Estructura de las tablas (como "cajas" para guardar datos)
- `init_db.py` - Script para crear la base de datos (ejecutar UNA VEZ)

---

## 🚀 Inicialización (UNA SOLA VEZ)

Para crear la base de datos, ejecuta:

```bash
python database/init_db.py
```

Esto creará el archivo `database/flujo_caja.db` automáticamente.

**¡Eso es todo!** No necesitas hacer nada más.

---

## 💡 ¿Qué es SQLite?

SQLite es como un Excel pero para programas:
- ✅ Se guarda como un archivo: `flujo_caja.db`
- ✅ No necesitas instalar nada (viene con Python)
- ✅ Funciona automáticamente
- ✅ Fácil de respaldar (solo copiar el archivo)

**No necesitas saber cómo funciona** - yo me encargo de todo.

---

## 🔧 Uso en el Código

Cuando necesites guardar o leer datos, usarás funciones simples como:

```python
# Guardar un usuario
crear_usuario(email="cliente@ejemplo.com", nombre="Empresa XYZ")

# Leer transacciones
transacciones = obtener_transacciones(usuario_id=1)

# Guardar clasificador
agregar_clasificador(usuario_id=1, nombre="PROVEEDORES", ...)
```

**No necesitas escribir SQL** - todo está en funciones simples.

---

## 📊 Estructura de Datos

La base de datos tiene estas "cajas" (tablas):

1. **usuarios** - Información de cada cliente
2. **clasificadores** - Reglas de clasificación
3. **mapeo_columnas** - Configuración de columnas por banco
4. **archivos_cargados** - Registro de archivos subidos
5. **transacciones** - Movimientos bancarios
6. **alertas** - Notificaciones

---

## 🔄 Respaldo

Para respaldar la base de datos, simplemente copia el archivo:

```bash
copy database/flujo_caja.db database/flujo_caja_backup.db
```

¡Así de simple!

---

## ❓ ¿Preguntas?

Si necesitas algo, solo pregunta. Todo está diseñado para ser simple y automático.


