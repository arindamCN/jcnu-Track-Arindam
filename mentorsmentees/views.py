from django.shortcuts import render # Arindam File
from django.views.generic import View
from django.http import HttpResponse
from mentorsmentees.models import Person
import json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class AddView(View):
    def get(self,request):
        html = "<html><body>Hi bro</body></html>" 
        return HttpResponse(html)

    def post(self,request):
        print(request.body)
        print(request.body.decode('utf-8'))
        # print(request.body.decode('utf-8').split('=')[1])
        json_data = json.loads(request.body.decode('utf-8'))
        person = Person(name=json_data['name'])
        person.save()
        return HttpResponse(person)


@method_decorator(csrf_exempt, name='dispatch')
class AddMenteeView(View):
    
    def get(self,request):
        html = "<html><body>Hi bro</body></html>" 
        return HttpResponse(html)

    def post(self,request):
        print(request.body.decode('utf-8'))
        json_data = json.loads(request.body.decode('utf-8'))

        person1 = Person.nodes.get(name=json_data['Mentor'])
        person2 = Person.nodes.get(name=json_data['Mentee'])
        # a = request.body.decode('utf-8').split('&')
        # person1 = Person.nodes.get(name=a[0].split("=")[1])
        # person2 = Person.nodes.get(name=a[1].split("=")[1])
        person1.mentee.connect(person2)

        return HttpResponse(person1.mentee)

@method_decorator(csrf_exempt, name='dispatch')
class ShowMenteesView(View):
    def get(self,request):

        print(request.body.decode('utf-8'))
        json_data = json.loads(request.body.decode('utf-8'))
        # person1 = Person.nodes.get(name=request.body.decode('utf-8').split('=')[1])
        person1 = Person.nodes.get(name=json_data['Mentor'])

        print(person1.getmentees())
        
        return HttpResponse(person1.getmentees())

    def post(self,request):
        OUTGOING = 1
        print(request.body.decode('utf-8'))
        #json_data = json.loads(request.body.decode('utf-8'))
        # person1 = Person.nodes.get(name=json_data['Mentor'])
        json_data = json.loads(request.body.decode('utf-8'))
        # person1 = Person.nodes.get(name=request.body.decode('utf-8').split('=')[1])
        person1 = Person.nodes.get(name=json_data['Mentor'])
        
        output = []
        a = person1.getmentees()
        for i in range(0,len(a)):
            output.append(a[i].__str__())
        
        output = json.dumps(output)
        return HttpResponse(output)




