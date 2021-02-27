from django.db import models

from django.contrib.auth import get_user_model

from .images import get_candidate_image_filepath, get_default_candidate_image

# Create your models here.


class Candidate(models.Model):
    
    PRIMARY = 1
    HIGH = 2

    level_choices = (
        (PRIMARY, 'Primaria'),
        (HIGH, 'Bachillerato'),
    )

    level = models.PositiveSmallIntegerField(
        choices=level_choices,
        default=PRIMARY,
    )
    
    candidates_name = models.CharField(max_length=170)

    proposal = models.TextField()



    image = models.ImageField(max_length=255, upload_to=get_candidate_image_filepath,
                                      default=get_default_candidate_image, blank=True, null=True)

    votes = models.ManyToManyField(
        get_user_model(), related_name="candidate_name"
    )

    @property
    def number_of_votes(self):
        return Candidate.objects.filter(id=self.pk).count()

    def __str__(self):
        return self.candidates_name
