from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User, Coruser

#로그인 시 DB에 존재하는 계정인지 확인 하는 코드
class CustomAuthenticationBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        print(f"Authenticate called with email: {email}, password: {password}")
        try:
            # 일반 회원 테이블에서 이메일 확인
            user = User.objects.get(email=email, password=password)
            print(f"{email},{password}",user)
            return user
        except User.DoesNotExist:
            try:
                # 법인 회원 테이블에서 이메일 확인
                user = Coruser.objects.get(email=email, password=password)
                print(user)
                return user
            except Coruser.DoesNotExist:
                # 사용자가 없으면 None 반환
                return None


    def get_user(self, user_id):
        try:
            # 일반 회원 테이블에서 사용자 ID 확인
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            try:
                # 법인 회원 테이블에서 사용자 ID 확인
                return Coruser.objects.get(pk=user_id)
            except Coruser.DoesNotExist:
                return None
