from django.shortcuts import render
from clients.models import Clients
from records.models import Records
from django.shortcuts import render, redirect
from .forms import RecordForm
from django.http import HttpResponse

def edit_record_info(request, record_id):
    data = {}

    if 'save_record_info' in request.POST:  # проверяем была ли нажата кнопочка с name = save_account_info в post запросе
        info = request.POST
        Records.objects.filter(id=record_id).update(procedure_name=info['procedure_name'],
                                                    cabinet=info['cabinet'],
                                                    price=info['price'],
                                                    datetime=info['datetime'])
        data['record'] = Records.objects.filter(id=record_id).values()
        return redirect('view_client_info', data['record'][0]['client_id_id'])

    data['record'] = Records.objects.filter(id=record_id).values()
    data['record_form'] = RecordForm(data=data['record'][0])  # указываем в data значение из базы, чтобы автоматом выставлялись в поля
    return render(request, 'records/edit.html', data)

def add_record(request, client_id):
    if request.method == 'POST':
        info = request.POST
        new_record = Records(procedure_name=info['procedure_name'],
                            client_id=Clients(client_id),
                            cabinet=info['cabinet'],
                            price=info['price'],
                            datetime=info['datetime'])
        new_record.save()
        return redirect('view_client_info', client_id)

    data = {}
    data['record_form'] = RecordForm()  # указываем в data значение из базы, чтобы автоматом выставлялись в поля
    return render(request, 'records/add.html', data)
