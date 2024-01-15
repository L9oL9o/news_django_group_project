from django.db.models import Model, CharField, TextField, URLField, ImageField


class News(Model):
    title = CharField(max_length=100)
    content = TextField()


class Detail_news(Model):
    title = CharField(max_length=100)
    content = TextField()


class From_real_news(Model):
    title = CharField(max_length=100)
    content = TextField()
    url = URLField(default="default")
    img = URLField(default="")
