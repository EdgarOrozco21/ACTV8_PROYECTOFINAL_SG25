from django.db import models
from django.utils import timezone

# ==========================================
# MODELO: MATERIAL_RECICLABLE
# ==========================================
class MaterialReciclable(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    # Nuevos campos
    tipo_material = models.CharField(max_length=50, default='No especificado')
    precio_por_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    unidad_medida = models.CharField(max_length=20, default='kg')
    es_toxico = models.BooleanField(default=False)
    punto_acopio_recomendado = models.CharField(max_length=255, blank=True, null=True)
    codigo_identificacion = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: CENTRO_ACOPIO
# ==========================================
class CentroAcopio(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    encargado = models.CharField(max_length=100, blank=True, null=True) # Permitir nulos
    horario = models.CharField(max_length=255, blank=True, null=True) # Permitir nulos
    # Nuevos campos
    email = models.EmailField(max_length=100, blank=True, null=True)
    horario_atencion = models.CharField(max_length=255, default='No especificado')
    capacidad_toneladas = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: DONANTE
# ==========================================
class Donante(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True) # Se mantiene por consistencia
    direccion = models.CharField(max_length=255, blank=True, null=True)
    # Nuevos campos
    tipo_donante = models.CharField(max_length=50, default='Persona')
    email = models.EmailField(max_length=100, blank=True, null=True) # Campo nuevo solicitado
    direccion_donante = models.CharField(max_length=255, blank=True, null=True)
    ruc_dni = models.CharField(max_length=20, blank=True, null=True, unique=True)
    fecha_registro = models.DateTimeField(default=timezone.now)
    es_anonimo = models.BooleanField(default=False)


    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: EMPLEADO_RECICLAJE
# ==========================================
class EmpleadoReciclaje(models.Model):
    nombre = models.CharField(max_length=255)
    puesto = models.CharField(max_length=100, blank=True, null=True) # Se mantiene
    turno = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True) # Se mantiene
    centro_acopio = models.ForeignKey(CentroAcopio, on_delete=models.CASCADE, null=True) # Permitir nulo temporalmente
    # Nuevos campos
    apellido = models.CharField(max_length=255, default='')
    dni = models.CharField(max_length=20, blank=True, null=True, unique=True)
    fecha_contratacion = models.DateTimeField(default=timezone.now)
    cargo = models.CharField(max_length=100, default='Operario')
    email = models.EmailField(max_length=100, blank=True, null=True) # Campo nuevo solicitado
    certificaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: RECEPCION_MATERIAL
# ==========================================
class RecepcionMaterial(models.Model):
    material = models.ForeignKey(MaterialReciclable, on_delete=models.CASCADE)
    cantidad_kg = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(default=timezone.now) # Se mantiene, se usará el nuevo campo
    donante = models.ForeignKey(Donante, on_delete=models.CASCADE, null=True, blank=True)
    centro_acopio = models.ForeignKey(CentroAcopio, on_delete=models.CASCADE)
    empleado_recepcion = models.ForeignKey(EmpleadoReciclaje, on_delete=models.SET_NULL, null=True, blank=True)
    # Nuevos campos
    fecha_recepcion = models.DateTimeField(default=timezone.now)
    estado_material = models.CharField(max_length=100, default='Recibido')
    observaciones = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"Recepción de {self.cantidad_kg} kg de {self.material.nombre}"

# ==========================================
# MODELO: PROCESAMIENTO_MATERIAL
# =========================================
class ProcesamientoMaterial(models.Model):
    recepcion = models.ForeignKey(RecepcionMaterial, on_delete=models.CASCADE)
    tipo_proceso = models.CharField(max_length=100)
    fecha_proceso = models.DateField()
    empleado = models.ForeignKey(EmpleadoReciclaje, on_delete=models.CASCADE)

    def __str__(self):
        return f"Procesamiento de {self.recepcion.material.nombre}"

# ==========================================
# MODELO: VENTA_MATERIAL
# ==========================================
class VentaMaterial(models.Model):
    material = models.ForeignKey(MaterialReciclable, on_delete=models.CASCADE)
    cantidad_vendida = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    centro_acopio = models.ForeignKey(CentroAcopio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta de {self.material.nombre}"
