from django.shortcuts import render

# Create your views here.


def home(request):
    result = ""

    if request.method == "POST":
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            op = request.POST.get('operation')

            if op == 'add':
                result = num1 + num2
            elif op == 'sub':
                result = num1 - num2
            elif op == 'mul':
                result = num1 * num2
            elif op == 'div':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Divide by Zero.....!!"
        except:
            result = "Invalid input"

    return render(request, 'home.html', {'result': result})
