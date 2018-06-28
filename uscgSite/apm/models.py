from django.db import models
from django.urls import reverse
import django.dispatch

# Create your models here.
class productLine(models.Model):
    """Model Representing a Product Line"""
    name = models.CharField(
        help_text = "Product Line Name (e.g. LREPL, IBCTPL)",
        max_length=30,
        )
    class Meta:
        ordering =['name']
        verbose_name = 'product Line'

    def __str__(self):
        """String Representation of Product Line Model"""
        return self.name

    def get_absolute_url(self):
        return reverse('product_line_view',args=[str(self.name)])

class shipClass(models.Model):
    name = models.CharField(
        help_text = "Ship Class Name (e.g WAGB, WTGB).",
        max_length = 10,
    )

    productLine = models.ForeignKey(
        'productLine',
        on_delete = models.SET_NULL,
        null=True,
        verbose_name = "product Line",
        )

    class Meta:
        ordering = ['name']
        verbose_name_plural = "ship Classes"

    def __str__(self):
        """String representaton of model class 'shipClass'."""
        return self.name

class shipInstance(models.Model):
    """Model representation of a Ship Instance"""
    name = models.CharField(
        help_text = 'Ship Name (e.g. POLAR STAR, MARIA BRAY)',
        max_length = 50,
    )
    hull = models.IntegerField(
        help_text = 'Hull Number (e.g. 102, 555)',
    )
    shipClass = models.ForeignKey(
        'shipClass',
        on_delete = models.SET_NULL,
        null = True,
        verbose_name = "Ship Class",
    )
    availability = models.DateField(
        help_text = 'Next Availability Date',
        null = True,
        blank = True,
    )

    length = models.IntegerField(
        help_text = "Ship Class Length (e.g. 100 foot ship).",
    )
    identifier = models.CharField(
        help_text = "Ship Class Identifier defaults to length - name (e.g. 175-WLM)",
        max_length = 30,
        blank = True,
        verbose_name='Description',
    )

    class Meta:
        ordering = ['hull']
        verbose_name = "ship Instance"

    def __str__(self):
        """String representation of shipInstance Model."""
        return "{0} {1} ({2} {3})".format("USCGC",
            self.name.upper(),
            self.shipClass.name.upper(),
            self.hull)

@django.dispatch.receiver(models.signals.post_init,sender = shipInstance)
def set_default_shipClass_identifier(sender,instance,*args,**kwargs):
    """
    Sets the default value for 'identifier' on the 'instance'.

    :param sender: The 'shipClass' class that sent the signalself.
    :param instance: The 'shipClass' instance that is being initialiazed

    :return: None
    """
    if not instance.identifier:
        instance.identifier = "{0}-{1}".format(instance.length,str(instance.shipClass))

class maintenanceRequirementList(models.Model):
    """Model representation of a Maintenance Item"""
    shipInstance = models.OneToOneField(
        'shipInstance',
        on_delete = models.SET_NULL,
        null = True,
        verbose_name = "Ship Instance",
    )

    class Meta:
        verbose_name = "maintenance Requirement List"

    def __str__(self):
        """String representation of Maintenance Requirement List"""
        return "MRL-" + str(self.shipInstance)

class maintenanceItem(models.Model):
    """Model representing a Maintenance Item"""
    title = models.CharField(
        help_text = 'Maintenance Item Title',
        max_length = 50,
    )
    description = models.CharField(
        help_text = 'Maintenance Item Description',
        max_length = 100,
        blank = True,
    )
    cfid = models.CharField(
        help_text = 'Functional Description (i.e. HULL, CR-SPRT)',
        max_length = 100,
        blank = True,
    )
    periodicity = models.IntegerField(
        help_text = 'Time Inteval for Maintenance Item Period',
        blank=True,

    )
    #Following is choices for Driver Model Field
    CMPC  = "CMP-Conditional"
    CMPR  = "CMP-Recurring"
    CONT  = "Conditional Task"
    ENG   = "Engineering Change"
    NON   = "NONE"
    REC   = "Recurring Work Items"

    DRIVER_CHOICES = (
        (CMPC, "CMP-Conditional"),
        (CMPR, "CMP-Recurring"),
        (CONT, "Conditional Task"),
        (ENG , "Engineering Change"),
        (NON , "NONE"),
        (REC , "Recurring Work Item"),
    )
    driver = models.CharField(
        max_length = 25,
        choices = DRIVER_CHOICES,
        default = NON,
    )
    fund_source = models.IntegerField(
        help_text = 'Funding Source',
        blank = True,
    )
    shipInstance = models.ManyToManyField('shipInstance',
        help_text = "Applicable Ship",
        verbose_name = "ship Instance"
    )
    maintenanceRequirementList = models.ManyToManyField(
        'maintenanceRequirementList',
        blank = True,
        help_text = "Applicable Maintenance Requirement List",
        verbose_name = "Maintenance Requirement List"
    )
    class Meta:
        ordering = ['title']
        verbose_name = "maintenance Item"

    def __str__(self):
        """String representation of Maintenance Item"""
        return str(self.title).upper()

class supplyPart(models.Model):
    """Model Representation of Maintenance Item parts"""
    NIIN = models.CharField(
        help_text = 'USCG NIIN Number',
        max_length = 30,
    )
    PN = models.CharField(
        help_text = 'Part Number',
        max_length = 30,
    )
    FSC = models.CharField(
        help_text = 'Part Location?',
        max_length = 10,
        )
    maintenanceItem = models.ManyToManyField(
        'maintenanceItem',
        help_text = "Applicable Maintenance Item",
        blank = True,
        verbose_name = "maintenance Item"
    )
    itemDescription = models.CharField(
        help_text = 'Item Description',
        max_length = 100,
        blank = True,
        verbose_name = "item Description"
    )

    class Meta:
        ordering = ['PN']
        verbose_name = "supply Part"

    def __str__(self):
        "String Representation of Part Model"
        return "Part Number:{0}, NIIN: {1}".format(str(self.PN),str(self.NIIN))
