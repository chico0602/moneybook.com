from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect, render, resolve_url
from django.template.loader import render_to_string
from django.views import generic
from .forms import (LoginForm, UserCreateForm, UserUpdateForm)

# Create your views here.
User = get_user_model()


def top(request):
    return render(request, 'registration/top.html')


# ログイン
class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


# ログアウト
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'registration/top.html'


# アカウント作成
# ユーザー仮登録
class UserCreate(generic.CreateView):

    template_name = 'registration/create.html'
    form_class = UserCreateForm

    # 仮登録と本登録用メールの発行
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # アクティベーションURLの送付
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject = render_to_string('registration/mail_template/create/subject.txt', context)
        message = render_to_string('registration/mail_template/create/message.txt', context)

        user.email_user(subject, message)
        return redirect('accounts:create_done')


# ユーザー仮登録完了
class UserCreateDone(generic.TemplateView):
    template_name = 'registration/create_done.html'


# メール内URLアクセス後のユーザー本登録
class UserCreateComplete(generic.TemplateView):

    template_name = 'registration/create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60 * 60 * 24)

    # tokenが正しければ本登録
    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()

        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    # 問題なければ本登録とする
                    user.is_active = True
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()


# そのユーザーだけ扱う
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


# ユーザー詳細
class UserDetail(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'registration/user_detail.html'


# ユーザー更新
class UserUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'registration/user_form.html'

    def get_success_url(self):
        return resolve_url('accounts:user_detail', pk=self.kwargs['pk'])
