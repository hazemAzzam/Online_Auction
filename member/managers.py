from django.contrib.auth.base_user import BaseUserManager

class MemberManager(BaseUserManager):
    def create_user(self, email, name, password=None, **kwargs):
        if not email or not name:
            raise ValueError("Please fill required fields")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **kwargs)
        user.set_password(password)

        user.save()
        return user
    
    def create_superuser(self, email, name, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        user = self.create_user(email, name, password, **kwargs)
        return user