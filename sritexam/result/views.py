from django.shortcuts import render
d={'results':[
                {'name':'tharun','rollno':'214g1a32b3','ps':'4','fs':'2'},
                {'name':'keshav','rollno':'214g1a32a6','ps':'4','fs':'0'},
                {'name':'yeshwanth','rollno':'214g1a32c7','ps':'4','fs':'3'},
                {'name':'praveen','rollno':'214g1a3207','ps':'4','fs':'0'},
            ]}
# Create your views here.
def func(request,rollno):
    result=None
    for record in d.get('results'):
        if record.get('rollno')==rollno:
            result=record
            break
    if result is not None:
        return render(request,'result.html',result)
    else:
        return render(request,'result.html')

        
