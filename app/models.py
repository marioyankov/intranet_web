from django.db import models
from django.utils import timezone


PLACE_OF_WORK_CHOICES = [
        ('Plovdiv', 'Plovdiv'),
        ('Graf Ignatievo', 'Graf Ignatievo'),
        ('Krumovo', 'Krumovo'),
    ]

STRUCTURAL_UNIT_CHOICES = [
    ('Търговска дирекция', 'Търговска дирекция'),
    ('Управление', 'Управление'),
    ('Финансово-икономическа дирекция', 'Финансово-икономическа дирекция'),
    ('Ремонт агрегати/Звено мех.', 'Ремонт агрегати/Звено мех.'),
    ('Офис КИС ЛИС', 'Офис КИС ЛИС'),
    ('Административна дирекция', 'Административна дирекция'),
    ('Дирекция Качество', 'Дирекция Качество'),
]

INTERNET_CHOICES = [
    ('Y', 'Да'),
    ('N', 'Не'),
]

SHARES_ACCESS_CHOICES = [
    ('none', 'none'),
    ('Off', 'Off'),
    ('OFI', 'OFI'),
    ('IT', 'IT'),
    ('oldpcs', 'oldpcs'),
]


class Employee(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=70)
    internet = models.CharField(max_length=5, choices=INTERNET_CHOICES, default='N')
    shares_access = models.CharField(max_length=10, choices=SHARES_ACCESS_CHOICES, default='none')
    place_of_work = models.CharField(max_length=32, choices = PLACE_OF_WORK_CHOICES, default = 'Plovdiv')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Toner(models.Model):
    manufacturer = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    quantity = models.IntegerField()
    recomended_quantity = models.IntegerField()
    document = models.FileField(upload_to='uploads/%Y%m%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.model}'

class Drum(models.Model):
    manufacturer = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    quantity = models.IntegerField()
    recomended_quantity = models.IntegerField()
    document = models.FileField(upload_to='uploads/%Y%m%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.model}'

class Computer(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default=None)
    manufacturer = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    # catch django.db.integrityError if its not unique
    serial_number = models.CharField(max_length=32, unique=True)
    cpu = models.CharField(max_length=20)
    ram = models.CharField(max_length=10)
    drive = models.CharField(max_length=20)
    video_card = models.CharField(max_length=20)
    mac_address = models.CharField(max_length=20)
    document = models.FileField(upload_to='uploads/%Y%m%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.user} PC'

class Monitor(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default=None)
    manufacturer = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    # catch django.db.integrityError if its not unique
    serial_number = models.CharField(max_length=32, unique=True)
    size = models.CharField(max_length=10)
    ports = models.CharField(max_length=50)
    document = models.FileField(upload_to='uploads/%Y%m%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.user} Monitor'

class Laptop(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default=None)
    manufacturer = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    # catch django.db.integrityError if its not unique
    serial_number = models.CharField(max_length=32, unique=True)
    cpu = models.CharField(max_length=20)
    ram = models.CharField(max_length=10)
    video_card = models.CharField(max_length=20)
    drive = models.CharField(max_length=20)
    mac_address = models.CharField(max_length=20)
    wifi_mac_address = models.CharField(max_length=20)
    document = models.FileField(upload_to='uploads/%Y%m%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.user} Laptop'

class Printer(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default=None)
    manufacturer = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    # catch django.db.integrityError if its not unique
    serial_number = models.CharField(max_length=32, unique=True)
    toner = models.ForeignKey(Toner, on_delete=models.SET_DEFAULT, default=None)
    drum = models.ForeignKey(Drum, on_delete=models.SET_DEFAULT, default=None)
    mac_address = models.CharField(max_length=20)
    document = models.FileField(upload_to='uploads/%Y%m%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.user} Printer'

class Request(models.Model):
    CARTRIDGE_CHOICES = list(Toner.objects.values_list('model','model'))
    cartridge_name = models.CharField(max_length=150, choices=CARTRIDGE_CHOICES, default='none')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cartridge_name