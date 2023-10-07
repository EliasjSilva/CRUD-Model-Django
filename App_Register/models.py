from django.db import models
from setup import settings

# Create your models here.
# from django.contrib.postgres.fields import ArrayField

# 'choices' must be an iterable containing (actual value, human readable name) tuples.
DEFAULT = 'Not Registered'

class User(models.Model):
    # id_user = models.AutoField(primary_key=True)

    GENDER = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Other', 'Other'),
    ]

    PROFESSION = [
        ('Font-end','Front-end'),
        ('Back-end','Back-end'),
        ('Full-Stack','Full-Stack'),
        ('Intern', 'Intern'),
        ('C.Security', 'C.Security'),
    ]

    OCUPATION = [
        ('Studying', 'Studying'),
        ('Working', 'Working'),
        ('Freelancer', 'Freelancer'),
        ('Unemployed', 'Unemployed'),
    ]

    TECHNOLOGIES = [
        ('Html', 'Html'),
        ('Css', 'Css'),
        ('JavaScript', 'JavaScript'),
        ('Python', 'Python'),
        ('Ruby', 'Ruby'),
        ('PHP', 'PHP'),
        ('C#', 'C#'),
        ('Java', 'Java'),
    ]


    LOCATE = [
        ('Acre - Rio Branco', 'Acre - Rio Branco'),
        ('Alagoas - Maceió', 'Alagoas - Maceió'),
        ('Amapá - Macapá', 'Amapá - Macapá'),
        ('Amazonas - Manaus', 'Amazonas - Manaus'),
        ('Bahia - Salvador', 'Bahia - Salvador'),
        ('Ceará - Fortaleza', 'Ceará - Fortaleza'),
        ('Espírito Santo - Vitória', 'Espírito Santo - Vitória'),
        ('Goiás - Goiânia', 'Goiás - Goiânia'),
        ('Maranhão - São Luís', 'Maranhão - São Luís'),
        ('Mato Grosso - Cuiabá', 'Mato Grosso - Cuiabá'),
        ('Mato Grosso do Sul - Campo Grande', 'Mato Grosso do Sul - Campo Grande'),
        ('Minas Gerais - Belo Horizonte', 'Minas Gerais - Belo Horizonte'),
        ('Paraíba - João Pessoa', 'Paraíba - João Pessoa'),
        ('Pernambuco - Recife', 'Pernambuco - Recife'),
        ('Piauí - Teresina', 'Piauí - Teresina'),
        ('Rio de Janeiro - Rio de Janeiro', 'Rio de Janeiro - Rio de Janeiro'),
        ('Rio Grande do Norte - Natal', 'Rio Grande do Norte - Natal'),
        ('Rio Grande do Sul - Porto Alegre', 'Rio Grande do Sul - Porto Alegre'),
        ('Rondônia - Porto Velho', 'Rondônia - Porto Velho'),
        ('Roraima - Boa Vista', 'Roraima - Boa Vista'),
        ('Santa Catarina - Florianópolis', 'Santa Catarina - Florianópolis'),
        ('São Paulo - São Paulo', 'São Paulo - São Paulo'),
        ('Sergipe - Aracaju', 'Sergipe - Aracaju'),
        ('Tocantins - Palmas', 'Tocantins - Palmas'),
        ('Distrito Federal - Brasília', 'Distrito Federal - Brasília'),
    ]


    # Person
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    gender = models.CharField(max_length=100, choices=GENDER, default=None)
    date = models.DateField()

    # Status
    profession = models.CharField(max_length=100, choices=PROFESSION, null=True) #default=None
    ocupation = models.CharField(max_length=100, choices=OCUPATION, null=True) #default=None
    # technologies = models.CharField(max_length=100, choices=TECHNOLOGIES, null=True ,default=None, blank=True)
    experience = models.TextField(blank=True, null=True)

    # Dados
    cpf = models.CharField(max_length= 11, null=True)
    phone = models.CharField(max_length=11, null=True)
    adress = models.CharField(max_length=155, blank=True, null=True)
    locate = models.CharField(max_length=100, choices=LOCATE) #default=None
    # ArrayField(
        # models.CharField(choices=LOCATE, max_length=100, blank=True, null=True),

    # Links
    email = models.EmailField()
    github = models.URLField(blank=True, null=True, default=None)
    linkedin = models.URLField(blank=True, null=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    # pegando o 'nome' para colocar no objeto.
    def __str__(self):
        return self.name