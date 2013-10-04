from django.shortcuts import render
from models import Account, Department, Desk, Company, TelephoneNumber, Email, Social_Network

def account(request, account_id):
    account_details = Account.objects.get(id = account_id)
    account_dep = Department.objects.get(id = account_id)
    account_desk = Desk.objects.get(id = account_id)
    account_company = Company.objects.get(id = account_id)
    account_telWFP = TelephoneNumber.objects.filter(account_id = account_id,company_id=1,telephoneDeviceType_id=1)[0]
    account_telMobile = TelephoneNumber.objects.filter(account_id=account_id,telephoneDeviceType_id=2)
    account_telLandline = TelephoneNumber.objects.filter(account_id = account_id,telephoneDeviceType_id=1)
    account_email = Email.objects.filter(account_id=account_id)
    account_social = Social_Network.objects.filter(account_id=account_id)
    context = {'account': account_details,
    'department': account_dep,
    'desk': account_desk,
    'company': account_company,
    'telWFP': account_telWFP,
    'mobiles': account_telMobile,
    'telephones': account_telLandline,
    'emails': account_email,
    'socials': account_social
    }
    return render(request, 'addressbook/account.html', context)

def index(request):
    account_list = Account.objects.all().order_by('-last_name')[:5]
    account_latest = Account.objects.filter(start_date__day=19)
    
    context = {'account_list': account_list, 
    		   'account_latest': account_latest,
    		  }
    return render(request, 'addressbook/index.html', context)