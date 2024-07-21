from models.users import UserModel
from schemas.user import User



class UserService():

    def __init__(self, db) -> None:
        self.db = db

    def get_user_by_email(self, email: str):
        user:User = self.db.query(UserModel).filter(
            UserModel.email == email).first()
        return user

    def create_user(self, user: User):
        new_user = UserModel(**user.model_dump())
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
