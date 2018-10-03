from django.db import models

class SoldData(models.Model):
  id = models.IntegerField(primary_key=True)
  address = models.CharField(max_length = 200)
  zipCode = models.CharField(max_length = 200)
  sellPrice = models.IntegerField()
  date = models.TextField(max_length = 200)
    
  def __str__(self):
    return self

  class Meta:
    verbose_name_plural = "sold"
    db_table = 'sold_solddata'
    managed = False