#from celery import shared_task
from datetime import datetime, timedelta
from .models import Email

#@shared_task
def expire_verification_code(email_id):
    email_obj = Email.objects.get(email_id=email_id)
    if email_obj.expires_at < datetime.now():
        email_obj.auth_num = None
        email_obj.save()
