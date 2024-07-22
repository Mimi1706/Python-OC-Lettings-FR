from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Address',
                ),
                migrations.DeleteModel(
                    name='Letting',
                ),
                migrations.DeleteModel(
                    name='Profile',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name='address',
                    table='lettings_address',
                ),
                migrations.AlterModelTable(
                    name='letting',
                    table='lettings_letting',
                ),
                migrations.AlterModelTable(
                    name='profile',
                    table='profiles_profile',
                ),
            ],
        ),
    ]
