from django.db import models

from django.contrib.auth import get_user_model


# Create your models here.

def get_image_extension(filename):
    if "." in filename:
        return filename.split(".")[-1]
    else:
        return None

def get_candidate_image_filepath(self, filename):
    """
    Returns the candidate image filepath
    """
    extension = get_image_extension(filename)

    if extension is not None:
        return f"images/candidates/{self.id}/image.{extension}"
    else:
        return f"images/candidates/{self.id}/image.png"

def get_default_candidate_image():
    """
    Returns the default profile image
    """

    return "images/default/default_gilflc.png"


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
        get_user_model(), related_name="candidate_name", blank=True
    )


    @property
    def number_of_votes(self):
        """
        Returns the votes of a candidate
        """
        return self.votes.count()

    def __str__(self):
        return self.candidates_name
