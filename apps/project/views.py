from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Project, Schudele,Network,Account,Data
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.


def registrarProyecto(request):
   name= request.POST["nameNP"]
   description= request.POST["descriptionNP"]
   endDate= request.POST["endDateNP"]
   proyecto = Project.objects.create(
      name=name, description=description , endDate=endDate, state=True, User= request.user)
   return redirect('/project')

def registrarCronograma(request):
   id= request.POST["idss"]
   description= request.POST["desNP"]
   startHour = request.POST["hiNP"]
   endHour = request.POST["hfNP"]
   frecuency= request.POST["frNP"]
   periodicity = request.POST["perNP"]
   project =request.POST["prNP"]
   project = Project.objects.get(id=project)
   network = request.POST["nwnt"]
   network = Network.objects.get(id=network)
   schudele = Schudele.objects.create(
       description=description , startHour=startHour, endHour=endHour, frecuencyHour= frecuency ,Periodicity=periodicity, Project=project,Network=network)
   return redirect("/project/Schudele/"+str(id))


def registrarAcc(request):
   urlname = request.POST["urlnameNP"]
   description =request.POST["dsNP"]
   type = request.POST["tpNP"]
   id= request.POST["idss"]
   schudele= Schudele.objects.get(id=id)
   account = Account.objects.create(
       urlname=urlname , description=description, type=type, state= True ,Schudele=schudele)
   return redirect("/project/Schudele/Account/"+str(id))

def registrarNet(request):
   name = request.POST["nameNP"]
   description = request.POST["dsNP"]
   user = request.POST["usNP"]
   password = request.POST["pssNP"]
   token = request.POST["tkNP"]
   method = request.POST["mtNP"]
   net = Network.objects.create(
      name=name , description=description, user=user, state= True ,password=password,token=token,  method= method)
   return redirect("/project/Network")

def registrarData(request):
   date = request.POST["dateNP"]
   text =request.POST["txtNP"]
   id= request.POST["idss"]
   account= Account.objects.get(id=id)
   data = Data.objects.create(
      date=date , text=text, Account=account)
   return redirect("/project/Schudele/Account/Data/"+str(id))

def eliminacionProyectos(request,id):
   project= Project.objects.get(id=id)
   project.delete()
   return redirect("/project")

def editarProyecto(request):
   name= request.POST["nameNP"]
   description= request.POST["descriptionNP"]
   endDate= request.POST["endDateNP"]
   id= request.POST["idNP"]
   state = request.POST["stateNP"]
   project= Project.objects.get(id=id)
   project.name=name
   project.description=description
   project.endDate=endDate
   project.state = state
   project.save()
   return redirect("/project")

def editarCronograma(request):
   id= request.POST["idNP"]
   description= request.POST["desNP"]
   startHour = request.POST["hiNP"]
   endHour = request.POST["hfNP"]
   frecuency= request.POST["frNP"]
   periodicity = request.POST["perNP"]
   schudele = Schudele.objects.get(id=id)
   schudele.description= description
   schudele.startHour=startHour
   schudele.endHour=endHour
   schudele.frecuencyHour=frecuency
   schudele.Periodicity=periodicity
   schudele.save()
   rid= schudele.Project.id
   return redirect("/project/Schudele/"+str(rid))

def editarAcc(request):
   id= request.POST["idNP"]
   urlname = request.POST["urlnameNP"]
   description = request.POST["desNP"]
   type = request.POST["tpNP"]
   state = request.POST["stNP"]
   account = Account.objects.get(id=id)
   account.urlname= urlname
   account.description=description
   account.type=type
   account.state=state
   account.save()
   rid= account.Schudele.id
   return redirect("/project/Schudele/Account/"+str(rid))

def editarNet(request):
   id= request.POST["idNP"]
   name = request.POST["nameNP"]
   description = request.POST["desNP"]
   user = request.POST["usNP"]
   password = request.POST["pssNP"]
   user = request.POST["usNP"]
   token = request.POST["tkNP"]
   state = request.POST["stNP"]
   method = request.POST["mtNP"]
   net = Network.objects.get(id=id)
   net.name= name
   net.description=description
   net.user=user
   net.password=password
   net.token=token
   net.state=state
   net.method=method
   net.save()
   return redirect("/project/Network")

def editarData(request):
   id= request.POST["idNP"]
   date = request.POST["dateNP"]
   text = request.POST["txtNP"]
   data = Data.objects.get(id=id)
   data.date= date
   data.text=text
   data.save()
   rid= data.Account.id
   return redirect("/project/Schudele/Account/Data/"+str(rid))

def eliminacionSchudele(request,id):
   schudele= Schudele.objects.get(id=id)
   rid=str(schudele.Project.id)
   schudele.delete()
   return redirect("/project/Schudele/"+rid)

def eliminacionData(request,id):
   data= Data.objects.get(id=id)
   rid=str(data.Account.id)
   data.delete()
   return redirect("/project/Schudele/Account/Data/"+rid)

def eliminacionAcc(request,id):
   account= Account.objects.get(id=id)
   rid=str(account.Schudele.id)
   account.delete()
   return redirect("/project/Schudele/Account/"+rid)

