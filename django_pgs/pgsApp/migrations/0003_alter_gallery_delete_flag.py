"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pgsApp", "0002_alter_gallery_options_gallery_delete_flag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="delete_flag",
            field=models.IntegerField(default=0),
        ),
    ]
