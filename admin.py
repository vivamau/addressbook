from django.contrib import admin

from addressbook.models import Privacy
admin.site.register(Privacy)

from addressbook.models import Country
admin.site.register(Country)

from addressbook.models import City
admin.site.register(City)

from addressbook.models import Company
admin.site.register(Company)

from addressbook.models import Department
admin.site.register(Department)

from addressbook.models import Building
admin.site.register(Building)

from addressbook.models import Desk
admin.site.register(Desk)

from addressbook.models import ContractType
admin.site.register(ContractType)

from addressbook.models import MailingList
admin.site.register(MailingList)

from addressbook.models import Team
admin.site.register(Team)

from addressbook.models import Account
admin.site.register(Account)

from addressbook.models import MotorVehicleType
admin.site.register(MotorVehicleType)

from addressbook.models import MotorVehicle
admin.site.register(MotorVehicle)

from addressbook.models import SocialNetworkType
admin.site.register(SocialNetworkType)

from addressbook.models import SocialNetwork
admin.site.register(SocialNetwork)

from addressbook.models import Website
admin.site.register(Website)

from addressbook.models import WebsiteType
admin.site.register(WebsiteType)

from addressbook.models import TelephoneNumber
admin.site.register(TelephoneNumber)

from addressbook.models import TelephoneDeviceType
admin.site.register(TelephoneDeviceType)

from addressbook.models import TelephoneNumberType
admin.site.register(TelephoneNumberType)

from addressbook.models import Email
admin.site.register(Email)

from addressbook.models import EmailType
admin.site.register(EmailType)

from addressbook.models import Address
admin.site.register(Address)

from addressbook.models import AddressType
admin.site.register(AddressType)