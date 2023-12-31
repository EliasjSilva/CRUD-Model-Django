# Generated by Django 4.2.6 on 2023-10-07 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], default=None, max_length=100)),
                ('date', models.DateField()),
                ('profession', models.CharField(choices=[('Font-end', 'Front-end'), ('Back-end', 'Back-end'), ('Full-Stack', 'Full-Stack'), ('Intern', 'Intern'), ('C.Security', 'C.Security')], max_length=100, null=True)),
                ('ocupation', models.CharField(choices=[('Studying', 'Studying'), ('Working', 'Working'), ('Freelancer', 'Freelancer'), ('Unemployed', 'Unemployed')], max_length=100, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('adress', models.CharField(blank=True, max_length=155, null=True)),
                ('locate', models.CharField(choices=[('Acre - Rio Branco', 'Acre - Rio Branco'), ('Alagoas - Maceió', 'Alagoas - Maceió'), ('Amapá - Macapá', 'Amapá - Macapá'), ('Amazonas - Manaus', 'Amazonas - Manaus'), ('Bahia - Salvador', 'Bahia - Salvador'), ('Ceará - Fortaleza', 'Ceará - Fortaleza'), ('Espírito Santo - Vitória', 'Espírito Santo - Vitória'), ('Goiás - Goiânia', 'Goiás - Goiânia'), ('Maranhão - São Luís', 'Maranhão - São Luís'), ('Mato Grosso - Cuiabá', 'Mato Grosso - Cuiabá'), ('Mato Grosso do Sul - Campo Grande', 'Mato Grosso do Sul - Campo Grande'), ('Minas Gerais - Belo Horizonte', 'Minas Gerais - Belo Horizonte'), ('Paraíba - João Pessoa', 'Paraíba - João Pessoa'), ('Pernambuco - Recife', 'Pernambuco - Recife'), ('Piauí - Teresina', 'Piauí - Teresina'), ('Rio de Janeiro - Rio de Janeiro', 'Rio de Janeiro - Rio de Janeiro'), ('Rio Grande do Norte - Natal', 'Rio Grande do Norte - Natal'), ('Rio Grande do Sul - Porto Alegre', 'Rio Grande do Sul - Porto Alegre'), ('Rondônia - Porto Velho', 'Rondônia - Porto Velho'), ('Roraima - Boa Vista', 'Roraima - Boa Vista'), ('Santa Catarina - Florianópolis', 'Santa Catarina - Florianópolis'), ('São Paulo - São Paulo', 'São Paulo - São Paulo'), ('Sergipe - Aracaju', 'Sergipe - Aracaju'), ('Tocantins - Palmas', 'Tocantins - Palmas'), ('Distrito Federal - Brasília', 'Distrito Federal - Brasília')], max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('github', models.URLField(blank=True, default=None, null=True)),
                ('linkedin', models.URLField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
