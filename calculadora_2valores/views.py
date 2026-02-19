from django.shortcuts import render

def calc2(request):
    if request.method == "POST":
        erro = None
        try:
            odd1 = float(request.POST.get("odd1").replace(",", "."))
            odd2 = float(request.POST.get("odd2").replace(",", "."))
            surebet  = (1 / odd1) + (1 / odd2)

            if surebet > 1:
                resultado = "Sem SureBet, não aposte"
            
            else:
                resultado = "Tem SureBet, pode apostar"

        except:
            erro = "ERRO: Insira números válidos"
            resultado = None
        
        return render(request, 'calculadora_2valores/index.html', {"resultado": resultado, "erro": erro })
    
    return render(request, "calculadora_2valores/index.html")