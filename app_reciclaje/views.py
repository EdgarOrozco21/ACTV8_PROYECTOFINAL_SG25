from django.shortcuts import render, redirect, get_object_or_404
from .models import MaterialReciclable, CentroAcopio, Donante, EmpleadoReciclaje, RecepcionMaterial

def home(request):
    return render(request, 'home.html')

# ==========================================
# VISTAS: MaterialReciclable
# ==========================================
def ver_materiales(request):
    materiales = MaterialReciclable.objects.all()
    return render(request, 'material/ver_materiales.html', {'materiales': materiales})

def agregar_material(request):
    if request.method == 'POST':
        MaterialReciclable.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST.get('descripcion', ''),
            tipo_material=request.POST.get('tipo_material', 'No especificado'),
            precio_por_kg=request.POST.get('precio_por_kg', 0.00),
            unidad_medida=request.POST.get('unidad_medida', 'kg'),
            es_toxico='es_toxico' in request.POST,
            punto_acopio_recomendado=request.POST.get('punto_acopio_recomendado', ''),
            codigo_identificacion=request.POST.get('codigo_identificacion')
        )
        return redirect('ver_materiales')
    return render(request, 'material/agregar_material.html')

def editar_material(request, material_id):
    material = get_object_or_404(MaterialReciclable, id=material_id)
    if request.method == 'POST':
        material.nombre = request.POST['nombre']
        material.descripcion = request.POST.get('descripcion', '')
        material.tipo_material = request.POST.get('tipo_material', 'No especificado')
        material.precio_por_kg = request.POST.get('precio_por_kg', 0.00)
        material.unidad_medida = request.POST.get('unidad_medida', 'kg')
        material.es_toxico = 'es_toxico' in request.POST
        material.punto_acopio_recomendado = request.POST.get('punto_acopio_recomendado', '')
        material.codigo_identificacion = request.POST.get('codigo_identificacion')
        material.save()
        return redirect('ver_materiales')
    return render(request, 'material/editar_material.html', {'material': material})

def borrar_material(request, material_id):
    material = get_object_or_404(MaterialReciclable, id=material_id)
    if request.method == 'POST':
        material.delete()
        return redirect('ver_materiales')
    return render(request, 'material/borrar_material.html', {'material': material})

# ==========================================
# VISTAS: CentroAcopio
# ==========================================
def ver_centros(request):
    centros = CentroAcopio.objects.all()
    return render(request, 'centro_acopio/ver_centros.html', {'centros': centros})

def agregar_centro(request):
    if request.method == 'POST':
        CentroAcopio.objects.create(
            nombre=request.POST['nombre'],
            direccion=request.POST.get('direccion', ''),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            horario_atencion=request.POST.get('horario_atencion', 'No especificado'),
            capacidad_toneladas=request.POST.get('capacidad_toneladas', 0.00),
            latitud=request.POST.get('latitud'),
            longitud=request.POST.get('longitud')
        )
        return redirect('ver_centros')
    return render(request, 'centro_acopio/agregar_centro.html')

def editar_centro(request, centro_id):
    centro = get_object_or_404(CentroAcopio, id=centro_id)
    if request.method == 'POST':
        centro.nombre = request.POST['nombre']
        centro.direccion = request.POST.get('direccion', '')
        centro.telefono = request.POST.get('telefono')
        centro.email = request.POST.get('email')
        centro.horario_atencion = request.POST.get('horario_atencion', 'No especificado')
        centro.capacidad_toneladas = request.POST.get('capacidad_toneladas', 0.00)
        centro.latitud = request.POST.get('latitud')
        centro.longitud = request.POST.get('longitud')
        centro.save()
        return redirect('ver_centros')
    return render(request, 'centro_acopio/editar_centro.html', {'centro': centro})

def borrar_centro(request, centro_id):
    centro = get_object_or_404(CentroAcopio, id=centro_id)
    if request.method == 'POST':
        centro.delete()
        return redirect('ver_centros')
    return render(request, 'centro_acopio/borrar_centro.html', {'centro': centro})

# ==========================================
# VISTAS: Donante
# ==========================================
def ver_donantes(request):
    donantes = Donante.objects.all()
    return render(request, 'donante/ver_donantes.html', {'donantes': donantes})

