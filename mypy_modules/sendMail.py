
# 通常のメール送信
from django.core.mail import send_mail

# add bcc
from django.core.mail import EmailMessage

# default_from_email
from django.conf import settings

# login_user
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# from request import user

# use template
from django.template.loader import render_to_string

####################
# {{ user.username }}様

# 苗字: {{ user.first_name }}
# 名前: {{ user.last_name }}
# メールアドレス: {{ user.email }}

# {% if user.is_superuser %}
# あなたは管理者です。
# {% endif %}
####################
# デフォルト送信先
from_email = settings.DEFAULT_FROM_EMAIL  # 送信者

####################
# class FruitList(ListView):
#     model = Fruit
#     paginate_by = "2"
#     queryset = Fruit.objects.filter(user=request.user)
#     context_object_name = "myfruitlist"
#     template_name = 'myfruit_list.html'

#     def get_queryset(self):
#         return Fruit.objects.filter(user=self.request.user)
####################


subject = "題名"
# message = "本文\\nです"

context: dict = {
    # テンプレート
}

# template file
def get(self, request, *args, **kwargs):
    login_user = self.request.user

    # ログインユーザから送信
    if request.user.is_authenticated():
        login_user_id = self.request.user.id
        
        user1 = authenticate(username='john', password='secret')
        user1.email_user(subject, message, from_email)
        
        recipient_list: list = ["strawberry.pasta1818@gmail.com"]  # 宛先リスト
        bcc: list = ["example@gmail.com"]  # BCCリスト

        message = render_to_string("app/mails/mail.txt", context, request)

# 通常メール送信
# send_mail(subject, message, from_email, recipient_list)
# bccあり
email = EmailMessage(subject, message, from_email, recipient_list, bcc)
print(email)
# email.send()

####################
# class NantokaView(LoginRequiredMixin, TemplateView):

#     login_url = '/accounts/login/'
#     template_name = 'nantoka.html'

#     def get(self, request, *args, **kwargs):
#         print(request.user)

#     def post(self, request, *args, **kwargs):
#         login_user = self.request.user
