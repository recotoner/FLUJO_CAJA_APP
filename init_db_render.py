"""
Script para inicializar la base de datos en Render/PostgreSQL.

Este script se ejecuta al iniciar el servicio en Render (gracias al Start Command):
bash -c "python init_db_render.py && streamlit run flujo_caja_app.py --server.port $PORT --server.address 0.0.0.0"

Objetivos:
1. Verificar que DATABASE_URL está configurada.
2. Crear todas las tablas definidas en Base (incluye 'usuarios').
3. Ejecutar, si existe, la lógica de seed (init_db) para crear usuario admin, etc.
"""

import os
import sys
import inspect

from database.connection import engine, SessionLocal
from database.models import Base, Usuario  # <-- añadimos Usuario


# Intentar importar la función init_db desde donde corresponda.
# Primero desde database.init_db (más canónico), luego desde database.connection como fallback.
seed_db = None
try:
    from database.init_db import init_db as seed_db  # type: ignore
except Exception:
    try:
        from database.connection import init_db as seed_db  # type: ignore
    except Exception:
        seed_db = None


def main() -> None:
    # 1) Verificar que DATABASE_URL está configurada
    if not os.getenv("DATABASE_URL"):
        print("❌ ERROR: DATABASE_URL no está configurada")
        print("💡 Asegúrate de configurar la variable de entorno DATABASE_URL en Render")
        sys.exit(1)

    print("=" * 60)
    print("  INICIALIZANDO BASE DE DATOS EN RENDER")
    print("=" * 60)
    url_preview = os.getenv("DATABASE_URL", "")[:60]
    print(f"\n📊 Tipo de BD: PostgreSQL (Producción)")
    print(f"🔗 URL (preview): {url_preview}...\n")

    # 2) Crear todas las tablas
    print("⏳ Creando tablas con Base.metadata.create_all(bind=engine)...")
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Tablas creadas (si no existían).")
    except Exception as e:
        print(f"\n❌ ERROR al crear las tablas: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    # 3) Ejecutar lógica de seed (usuario admin, tipos por defecto, etc.), si existe
    if seed_db is not None:
        print("\n⏳ Ejecutando init_db (semilla de datos iniciales)...")
        try:
            sig = inspect.signature(seed_db)
            if len(sig.parameters) == 0:
                # init_db() sin parámetros
                seed_db()
            else:
                # init_db(db) o similar
                db = SessionLocal()
                try:
                    seed_db(db)
                finally:
                    db.close()
            print("✅ init_db ejecutado correctamente.")
        except Exception as e:
            print(f"\n⚠️ ERROR al ejecutar init_db (semilla): {e}")
            import traceback
            traceback.print_exc()
            # No abortamos el proceso: al menos las tablas ya existen
    else:
        print("\nℹ️ No se encontró función init_db; solo se crearon las tablas (sin seed).")

    # 4) DEBUG: listar usuarios que ve Render en esta conexión
    print("\n📋 Usuarios visibles desde esta conexión (PostgreSQL en Render):")
    db_debug = None
    try:
        db_debug = SessionLocal()
        users = db_debug.query(Usuario).all()
        if not users:
            print("   (sin usuarios en la tabla 'usuarios')")
        else:
            for u in users:
                # imprimimos id y email para verificar que esté, por ejemplo, hrubilar@yahoo.es
                print(f"   - {u.id} | {u.email}")
    except Exception as e:
        print(f"⚠️ No se pudo listar usuarios para debug: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if db_debug is not None:
            try:
                db_debug.close()
            except Exception:
                pass

    print("\n" + "=" * 60)
    print("✅ PROCESO DE INICIALIZACIÓN TERMINADO")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()




