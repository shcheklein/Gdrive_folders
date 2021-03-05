from django.core.mail import EmailMessage


def send_parodi_mail(email, **kwargs):

    email = EmailMessage(

        to=[f"{email}"],
    )
    email.from_email = None
    email.template_id = '2589673'
    email.merge_global_data = {
        'client_name': f'{kwargs.get("client_name")}',
        'study_name': f'{kwargs.get("study_name")},',
        'id_remito': f'{kwargs.get("id_remito")}'

    }
    email.send()
    return email
