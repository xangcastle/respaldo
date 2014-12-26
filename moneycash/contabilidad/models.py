from moneycash.models import Poliza as base_poliza,\
DetallePoliza as base_detalle_poliza#, poliza_producto as base_producto


class Factura(base_detalle_poliza):
    class Meta:
        proxy = True
        verbose_name_plural = "facturas incluidas en la poliza"


#class Producto(base_producto):
    #class Meta:
        #proxy = True
        #verbose_name_plural = "productos incluidos en la poliza"


class Poliza(base_poliza):
    class Meta:
        proxy = True
        verbose_name_plural = "liquidacion de polizas"