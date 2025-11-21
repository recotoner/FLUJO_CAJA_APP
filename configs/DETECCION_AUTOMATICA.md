# 🔍 Detección Automática de Cliente

## ¿Cómo funciona?

El sistema detecta automáticamente qué cliente está accediendo basándose en el **nombre del archivo de datos** que cargas.

## Patrones de Nombres de Archivo

El sistema busca estos patrones en el nombre del archivo:

### Patrones Soportados:

1. **`cliente_[nombre]_*.xlsx`**
   - Ejemplo: `cartola_cliente_a_junio_2025.xlsx` → Detecta: `cliente_a`
   - Ejemplo: `cliente_b_datos.xlsx` → Detecta: `cliente_b`

2. **`empresa_[nombre]_*.xlsx`**
   - Ejemplo: `datos_empresa_xyz.xlsx` → Detecta: `empresa_xyz`

3. **`[nombre]_cartola.xlsx`**
   - Ejemplo: `cliente_c_cartola.xlsx` → Detecta: `cliente_c`

4. **`cartola_[nombre]_*.xlsx`**
   - Ejemplo: `cartola_empresa_abc.xlsx` → Detecta: `empresa_abc`

5. **`[nombre]_datos.xlsx`**
   - Ejemplo: `sucursal_norte_datos.xlsx` → Detecta: `sucursal_norte`

## Mapeo con Configuraciones

Una vez detectado el nombre del cliente, el sistema busca automáticamente un archivo de configuración que coincida:

### Nombres de Configuración Esperados:

- `clasificadores_[nombre_cliente].json`
- `clasificadores_[nombre_cliente].xlsx`

### Ejemplos:

| Archivo de Datos | Cliente Detectado | Configuración Buscada |
|------------------|-------------------|------------------------|
| `cartola_cliente_a_junio.xlsx` | `cliente_a` | `clasificadores_cliente_a.json` o `clasificadores_cliente_a.xlsx` |
| `datos_empresa_xyz.xlsx` | `empresa_xyz` | `clasificadores_empresa_xyz.json` o `clasificadores_empresa_xyz.xlsx` |
| `cliente_b_cartola.xlsx` | `cliente_b` | `clasificadores_cliente_b.json` o `clasificadores_cliente_b.xlsx` |

## Flujo de Detección

1. **Usuario carga archivo**: `cartola_cliente_a_junio_2025.xlsx`
2. **Sistema detecta**: `cliente_a` desde el nombre del archivo
3. **Sistema busca**: `clasificadores_cliente_a.json` o `clasificadores_cliente_a.xlsx`
4. **Si encuentra**: Carga automáticamente esa configuración
5. **Si no encuentra**: Muestra selector manual con todas las configuraciones disponibles

## Selección Manual

Si la detección automática no funciona o prefieres seleccionar manualmente:

1. El selector en la barra lateral muestra todas las configuraciones disponibles
2. Puedes cambiar la selección en cualquier momento
3. La selección se recuerda durante la sesión

## Recomendaciones de Nomenclatura

Para que la detección automática funcione mejor:

### ✅ Nombres Recomendados:
- `cartola_cliente_a_junio_2025.xlsx`
- `datos_empresa_xyz_2025.xlsx`
- `cliente_b_cartola.xlsx`
- `empresa_abc_datos.xlsx`

### ❌ Nombres que NO se detectan bien:
- `cartola_junio_2025.xlsx` (sin nombre de cliente)
- `datos.xlsx` (muy genérico)
- `archivo_123.xlsx` (sin patrón reconocible)

## Configuración Manual por Cliente

Si tienes archivos con nombres que no siguen los patrones, puedes:

1. **Renombrar los archivos** para seguir los patrones recomendados
2. **Usar el selector manual** en la barra lateral
3. **Crear un mapeo personalizado** editando el código (avanzado)

## Ubicación de Archivos

### Archivos de Datos:
- Pueden estar en cualquier ubicación accesible
- Se especifican en el campo "Nombre del archivo Excel"

### Archivos de Configuración:
- Directorio `configs/` (recomendado)
- O directorio raíz del proyecto

## Ejemplo Completo

```
📁 Proyecto/
├── 📄 flujo_caja_app.py
├── 📁 configs/
│   ├── 📄 clasificadores_cliente_a.xlsx
│   ├── 📄 clasificadores_cliente_b.json
│   └── 📄 clasificadores_empresa_xyz.xlsx
└── 📁 datos/
    ├── 📊 cartola_cliente_a_junio_2025.xlsx
    ├── 📊 cartola_cliente_b_julio_2025.xlsx
    └── 📊 datos_empresa_xyz_2025.xlsx
```

**Flujo:**
1. Usuario carga: `datos/cartola_cliente_a_junio_2025.xlsx`
2. Sistema detecta: `cliente_a`
3. Sistema carga: `configs/clasificadores_cliente_a.xlsx` automáticamente
4. ✅ Todo funciona sin intervención manual


