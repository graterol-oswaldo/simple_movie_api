from models.users import UserModel
from schemas.user import User, UserBase
from utils.pwd_hash_manager import get_password_hash,verify_password


class UserService():

    def __init__(self, db) -> None:
        self.db = db

    def authenticate_user(self, login_data:UserBase):
        user:User = self.get_user_by_email(login_data.email)
        if not user:
            return False
        if not verify_password(login_data.password, user.password):
            return False
        return user

    def get_user_by_email(self, email: str):
        user:User = self.db.query(UserModel).filter(
            UserModel.email == email).first()
        return user

    def create_user(self, user: User):
        new_user = UserModel(**user.model_dump())
        new_user.password = get_password_hash(new_user.password)
        self.db.add(new_user)
        self.db.commit()
        return

    def update_user(self, email: str, data: User):
        user = self.db.query(UserModel).filter(
            UserModel.email == email).first()
        user.name = data.name
        user.email = data.email
        user.password = data.password
        user.is_active = data.is_active
        self.db.commit()
        return
