# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.http import HttpResponse

from web_neural.project.models import Subject, Style, Conversecpu, Conversegpu
from web_neural.project.forms import SubjectForm, StyleForm

from web_neural.project.neuralArtistic.gpuver.neural_artistic import Rungpu
from web_neural.project.neuralArtistic.cpuver.neural_artisticcpu import Runcpu

# Create your views here.
def list(request):
    #Handle file upload
    style_list = Style.objects.all()      
    if request.method == 'POST':
        subjectform = SubjectForm(request.POST, request.FILES)
        
        if subjectform.is_valid():
            newsub = Subject(subjectfile=request.FILES['subjectfile'])
            newsub.save()
            return render_to_response('list.html',{'subjectform': subjectform, 'style_list': style_list, 'sub': newsub }, context_instance=RequestContext(request))
    else:           
        subjectform = SubjectForm() # A empty, unbound for
        
    #Render list page with the documents and the form
    return render_to_response('list.html',{'subjectform': subjectform, 'style_list': style_list}, context_instance=RequestContext(request))
  
def conversing(request):
    
    sub = Subject.objects.last()
    sty= Style.objects.last()
    
    runcpu = Runcpu()
    rungpu = Rungpu()
    
    runcpu.setArg(sub.subjectfile.url , sty.stylefile.url)
    rungpu.setArg(sub.subjectfile.url , sty.stylefile.url)
    
    runcpu.start()
    rungpu.start()
    

    cpuconversing = Conversecpu.objects.last()
    cpuname= cpuconversing.get_file_name()
    
    gpuconversing = Conversegpu.objects.last()
    gpuname= gpuconversing.get_file_name()
    
    
    return render(request, 'conversing.html', {'cpuconv' : cpuname, 'gpuconv' : gpuname, 'cpuconverses' : cpuconversing, 'sub': sub, 'sty': sty})
    #return render(request, 'conversing.html', {'with_layout': with_layout ,'gpuconv' : gpuname, 'sub': sub, 'sty': sty})

def imge(request):
        
    cpuconversing = Conversecpu.objects.last()
    cpuname= cpuconversing.get_file_name()
    
    gpuconversing = Conversegpu.objects.last()
    gpuname= gpuconversing.get_file_name()
    
    tpl = loader.get_template("conview.html")
    ctx= RequestContext(request, {'cpuconv' : cpuname, 'gpuconv' : gpuname})
    #ctx= RequestContext(request, {'gpuconv' : gpuname})
    
    return HttpResponse(tpl.render(ctx))
    #return render(request, 'conview.html', {'with_layout': with_layout ,'conv' : name, 'converses' : conversing})
    