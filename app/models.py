from datetime import datetime, timezone
import uuid
from .extensions import  db
from werkzeug.security import generate_password_hash, check_password_hash


# Modelo de tabla usuarios
class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False)
    email  = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(40), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    ultimo_acceso = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    status = db.Column(db.Boolean, default=True)
    movimientos = db.relationship("Movimientos", back_populates="usuario")

    # --- Métodos de Contraseña ---

    def set_password(self, password):
        """Genera y guarda el hash de la contraseña."""
        # Se puede llamar en el constructor o en la actualización
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica una contraseña de texto plano contra el hash guardado."""
        # Compara el hash en la DB (self.password_hash) con el texto plano provisto
        return check_password_hash(self.password_hash, password)


# Modelo de tabla movimientos
class Movimientos(db.Model):
    __tablename__ = 'movimientos'

    id_movimiento = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_producto   = db.Column(db.String(36), db.ForeignKey('productos.id_producto'), nullable=False)
    id_usuario = db.Column(db.String(36), db.ForeignKey('usuarios.id_usuario'), nullable=False)
    tipo_movimiento = db.Column(db.String(60))
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    motivo = db.Column(db.String(60))
    referencia = db.Column(db.String(80))
    fecha_movimiento = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    observaciones = db.Column(db.String(150))

    producto = db.relationship("Producto", back_populates="movimientos")
    usuario = db.relationship("Usuario", back_populates="movimientos")


# Modelo de tabla productos
class Producto (db.Model):
    __tablename__ = 'productos'

    id_producto = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre_producto = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(150), nullable=False)
    codigo_barras = db.Column(db.String(50), unique=True, nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock_minimo = db.Column(db.Integer, nullable=False)
    stock_actual = db.Column(db.Integer, nullable=False)
    id_categoria = db.Column(db.String(36), db.ForeignKey('categorias.id_categoria'),nullable=False)
    imagen_url = db.Column(db.String(200))
    fecha_creacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    fecha_actualizacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    status = db.Column(db.Boolean, default=True)

    categoria = db.relationship("Categoria", back_populates="productos")
    movimientos = db.relationship("Movimientos", back_populates="producto")
    proveedores = db.relationship("ProductoProveedor", back_populates="producto")


# Modelo de tabla categoria
class Categoria (db.Model):
    __tablename__ = 'categorias'

    id_categoria = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre_categoria = db.Column(db.String(100), unique=True ,nullable=False)
    descripcion_cat = db.Column(db.String(150), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    status = db.Column(db.Boolean, default=True)
    productos = db.relationship("Producto", back_populates="categoria")

# Modelo de tabla producto_proveedor
class ProductoProveedor(db.Model):
    __tablename__ = 'producto_proveedor'

    id_producto_proveedor = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_producto = db.Column(db.String(36), db.ForeignKey('productos.id_producto'), nullable=False)
    id_proveedor = db.Column(db.String(36), db.ForeignKey('proveedor.id_proveedor'), nullable=False)
    precio_compra = db.Column(db.Numeric(10, 2), nullable=False)
    tiempo_entrega_dias = db.Column(db.Integer)
    fecha_creacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    preferido = db.Column(db.Boolean)

    producto = db.relationship("Producto", back_populates="proveedores")
    proveedor = db.relationship("Proveedor", back_populates="productos")


# Modelo de tabla proveedor
class Proveedor (db.Model):
    __tablename__ = 'proveedor'

    id_proveedor = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre_proveedor = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    direccion = db.Column(db.String(150), unique=True, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    status = db.Column(db.Boolean, default=True)
    productos = db.relationship("ProductoProveedor", back_populates="proveedor")



class TokenBlocklist(db.Model):
    __tablename__ = "token_blocklist"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    jti = db.Column(db.String(36), nullable=False, index=True, unique=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))







