from django.shortcuts import render, redirect
from .models import *
from requests.forms import MessageForm
import telegram
from django.conf import settings
import asyncio
from requests.models import Contact


def get_common_context():
    about_text = AboutText.objects.all()
    general_page = GeneralPage.objects.all()
    portfolio_items = Portfolio.objects.all()
    comments = Comments.objects.all()

    context = {
        'general_page': general_page,
        'portfolio_items': portfolio_items,
        'comments': comments,
        'about_text': about_text,
    }

    return context


async def send_telegram_message(chat_id, message):
    bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text=message)


def process_form(request, template_name):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            chat_id = settings.TELEGRAM_GROUP_CHAT_ID
            message = message = f"Новые данные из формы:\n\nИмя: {data['name']}\nEmail: {data['email']}\nНомер телефона: {data['phone_number']}\nСообщение: {data['message']}"


            asyncio.run(send_telegram_message(chat_id, message))

            # Добавление данных в модель
            contact = Contact(
                name=data['name'],
                email=data['email'],
                phone_number=data['phone_number'],
                message=data['message']
            )
            contact.save()

            return redirect('https://instagram.com/workbench.kz?igshid=MzRlODBiNWFlZA==')
    else:
        form = MessageForm()

    context = {
        'form': form,
    }

    common_context = get_common_context()
    context.update(common_context)

    return render(request, template_name, context)


def index(request):
    return process_form(request, 'main/index.html')


def kazakh_mode(request):
    return process_form(request, 'main/kz.html')


def russian_mode(request):
    return process_form(request, 'main/ru.html')