from django.shortcuts import render

def calc3(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")
        erro = None

        try:
            if form_type == "odds":
                #primeiro_formulario
                odd1 = float(request.POST.get("odd1").replace(",", "."))
                odd2 = float(request.POST.get("odd2").replace(",", "."))
                odd3 = float(request.POST.get("odd3").replace(",", "."))
                numero1 = 1 / odd1
                numero2 = 1 / odd2
                numero3 = 1 / odd3
                surebet  = numero1 + numero2 +numero3

                if surebet > 1:
                    resultado = "Sem SureBet, não aposte"
                    tem_surebet = None
                
                else:
                    resultado = "Tem SureBet, pode apostar"
                    tem_surebet = "Sim"

                return render(request, 'calculadora_3valores/index.html', {"resultado": resultado, "tem_surebet": tem_surebet, "odd1":odd1, "odd2":odd2, "odd3":odd3})

            elif form_type == "valor":
                #segundo_formulario
                odd1 = float(request.POST.get("odd1").replace(",", "."))
                odd2 = float(request.POST.get("odd2").replace(",", "."))
                odd3 = float(request.POST.get("odd3").replace(",", "."))
                valor_total = float(request.POST.get("valor_total").replace(",", "."))

                numero1 = (1 / odd1)
                numero2 = (1 / odd2)
                numero3 = (1 / odd3)
                surebet = numero1 + numero2 + numero3
                apostar1 = round((numero1 / surebet) * valor_total, 2)
                apostar2 = round((numero2 / surebet) * valor_total, 2)
                apostar3 = round((numero3 / surebet) * valor_total, 2)

                return render(request, 'calculadora_3valores/index.html', {"apostar1": apostar1, "apostar2": apostar2, "apostar3": apostar3})

        except:
            erro = "ERRO: Insira números válidos"
        
        return render(request, 'calculadora_3valores/index.html', {"erro": erro})

    return render(request, "calculadora_3valores/index.html")