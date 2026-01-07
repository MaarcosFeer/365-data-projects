from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models, database

# 1. Crear las tablas en la base de datos automáticamente al iniciar
# Esto le dice a SQLAlchemy: "Si no existen las tablas, créalas ahora".
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="API de Inventario", description="Día 3: FastAPI + Docker + Postgres")

# 2. Esquema de validación (Pydantic)
# Define qué datos esperamos recibir del usuario
class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int

# 3. RUTA: Crear un producto nuevo (POST)
@app.post("/productos/", summary="Crear nuevo producto")
def crear_producto(producto: ProductoCreate, db: Session = Depends(database.get_db)):
    # Convertimos el JSON recibido en un objeto de Base de Datos
    nuevo_producto = models.Producto(**producto.dict())
    
    # Guardamos en la BD
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto) # Recargamos para obtener el ID generado
    
    return nuevo_producto

# 4. RUTA: Leer productos (GET)
@app.get("/productos/", summary="Listar inventario")
def leer_productos(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    # Consulta SQL equivalente a: SELECT * FROM productos LIMIT 100
    productos = db.query(models.Producto).offset(skip).limit(limit).all()
    return productos

# 5. Ruta Raíz
@app.get("/")
def root():
    return {"mensaje": "¡La API de Inventario está funcionando en Docker! 🐳"}