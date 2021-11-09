from django.db import models

# Create your models here.
#Modelo de curso


class CourseManager(models.Model):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )


class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    descricao = models.TextField('Descricao', blank=True)
    start_date = models.DateField('Data de Inicio', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem',
                              null=True, blank=True)
    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em ', auto_now=True)


class Meta:
    db_table = 'appcourses'


objects = CourseManager()




