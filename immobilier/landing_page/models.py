from django.db import models

class sale(models.Model):
    
    state_list = (
        ("Tunis", "Tunis"),
        ("Ariana", "Ariana"),
        ("Ben arous", "Ben arous"),
        ("Mannouba", "Mannouba"),
        ("Bizerte", "Bizerte"),
        ("Nabeul", "Nabeul"),
        ("Béja", "Béja"),
        ("Jandouba", "Jandouba"),
        ("Zaghouan", "Zaghouan"),
        ("Siliana", "Siliana"),
        ("Le Kef", "Le Kef"),
        ("Sousse", "Sousse"),
        ("Monastir", "Monastir"),
        ("Mahdia", "Mahdia"),
        ("Kasserine", "Kasserine"),
        ("Sidi bouzid", "Sidi bouzid"),
        ("Kairouan", "Kairouan"),
        ("Gafsa", "Gafsa"),
        ("sfax", "sfax"),
        ("Gabes", "Gabes"),
        ("Médenine", "Médenine"),
        ("Tozeur", "Tozeur"),
        ("Kebili", "Kebili"),
        ("Tataouine", "Tataouine"),
    )    
    
    type_list = (
        ("r", "Residential"), # Any property used for residential purposes
        ("c", "Commercial"), # Any property used exclusively for business purposes 
        ("i", "Industrial"), # Any property used for manufacturing, production, distribution, storage, and research and development
        ("l", "Land"), # Includes undeveloped property, vacant land, and agricultural land (farms, orchards, ranches, and timberland).
        ("sp", "Special purpose") # Property used by the public 
    )
    
    #details fields
    state = models.CharField(max_length=20, choices = state_list)
    
    location = models.CharField(max_length=300, blank=True, null=True)
    
    type = models.CharField(max_length=20, choices = type_list, default = "")
    
    surface_area = models.IntegerField(default=0) # in m**2 or hektar (10000m)
     
    description = models.CharField(max_length=1000)
    
    rooms = models.IntegerField(max=9, default=0)
   
    #Contact fields
    number = models.CharField(max_length=8, blank=True, null=True)
    
    def __str__(self):
        return f" is selling a {self.state} property"