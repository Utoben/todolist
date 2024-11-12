from django.core.mail import send_mail

# отправка письма заказчику
def long_send_order(admins_email, fullname, his_email, description):
    subject = f'Новый запрос на консультацию от {fullname}'
 
    message = f'Желающий {fullname}, вопрос: {description}, email: {his_email}'
    from_email = 'ubbelousov@yandex.ru'
    # redis_conn = Redis(host='127.0.0.1', port=6379)
    
    # q = Queue(connection=redis_conn)
    # job = q.enqueue(send_email, subject, message, from_email, [to_email])
    print(f'отправка начата long_send_order')
    send_mail(subject, message, from_email, [admins_email])
    print(f'отправка закончена long_send_order')
    
# отправка письма исполнителю
def long_send_confirmation(fullname, his_email):
    subject = f'Просто школа разработки. Запрос на консультацию'
    
    message = f'{fullname}, ваш запрос на консультацию получен. На него скоро ответит преподаватель'
    from_email = 'ubbelousov@yandex.ru'
    # redis_conn = Redis(host='127.0.0.1', port=6379)
    
    # q = Queue(connection=redis_conn)
    # job = q.enqueue(send_email, subject, message, from_email, [to_email])
    send_mail(subject, message, from_email, [his_email])
