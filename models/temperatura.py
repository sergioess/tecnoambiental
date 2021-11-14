from app import database
from sqlalchemy import asc, desc
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import date

from models.ciudad import Ciudad

class Temperatura(database.Model):

    __tablename__ = 'registro_temperatura'

    id = database.Column(database.Integer, primary_key=True)
    fecha_registro = database.Column(database.Date, nullable=False)
    id_ciudad = database.Column(database.Integer, ForeignKey("ciudad.id"))
    temperatura_aire = database.Column(database.Float, nullable=False)
    id_usuario = database.Column(database.Integer, nullable=False)

#este es el toString personalizado
    def __str__(self):
        return f"<Temperatura {self.id} {self.fecha_registro} {self.id_ciudad} {self.temperatura_aire} {self.id_usuario} >"

    def __init__(self, id_ciudad, temperatura_aire, id_usuario):
        self.fecha_registro = fecha_registro
        self.id_ciudad = id_ciudad
        self.temperatura_aire = temperatura_aire
        self.id_usuario = id_usuario
        


    @staticmethod
    def get_all():
        return Temperatura.query.all()


    def get_by_id(id):
        return Temperatura.query.filter_by(id=id).first()


    def save(self):

        print (self)
        database.session.add(self)
        database.session.commit()

    def delete(id):
        print(id)
        temperaturaElimina = Temperatura.query.filter_by(id=id).first()
        # print(temperaturaElimina)

        database.session.delete(temperaturaElimina)
        database.session.commit()