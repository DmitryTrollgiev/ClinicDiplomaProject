from django.db import models


# Create your models here.
class Clients(models.Model):
    name = models.CharField("Имя", max_length=10000, null=True)
    sex = models.TextField("Пол", null=True)
    polis = models.IntegerField("ПОЛИС ОМС", null=True)
    passport_number = models.TextField("Серия и номер паспорта", null=True)
    phone = models.IntegerField("Телефон", null=True)
    age = models.IntegerField("Возраст", null=True)
    mail = models.TextField("Почта", null=True)
    # status = models.IntegerField("Статус", default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        db_table = "clients"
