# Generated by Django 4.0.1 on 2022-01-24 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recordproduksi', '0002_remove_rencanaproduksi_part_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hasilproduksi',
            old_name='id_rencana_produksi',
            new_name='rencana_produksi',
        ),
        migrations.RemoveField(
            model_name='hasilproduksi',
            name='part_number',
        ),
        migrations.RemoveField(
            model_name='hasilproduksi',
            name='qty',
        ),
        migrations.AlterField(
            model_name='rencanaproduksidetail',
            name='line_number',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='HasilProduksiDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('hasil_produksi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='recordproduksi.hasilproduksi')),
                ('part_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordproduksi.barang')),
            ],
        ),
    ]
