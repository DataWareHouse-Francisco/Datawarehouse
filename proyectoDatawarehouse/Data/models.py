from django.db import models

# Create your models here.


class UnidaddeMedida(models.Model):

	NombreMedida=models.TextField(default='')
	def __str__(self):
		return self.NombreMedida
class Producto(models.Model):

	NombreProducto=models.TextField(default='')
	DescripcionProducto=models.TextField(default='')
	TipoProducto=models.TextField(default='')

	def	__str__(self):
		return self.NombreProducto
class ValorMedida(models.Model):

	Valormedida=models.TextField(default='')
	unidadID=models.ForeignKey(UnidaddeMedida, on_delete=models.CASCADE)
	productoID=models.ForeignKey(Producto,on_delete=models.CASCADE)
	def __str__(self):
		return "%s %s(s)" % (self.Valormedida,self.unidadID)

class Caracteristica(models.Model):
	NombreCaracteristica=models.TextField(default='')
	def __str__(self):
		return self.NombreCaracteristica

class CaracteristicaDeProducto(models.Model):
	ValorCaracteristica=models.TextField(default='')
	CaracteristicaID=models.ForeignKey(Caracteristica,on_delete=models.CASCADE)
	productoID=models.ManyToManyField(Producto)

	def __str__(self):
		return	"caracteristica %s: %s de %s" %(self.CaracteristicaID,self.ValorCaracteristica,self.productoID)


class Categoria(models.Model):
	NombreCategoria=models.TextField(default='')
	DescripcionCategoria=models.TextField(default='')
	CategoriaPadre=models.BooleanField(default=False)

	def __str__(self):
		return self.NombreCategoria
class CategoriaProducto(models.Model):
	productoID=models.ManyToManyField(Producto)
	categoriaID=models.OneToOneField(Categoria,on_delete=models.CASCADE)
	def __str__(self):
		return "%s de %s" %(self.productoID,self.categoriaID)

class TipoCodigo(models.Model):
	NombreCodigo=models.TextField(default='')
	def __str__(self):
		return self.NombreCodigo


class ValorCodigo(models.Model):
	CodigoProducto=models.TextField(default='')
	productoID=models.ManyToManyField(Producto)
	tipoID=models.ManyToManyField(TipoCodigo)
	def __str__(self):
	 	return "codigo %s: %s de %s"%(self.tipoID,self.CodigoProducto,self.productoID)
class RubroComercio(models.Model):
	NombreRubro=models.TextField(default='')
	def __str__(self):
		return self.NombreRubro

class Comercio(models.Model):
	NombreComercio=models.TextField(default='')
	RubroID=models.ForeignKey(RubroComercio,on_delete=models.CASCADE)
	def __str__(delf):
		return self.NombreComercio
class Sucursal(models.Model):
	NombreSucursal=models.TextField(default='')
	DireccionSucursal=models.TextField(default='')
	PaisSucursal=models.TextField(default='')
	comercioID=models.ForeignKey(Comercio,on_delete=models.CASCADE)

	def __str__(self):
		return "sucursal %s: de %s"%(self.NombreSucursal,self.PaisSucursal)

class Precio(models.Model):
	TipoPrecio=models.TextField(default='')
	ValoPrecio=models.TextField(default='')
	productoID=models.OneToOneField(Producto,on_delete=models.CASCADE)
	SucursalID=models.ForeignKey(Sucursal,on_delete=models.CASCADE)

	def __str__(self):
		return "precio %s: de %s" %(self.ValoPrecio,self.productoID)


