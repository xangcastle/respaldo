from moneycash.apps.facturacion.admin import admin,factura_admin,documento_admin
from moneycash.apps.caja.models import Factura,no_impresas, Recibo, CierreCaja,\
    Deposito, pago_efectivo, pago_cheque, pago_tarjeta, pago_credito,\
    pago_transferencia, abonos_factura
   
class deposito_tabular(admin.TabularInline):
    model = Deposito
    fields = ('fecha','banco','monto','numero')
    extra = 1
    classes = ('grp-collapse grp-open',)
    
class factura_tabular(admin.TabularInline):
    model = Factura
    extra = 0
    classes = ('grp-collapse grp-open',)
    fields = ('numero','nombre','total')
    
class efectivo_tabular(admin.TabularInline):
    model = pago_efectivo
    extra = 1
    classes = ('grp-collapse grp-open',)
    fields = ('monto','moneda')
    
class cheque_tabular(admin.TabularInline):
    model = pago_cheque
    extra = 1
    classes = ('grp-collapse grp-closed',)
    fields = ('monto','moneda','banco','numero_cheque')
    
class tarjeta_tabular(admin.TabularInline):
    model = pago_tarjeta
    extra = 1
    classes = ('grp-collapse grp-closed',)
    fields = ('monto','moneda','banco')
    
class credito_tabular(admin.TabularInline):
    model = pago_credito
    extra = 1
    classes = ('grp-collapse grp-closed',)
    fields = ('monto','moneda','banco','cuenta')
    
class transferencia_tabular(admin.TabularInline):
    model = pago_transferencia
    extra = 1
    classes = ('grp-collapse grp-closed',)
    fields = ('monto','moneda','banco','numero_transferencia')
    
class abonos_factura(admin.TabularInline):
    model = abonos_factura
    extra = 1
    classes = ('grp-collapse grp-closed',)
    fields = ('factura','total','monto','saldo')
    
class recibo_admin(documento_admin):
    fieldsets = (
        ('Datos Principales', {
        'classes': ('grp-collapse grp-open',),
        'fields': (('fecha', 'numero'),('cliente','nombre'),'concepto','monto')
        }),
        
    )
    inlines = [efectivo_tabular,cheque_tabular,tarjeta_tabular,transferencia_tabular,abonos_factura]
    
    
class no_impresas_admin(admin.ModelAdmin):
    list_display = ('nombre','subtotal','descuento','iva','total')
    fields = (('numero','nombre'),('alcaldia','retencion_ir'),'subtotal','descuento','iva','total')
    inlines = [efectivo_tabular,tarjeta_tabular,credito_tabular]
    
class cierre_caja_admin(documento_admin):
    list_display = ('numero','fecha','user','caja','sucursal')
    fields =  (('numero','fecha','user'),('saldo_inicial','saldo_final'),('caja','sucursal'),)
    inlines = [deposito_tabular,factura_tabular]
    
admin.site.register(Factura,factura_admin)
admin.site.register(no_impresas,no_impresas_admin)
admin.site.register(Recibo,recibo_admin)
admin.site.register(CierreCaja,cierre_caja_admin)