from django.db.models import Q
from django.shortcuts import render
from clients.models import Clients
from records.models import Records
from django.shortcuts import render, redirect
from .forms import ClientForm


def index(request):
    if 'user_id' not in request.session:  # если пользователь не авторизован, отправляем на страницу входа
        return redirect('login')

    if 'deactivate-account' in request.POST:
        Clients.objects.filter(id=request.POST['deactivate-account']).delete()
        return redirect("clients")

    data = {}
    data['search_text'] = ''
    if 'search' in request.POST:
        data['search_text'] = request.POST['search_text'].strip()
        data['clients'] = Clients.objects.filter(
        Q(phone__contains=data['search_text']) |
        Q(name__contains=data['search_text']) |
        Q(mail__contains=data['search_text'])
    )

    else:
        data['clients'] = Clients.objects.all()

    return render(request, 'clients/index.html', data)


def view_client_info(request, client_id):
    if 'user_id' not in request.session:  # если пользователь не авторизован, отправляем на страницу входа
        return redirect('login')

    if 'undo-pay' in request.POST:
        rec = Records.objects.filter(id=request.POST['undo-pay']).values()
        new_rec = 1
        if rec[0]['is_payed']:
            new_rec = 0
        Records.objects.filter(id=request.POST['undo-pay']).update(is_payed=new_rec)
        return redirect("view_client_info", client_id)

    if 'undo-cancel' in request.POST:
        rec = Records.objects.filter(id=request.POST['undo-cancel']).values()
        new_rec = 1
        if rec[0]['is_cancelled']:
            new_rec = 0
        Records.objects.filter(id=request.POST['undo-cancel']).update(is_cancelled=new_rec)
        return redirect("view_client_info", client_id)


    data = {}
    data['client'] = Clients.objects.filter(id=client_id).values()
    data['records'] = Records.objects.filter(client_id=client_id).order_by('-datetime').values()
    return render(request, 'clients/view.html', data)


def edit_client_info(request, client_id):
    if 'user_id' not in request.session:  # если пользователь не авторизован, отправляем на страницу входа
        return redirect('login')

    data = {}

    if 'save_client_info' in request.POST:  # проверяем была ли нажата кнопочка с name = save_account_info в post запросе
        info = request.POST
        Clients.objects.filter(id=client_id).update(name=info['name'],
                                                    sex=info['sex'],
                                                    phone=info['phone'],
                                                    polis=info['polis'],
                                                    mail=info['mail'],
                                                    age=info['age'],
                                                    passport_number=info['passport_number'])
        return redirect('view_client_info', client_id)

    data['client'] = Clients.objects.filter(id=client_id).values()
    data['records'] = Records.objects.filter(client_id=client_id).order_by('-datetime').values()
    data['client_form'] = ClientForm(
        data=data['client'][0])  # указываем в data значение из базы, чтобы автоматом выставлялись в поля
    return render(request, 'clients/edit.html', data)


def add_client(request):
    if request.method == 'POST':
        info = request.POST
        new_client = Clients(name=info['name'],
                            sex=info['sex'],
                            phone=info['phone'],
                            polis=info['polis'],
                            mail=info['mail'],
                            age=info['age'],
                            passport_number=info['passport_number'])
        new_client.save()
        return redirect('view_client_info', new_client.id)

    data = {}
    data['client_form'] = ClientForm()  # указываем в data значение из базы, чтобы автоматом выставлялись в поля
    return render(request, 'clients/add.html', data)
