from django.shortcuts import render

def calc3(request):
    if request.method == "POST":
        erro = None
        try:
            odd1 = float(request.POST.get("odd1").replace(",", "."))
            odd2 = float(request.POST.get("odd2").replace(",", "."))
            odd3 = float(request.POST.get("odd3").replace(",", "."))
            surebet  = (1 / odd1) + (1 / odd2) + (1 / odd3)

            if surebet < 1:
                resultado = "Sem SureBet, não aposte"
            
            else:
                resultado = "Tem SureBet, pode apostar"

        except:
            erro = "ERRO: Insira números válidos"
            resultado = None
        
        return render(request, 'calculadora_3valores/index.html', {"resultado": resultado, "erro": erro })
    
    return render(request, "calculadora_3valores/index.html")