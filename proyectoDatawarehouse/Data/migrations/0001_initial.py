# Generated by Django 3.0.2 on 2020-01-24 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCaracteristica', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCategoria', models.TextField(default='')),
                ('DescripcionCategoria', models.TextField(default='')),
                ('CategoriaPadre', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comercio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreComercio', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreProducto', models.TextField(default='')),
                ('DescripcionProducto', models.TextField(default='')),
                ('TipoProducto', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='RubroComercio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreRubro', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCodigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCodigo', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='UnidaddeMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreMedida', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ValorMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Valormedida', models.TextField(default='')),
                ('productoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.Producto')),
                ('unidadID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.UnidaddeMedida')),
            ],
        ),
        migrations.CreateModel(
            name='ValorCodigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoProducto', models.TextField(default='')),
                ('productoID', models.ManyToManyField(to='Data.Producto')),
                ('tipoID', models.ManyToManyField(to='Data.TipoCodigo')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreSucursal', models.TextField(default='')),
                ('DireccionSucursal', models.TextField(default='')),
                ('PaisSucursal', models.TextField(default='')),
                ('comercioID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.Comercio')),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoPrecio', models.TextField(default='')),
                ('ValoPrecio', models.TextField(default='')),
                ('SucursalID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.Sucursal')),
                ('productoID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Data.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='comercio',
            name='RubroID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.RubroComercio'),
        ),
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoriaID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Data.Categoria')),
                ('productoID', models.ManyToManyField(to='Data.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='CaracteristicaDeProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ValorCaracteristica', models.TextField(default='')),
                ('CaracteristicaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.Caracteristica')),
                ('productoID', models.ManyToManyField(to='Data.Producto')),
            ],
        ),
    ]
