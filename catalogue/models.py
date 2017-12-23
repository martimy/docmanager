from django.db import models
from django.urls import reverse
#from django.forms import ModelForm


class Series(models.Model):
    series_title = models.CharField("series title", max_length=100, null=True)

class Book(models.Model):
    DOC_TYPE = (
        ('B', 'Book'),
        ('C', 'Book Chapter'),
        ('W', 'White Paper'),
        ('P', 'Research Paper'),
        ('R', 'Report'),
        ('S', 'Presentation'),
        ('M', 'Manual'),
        ('U', 'Undefined'),
    )

    DOC_RATING = (
        (0, 'Unrated'),
        (1, 'Poor'),
        (2, 'Ok'),
        (3, 'Good'),
    )

    filepath = models.CharField(max_length=200)
    filename = models.CharField(max_length=200)
    title = models.CharField("document title", max_length=200)
    type = models.CharField("document type", max_length=1, choices=DOC_TYPE, default="U")
    description = models.TextField()
    category = models.CharField(max_length=50, null=True, blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField("document rating", choices=DOC_RATING, default=0)
    seen = models.DateTimeField()

    series = models.ForeignKey(Series, null=True, on_delete=models.CASCADE)
    relatives = models.ManyToManyField("self", through="Association",  symmetrical=False)

class Association(models.Model):
    note = models.CharField("association note", max_length=100)
    association = models.ForeignKey(Book, on_delete=models.CASCADE)
    #right = models.ForeignKey(Book, related_name="right_side", on_delete=models.CASCADE)


#    def get_absolute_url(self):
#        return reverse('book_detail', kwargs={'id': self.id})

#class BookForm(ModelForm):
#    class Meta:
#        model = Book
#        fields = ['title', 'type', 'category', 'tags', 'rating', 'description']
#        fields = '__all__'
