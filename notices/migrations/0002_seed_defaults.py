from django.db import migrations


def seed_defaults(apps, schema_editor):
    Institution = apps.get_model('notices', 'Institution')
    Category = apps.get_model('notices', 'Category')
    Department = apps.get_model('notices', 'Department')

    Institution.objects.get_or_create(
        pk=1,
        defaults={
            'name': 'CampusConnect Academy',
            'tagline': 'Everything your campus needs to communicate better',
            'primary_color': '#3157f6',
        },
    )

    categories = [
        ('Academic', '📚', '#3157f6'),
        ('Examinations', '📝', '#7c3aed'),
        ('Events', '🎉', '#db2777'),
        ('Placements', '💼', '#059669'),
        ('Sports', '🏆', '#ea580c'),
        ('Emergency', '🚨', '#dc2626'),
    ]
    for name, icon, color in categories:
        Category.objects.get_or_create(name=name, defaults={'icon': icon, 'color': color})

    departments = [
        ('Computer Science and Engineering', 'CSE'),
        ('Electronics and Communication Engineering', 'ECE'),
        ('Mechanical Engineering', 'ME'),
        ('Civil Engineering', 'CE'),
        ('Administration', 'ADMIN'),
    ]
    for name, short_name in departments:
        Department.objects.get_or_create(name=name, defaults={'short_name': short_name})


def remove_defaults(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [('notices', '0001_initial')]
    operations = [migrations.RunPython(seed_defaults, remove_defaults)]
