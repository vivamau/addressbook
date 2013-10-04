from django.db import models
from uuidfield import UUIDField
#from webcam.fields import CameraField
#import webcam.admin


class Privacy(models.Model):
    class Meta:
        verbose_name_plural = 'Privacy Status'
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Country(models.Model):	
    class Meta:
        verbose_name_plural = 'Countries'
    ISO3 = models.CharField(max_length=3)
    UNCODE = models.CharField(max_length=3)
    ISO2 = models.CharField(max_length=2)
    UN_name = models.CharField(max_length=300)
    common_name = models.CharField(max_length=300)
    local_name = models.CharField(max_length=300)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    tel_prefix = models.CharField(max_length=4)

    def __unicode__(self):
        return self.common_name


class City(models.Model):
    class Meta:
        verbose_name_plural = 'Cities'
        verbose_name = 'City'
    name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    local_name = models.CharField(max_length=200)
    tel_prefix = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name


class Company(models.Model):
    class Meta:
        verbose_name_plural = 'Companies'
        verbose_name = 'Company'
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    city = models.ForeignKey(City)
    tel_prefix = models.CharField(max_length=10, blank=True)
    website = models.URLField(max_length=150, blank=True)
    faxNumber = models.CharField("Fax", max_length=150, blank=True)
    telNumber = models.CharField("Telephone", max_length=150, blank=True)
    email = models.EmailField("Email Address", blank=True)
    contactName = models.CharField("Main Contact", max_length=150, blank=True)

    def __unicode__(self):
        return self.name


class Department(models.Model):
    class Meta:
        verbose_name_plural = 'Departments'
        verbose_name = 'Department'
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=200)
    acronym = models.CharField(max_length=10,)
    company = models.ForeignKey(Company)

    def __unicode__(self):
        return self.name


class Building(models.Model):
    class Meta:
        verbose_name_plural = 'Buildings'
        verbose_name = 'Building'
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    acronym = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    capacity = models.IntegerField(default=0)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return self.acronym


class Desk(models.Model):
    class Meta:
        verbose_name_plural = 'Desks'
        verbose_name = 'Desk'
    acronym = models.CharField(max_length=10)
    floor = models.IntegerField(default=0)
    tower = models.CharField(max_length=100, blank=True)
    building = models.ForeignKey(Building)

    def __unicode__(self):
        return self.acronym


class ContractType(models.Model):
    class Meta:
        verbose_name_plural = 'Contract Types'
        verbose_name = 'Contract Type'
    acronym = models.CharField(max_length=10)
    description = models.TextField()
    short_description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.acronym


class MailingList(models.Model):
    class Meta:
        verbose_name_plural = 'Mailing Lists'
        verbose_name = 'Mailing List'
    name = models.CharField(max_length=200)
    description = models.TextField()
    manageURI = models.URLField("Link to manage", max_length=200, blank=True)

    def __unicode__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField('Team foundation date')
    end_date = models.DateTimeField('Team end date')

    def __unicode__(self):
        return self.name


class Account(models.Model):
    class Meta:
        verbose_name_plural = 'Accounts'
        verbose_name = 'Account'
    uuid = UUIDField(auto=True)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    index_number = models.CharField(max_length=100)
    job_description = models.TextField()
    start_date = models.DateTimeField('Contract start date')
    end_date = models.DateTimeField('Contract end date')
    contractType = models.ForeignKey(ContractType, verbose_name='Contract Type')
    department = models.ForeignKey(Department)
    desk = models.ForeignKey(Desk)
    picture = models.ImageField(upload_to="addressbook/img/")
    #pictureWebCam = CameraField()
    team = models.ManyToManyField(Team)
    mailinglist = models.ManyToManyField(MailingList, verbose_name="Mailing List")

    def __unicode__(self):
        return self.last_name + ", " + self.first_name