def eliminacionNet(request,id):
   network= Network.objects.get(id=id)
   network.delete()
   return redirect("/project/Network/")

class IndexView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/index.html'

   def get_context_data(self, *args, **kwargs):
      context = super(IndexView,self).get_context_data(*args, **kwargs)
      proyectos = list(Project.objects.filter(User_id=self.request.user).values())
      context['proyectos'] = proyectos
      context['api'] = {
            'title': 'Projects',
        }
      return context 
   
class EdView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/edicionProyectos.html'

   def get_context_data(self,id, *args, **kwargs):
      context = super(EdView,self).get_context_data(*args, **kwargs)
      proyecto = Project.objects.get(id=id)
      context['proyecto'] = proyecto
      context['api'] = {
            'title': 'Projects',
        }
      return context
   
class EdCView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/ediciondehorarios.html'

   def get_context_data(self,id, *args, **kwargs):
      context = super(EdCView,self).get_context_data(*args, **kwargs)
      schudele = Schudele.objects.get(id=id)
      context['schudele'] = schudele
      context['api'] = {
            'title': 'Projects',
        }
      return context

class EschuView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/Schudele.html'
   def get_context_data(self,id, *args, **kwargs):
      context = super(EschuView,self).get_context_data(*args, **kwargs)
      schudele = list(Schudele.objects.filter(Project_id=id).values('id','description','startHour','endHour','frecuencyHour','Periodicity','Project__name', 'Network__name'))
      context['schudele'] = schudele
      context['abc'] = id
      context['api'] = {
            'title': 'Projects',
        }
      return context


class CPView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/creacionProyectos.html'
   def get_context_data(self,id, *args, **kwargs):
      context = super(CPView,self).get_context_data(*args, **kwargs)
      context['api'] = {
            'title': 'Projects',
        }
      return context


class CCView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/creacionCronograma.html'

   def get_context_data(self,abc, *args, **kwargs):
      context = super(CCView,self).get_context_data(*args, **kwargs)
      networks = list(Network.objects.all())
      
      context['networks'] = networks
      context['usid'] = abc
      
      context['api'] = {
            'title': 'Projects',
        }
      return context
   
class AccView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/Account.html'
   def get_context_data(self,id, *args, **kwargs):   
      context = super(AccView,self).get_context_data(*args, **kwargs)
      account = list(Account.objects.filter(Schudele_id=id).values())
      
      context['accounts'] = account
      context['abc'] = id
      context['api'] = {
            'title': 'Projects',
        }
      return context
   
class EdACCView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/edicionAcc.html'

   def get_context_data(self,id, *args, **kwargs):
      context = super(EdACCView,self).get_context_data(*args, **kwargs)
      account = Account.objects.get(id=id)
      context['account'] = account
      
      context['api'] = {
            'title': 'Projects',
        }
      return context

class CAccView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/creacionAcc.html'
 #id cuenta
   def get_context_data(self,abc, *args, **kwargs):
      context = super(CAccView,self).get_context_data(*args, **kwargs)
  
      context['usid'] = abc
      
      context['api'] = {
            'title': 'Projects',
        }
      return context

class DataView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/Data.html'
   def get_context_data(self,id, *args, **kwargs):   
      context = super(DataView,self).get_context_data(*args, **kwargs)
      data = list(Data.objects.filter(Account_id=id).values())
      context['accounts'] = data
      context['abc'] = id
      context['api'] = {
            'title': 'Projects',
        }
      return context
   
class EdDataView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/edicionData.html'

   def get_context_data(self,id, *args, **kwargs):
      context = super(EdDataView,self).get_context_data(*args, **kwargs)
      data = Data.objects.get(id=id)
      context['account'] = data
      
      context['api'] = {
            'title': 'Projects',
        }
      return context
   
class CDataView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/creacionData.html'
 #id cuenta
   def get_context_data(self,abc, *args, **kwargs):
      context = super(CDataView,self).get_context_data(*args, **kwargs)
   
      context['usid'] = abc
      
      context['api'] = {
            'title': 'Projects',
        }
      return context
   
class NetView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/Network.html'
   def get_context_data(self, *args, **kwargs):   
      context = super(NetView,self).get_context_data(*args, **kwargs)
      network = list(Network.objects.all())
      context['accounts'] = network
      context['api'] = {
            'title': 'Projects',
        }
      return context
   
class EdNetView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/edicionNetwork.html'

   def get_context_data(self,id, *args, **kwargs):
      context = super(EdNetView,self).get_context_data(*args, **kwargs)
      net = Network.objects.get(id=id)
      context['account'] = net
      
      context['api'] = {
            'title': 'Projects',
        }
      return context
   
class CNetView(LoginRequiredMixin, TemplateView):
   template_name = 'app/project/creacionNetwork.html'
 #id cuenta
   def get_context_data(self, *args, **kwargs):
      context = super(CNetView,self).get_context_data(*args, **kwargs)
      context['api'] = {
            'title': 'Projects',
        }
      return context