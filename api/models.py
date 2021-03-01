from django.db import models

CATEGORIES_CHOICES = (
    ("Marketing Digital", "Marketing Digital"),
    ("Manualidades", "Manualidades"),
    ("Ilustración y Dibujo", "Ilustración y Dibujo"),
    ("Lifestyle", "Lifestyle"),
    ("Marketing Digital", "Marketing Digital"),
    ("Video", "Video"),
    ("Negocios", "Negocios"),
    ("Fotografia", "Fotografia"),
    ("Diseño", "Diseño"),
    ("Escritura", "Escritura"),
    ("Animación & 3D", "Animación & 3D"),
)

SUBCATEGORIES_CHOICES = (
    ("Marketing Digital", "Marketing Digital"),
    ("Bordado y costura","Bordado y costura" ),
    ("Ilustración Digital", "Ilustración Digital"),
    ("Lifestyle", "Lifestyle"),
    ("Producción", "Producción"),
    ("Locución", "Locución"),
    ("Innovación", "Innovación"),
    ("Liderazgo", "Liderazgo"),
    ("Fundamentos de fotografía", "Fundamentos de fotografía"),
    ("Publicidad", "Publicidad"),
    ("Postproducción", "Postproducción"),
    ("Dibujo", "Dibujo"),
    ("Branding", "Branding"),
    ("Retoque Fotográfico", "Retoque Fotográfico"),
    ("Escritura", "Escritura"),
    ("Ventas", "Ventas"),
    ("Data", "Data"),
    ("Animación 2D", "Animación 2D"),
)

LEVEL_CHOICES = (
    ("Introductorio", "Introductorio"),
    ("Intermedio", "Intermedio"),
    ("Completo", "Completo"),
    ("Avanzado", "Avanzado"),
)

class Course(models.Model):
    name = models.CharField(max_length = 150)
    category = models.CharField(max_length = 150, choices=CATEGORIES_CHOICES)
    subcategory = models.CharField(max_length = 150, choices=SUBCATEGORIES_CHOICES)
    level = models.CharField(max_length = 50, choices=LEVEL_CHOICES)
    username = models.CharField(max_length = 50)
    real_price = models.FloatField(default= 0)
    price = models.FloatField(default= 0)
    discount = models.FloatField(default= 0)
    score = models.FloatField(default= 0)
    users = models.IntegerField(default= 0)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
