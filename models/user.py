"""
Created by anthony on 19.10.17
user
"""
from sqlalchemy import BigInteger, Column, String, Boolean
from config.db_config import Base


class User(Base):
    __tablename__ = 'users'
    # user's id is his chat_id
    id              = Column(BigInteger, primary_key=True)
    username        = Column(String)
    first_name      = Column(String)
    # safe delete flag
    is_active       = Column(Boolean, default=True)
    #interface_lang  = Column(String)

    def __init__(self, username, chat_id, first_name):
        self.set_username(username)
        self.set_id(chat_id)
        self.set_first_name(first_name.capitalize())
        #self.set_interface_lang(interface_lang)

    def get_id(self):
        return self.id

    def set_id(self, id_value):
        self.id = id_value

    def get_username(self):
        return self.username

    def set_username(self, name):
        self.username = name

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, name):
        self.first_name = name

    # def get_interface_lang(self):
    #     return  self.interface_lang
    #
    # def set_interface_lang(self, lang):
    #     self.interface_lang=lang