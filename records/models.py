from django.db import models
from clients.models import Clients
from datetime import datetime

class Records(models.Model):
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    datetime = models.DateTimeField("Время", default=datetime.now())
    procedure_name = models.TextField("Процедура", null=True)
    cabinet = models.TextField("Кабинет", null=True)
    price = models.IntegerField("Цена", null=True)
    is_payed = models.IntegerField("Оплачено", default=0)
    is_cancelled = models.IntegerField("Отменено", default=0)


    def __str__(self):
        return self.procedure_name

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        db_table = "records"
