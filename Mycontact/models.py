from django.db import models

#class Contact(models.Model):
    #dans postregresql, on peut utiliser le type de données "serial" pour créer un champ auto-incrémenté. Cependant, dans Django, le champ "AutoField" est utilisé pour créer un champ auto-incrémenté qui est compatible avec plusieurs bases de données, y compris PostgreSQL. Donc, vous pouvez utiliser "AutoField" pour créer un champ auto-incrémenté dans votre modèle Contact.
    #id = models.AutoField(primary_key=True)
    #firstname = models.CharField(max_length=200)
    #lastname = models.CharField(max_length=200)
    #email = models.EmailField(max_length=254)
    #message = models.TextField()

    #def __str__(self):
    #    return f"{self.firstname} {self.lastname}"


from mongoengine import Document, StringField, EmailField
class Contact(Document):
 firstname = StringField(max_length=100, required=True)
 lastname = StringField(max_length=100, required=True)
 email = EmailField(required=True)
 message = StringField(required=True)
 def __str__(self):
  return f"{self.firstname} {self.lastname}" 