def agregar_donante(request):
    if request.method == 'POST':
        Donante.objects.create(
            nombre=request.POST['nombre'],
            tipo_donante=request.POST.get('tipo_donante', 'Persona'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            direccion_donante=request.POST.get('direccion_donante'),
            ruc_dni=request.POST.get('ruc_dni'),
            es_anonimo='es_anonimo' in request.POST
        )
        return redirect('ver_donantes')
    return render(request, 'donante/agregar_donante.html')

def editar_donante(request, donante_id):
    donante = get_object_or_404(Donante, id=donante_id)
    if request.method == 'POST':
        donante.nombre = request.POST['nombre']
        donante.tipo_donante = request.POST.get('tipo_donante', 'Persona')
        donante.telefono = request.POST.get('telefono')
        donante.email = request.POST.get('email')
        donante.direccion_donante = request.POST.get('direccion_donante')
        donante.ruc_dni = request.POST.get('ruc_dni')
        donante.es_anonimo = 'es_anonimo' in request.POST
        donante.save()
        return redirect('ver_donantes')
    return render(request, 'donante/editar_donante.html', {'donante': donante})

def borrar_donante(request, donante_id):
    donante = get_object_or_404(Donante, id=donante_id)
    if request.method == 'POST':
        donante.delete()
        return redirect('ver_donantes')
    return render(request, 'donante/borrar_donante.html', {'donante': donante})

# ==========================================
# VISTAS: EmpleadoReciclaje
# ==========================================
def ver_empleados(request):
    empleados = EmpleadoReciclaje.objects.all()
    return render(request, 'empleado/ver_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        centro_acopio_id = request.POST.get('centro_acopio')
        centro_acopio = get_object_or_404(CentroAcopio, id=centro_acopio_id) if centro_acopio_id else None
        EmpleadoReciclaje.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST.get('apellido', ''),
            dni=request.POST.get('dni'),
            cargo=request.POST.get('cargo', 'Operario'),
            turno=request.POST.get('turno'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            certificaciones=request.POST.get('certificaciones'),
            centro_acopio=centro_acopio
        )
        return redirect('ver_empleados')
    centros = CentroAcopio.objects.all()
    return render(request, 'empleado/agregar_empleado.html', {'centros': centros})

def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(EmpleadoReciclaje, id=empleado_id)
    if request.method == 'POST':
        centro_acopio_id = request.POST.get('centro_acopio')
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST.get('apellido', '')
        empleado.dni = request.POST.get('dni')
        empleado.cargo = request.POST.get('cargo', 'Operario')
        empleado.turno = request.POST.get('turno')
        empleado.telefono = request.POST.get('telefono')
        empleado.email = request.POST.get('email')
        empleado.certificaciones = request.POST.get('certificaciones')
        empleado.centro_acopio = get_object_or_404(CentroAcopio, id=centro_acopio_id) if centro_acopio_id else None
        empleado.save()
        return redirect('ver_empleados')
    centros = CentroAcopio.objects.all()
    return render(request, 'empleado/editar_empleado.html', {'empleado': empleado, 'centros': centros})

def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(EmpleadoReciclaje, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# ==========================================
# VISTAS: RecepcionMaterial
# ==========================================
def ver_recepciones(request):
    recepciones = RecepcionMaterial.objects.all()
    return render(request, 'recepcion/ver_recepciones.html', {'recepciones': recepciones})

def agregar_recepcion(request):
    if request.method == 'POST':
        donante_id = request.POST.get('donante')
        donante = get_object_or_404(Donante, id=donante_id) if donante_id else None
        material = get_object_or_404(MaterialReciclable, id=request.POST['material'])
        empleado = get_object_or_404(EmpleadoReciclaje, id=request.POST['empleado_recepcion'])
        
        RecepcionMaterial.objects.create(
            material=material,
            centro_acopio=empleado.centro_acopio,
            donante=donante,
            cantidad_kg=request.POST['cantidad_kg'],
            estado_material=request.POST.get('estado_material', 'Recibido'),
            observaciones=request.POST.get('observaciones'),
            empleado_recepcion=empleado
        )
        return redirect('ver_recepciones')
    
    donantes = Donante.objects.all()
    materiales = MaterialReciclable.objects.all()
    empleados = EmpleadoReciclaje.objects.all()
    return render(request, 'recepcion/agregar_recepcion.html', {
        'donantes': donantes, 
        'materiales': materiales, 
        'empleados': empleados
    })

def editar_recepcion(request, recepcion_id):
    recepcion = get_object_or_404(RecepcionMaterial, id=recepcion_id)
    if request.method == 'POST':
        donante_id = request.POST.get('donante')
        recepcion.donante = get_object_or_404(Donante, id=donante_id) if donante_id else None
        recepcion.material = get_object_or_404(MaterialReciclable, id=request.POST['material'])
        empleado = get_object_or_404(EmpleadoReciclaje, id=request.POST['empleado_recepcion'])
        recepcion.empleado_recepcion = empleado
        recepcion.centro_acopio = empleado.centro_acopio
        recepcion.cantidad_kg = request.POST['cantidad_kg']
        recepcion.estado_material = request.POST.get('estado_material', 'Recibido')
        recepcion.observaciones = request.POST.get('observaciones')
        recepcion.save()
        return redirect('ver_recepciones')
    
    donantes = Donante.objects.all()
    materiales = MaterialReciclable.objects.all()
    empleados = EmpleadoReciclaje.objects.all()
    return render(request, 'recepcion/editar_recepcion.html', {
        'recepcion': recepcion,
        'donantes': donantes, 
        'materiales': materiales, 
        'empleados': empleados
    })

def borrar_recepcion(request, recepcion_id):
    recepcion = get_object_or_404(RecepcionMaterial, id=recepcion_id)
    if request.method == 'POST':
        recepcion.delete()
        return redirect('ver_recepciones')
    return render(request, 'recepcion/borrar_recepcion.html', {'recepcion': recepcion})
