from django.db import models

class Client(models.Model):
    """fishgirl's clients"""
    client_name=models.CharField("Nome", max_length=200, unique=True)
    client_address=models.CharField("Endereço", max_length=200)
    client_contact=models.CharField("Contacto", max_length=200)
    client_email=models.EmailField("Email", max_length=200, null=True)
    client_note=models.CharField("Observações", max_length=200)
    client_date_added=models.DateTimeField("Data Adicionado", auto_now_add=True)
    def __str__(self):
        return self.client_name

class Family(models.Model):
    family_name=models.CharField("Família", max_length=200, unique=True)
    class Meta:
        verbose_name_plural='Families'
    def __str__(self):
        return self.family_name

class Product(models.Model):
    """fishgirl's products"""
    product_name=models.CharField("Nome", max_length=200, unique=True)
    product_family=models.ForeignKey(Family, on_delete=models.PROTECT, verbose_name="Família")
    product_note=models.CharField("Observações", max_length=200)
    product_date_added=models.DateTimeField("Data Adicionado", auto_now_add=True)
    def __str__(self):
        return self.product_name

class Sale(models.Model):
    """fishgirl's sales"""
    id=models.AutoField(primary_key=True)
    sale_date=models.DateTimeField("Data da Venda", auto_now_add=True)
    client=models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name="Clientes")
    sale_note=models.CharField("Observações", max_length=200, null=True)
    def __str__(self):
        return "Venda a "+str(self.client)+" - "+str(self.sale_date)[:10]

class Movement(models.Model):
    id=models.AutoField(primary_key=True)
    sale=models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name="Venda")
    movement_product=models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Produto")
    movement_quantity=models.DecimalField("Quantidade", max_digits=7,decimal_places=3)
    movement_purchase_price=models.DecimalField("Preço de Custo", max_digits=7,decimal_places=3, null=True, help_text="Introduza '0' para ignorar.")
    movement_selling_price=models.DecimalField("Preço de Venda", max_digits=7,decimal_places=3)
    def __str__(self):
        return f"{self.movement_quantity}kg de {self.movement_product}"