class MotorVehicleType(models.Model):
    class Meta:
        verbose_name_plural = 'Motor Vehicle Types'
        verbose_name = 'Motor Vehicle Type'
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class MotorVehicle(models.Model):
    class Meta:
        verbose_name_plural = 'Motor Vehicles'
        verbose_name = 'Motor Vehicle'
    plate = models.CharField(max_length = 20)
    country = models.ForeignKey(Country)
    year = models.IntegerField()
    motorVehicleType = models.ForeignKey(MotorVehicleType, verbose_name='Type')
    account = models.ForeignKey(Account)
    privacy = models.ForeignKey(Privacy)

    def __unicode__(self):
        return self.plate


class SocialNetworkType(models.Model):
    class Meta:
        verbose_name_plural = 'Social Network Types'
        verbose_name = 'Social Network Type'
    name = models.CharField("Platform", max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class SocialNetwork(models.Model):
    class Meta:
        verbose_name_plural = 'Social Networks'
        verbose_name = 'Social Network'
    username = models.CharField(max_length=100)
    socialNetworkType = models.ForeignKey(SocialNetworkType, verbose_name="Platform")
    account = models.ForeignKey(Account, related_name='socials')
    privacy = models.ForeignKey(Privacy)

    def __unicode__(self):
        return self.username


class WebsiteType(models.Model):
    class Meta:
        verbose_name_plural = 'Website Types'
        verbose_name = 'Website Type'
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Website(models.Model):
    uri = models.URLField(max_length=1000)
    name = models.CharField(max_length=200)
    description = models.TextField()
    websiteType = models.ForeignKey(WebsiteType, verbose_name="Type")
    account = models.ForeignKey(Account, related_name='websites')
    privacy = models.ForeignKey(Privacy)

    def __unicode__(self):
        return self.uri


class EmailType(models.Model):
    class Meta:
        verbose_name_plural = 'Email Types'
        verbose_name = 'Email Type'
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Email(models.Model):
    email = models.EmailField(max_length=200)
    emailType = models.ForeignKey(EmailType, verbose_name='Email Type')
    account = models.ForeignKey(Account, related_name='emails')
    privacy = models.ForeignKey(Privacy)

    def __unicode__(self):
        return self.email


class TelephoneNumberType(models.Model):
    class Meta:
        verbose_name_plural = 'Tel. Number Types'
        verbose_name = 'Tel. Number Type'
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class TelephoneDeviceType(models.Model):
    class Meta:
        verbose_name_plural = 'Tel. Device Types'
        verbose_name = 'Tel. Device Type'
    name = models.CharField("Device Type", max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class TelephoneNumber(models.Model):
    class Meta:
        verbose_name_plural = 'Tel. Numbers'
        verbose_name = 'Tel. Number'
    country = models.ForeignKey(Country)
    city = models.ForeignKey(City)
    extension = models.CharField(max_length=100,blank=True)
    numberComplete = models.CharField("Number Complete", max_length=100)
    telephoneNumberType = models.ForeignKey(TelephoneNumberType, verbose_name="Number Type")
    telephoneDeviceType = models.ForeignKey(TelephoneDeviceType, verbose_name="Device Type")
    account = models.ForeignKey(Account, related_name="telephones")  # equivalent to _set to reverse data extraction
    company = models.ForeignKey(Company)
    privacy = models.ForeignKey(Privacy)

    def __unicode__(self):
        return self.numberComplete


class AddressType(models.Model):
    class Meta:
        verbose_name_plural = 'Address Types'
        verbose_name = 'Address Type'
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Address(models.Model):
    class Meta:
        verbose_name_plural = 'Addresses'
        verbose_name = 'Address'
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    cap = models.CharField(max_length=10)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    city = models.ForeignKey(City)
    country = models.ForeignKey(Country)
    privacy = models.ForeignKey(Privacy)
    addressType = models.ForeignKey(AddressType, verbose_name="Address Type")
    account = models.ForeignKey(Account, related_name="addresses")

    def __unicode__(self):
        return self.street