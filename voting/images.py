"""
Images operations
"""

def get_image_extension(filename):
    if "." in filename:
        return filename.split(".")[-1]
    else:
        return None

def get_candidate_image_filepath(self, filename):
    """
    Returns the profto store
    """
    extension = get_image_extension(filename)
    
    if extension is not None:
        return f"images/candidates/{self.pk}/image.{extension}"
    else:
        return f"images/candidates/{self.pk}/image.png"



def get_default_candidate_image():
    """
    Returns the default profile image
    """

    return "images/default/default_gilflc.png"
