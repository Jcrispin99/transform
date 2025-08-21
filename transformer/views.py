from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    """Vista principal que muestra la interfaz del transformador de texto"""
    return render(request, 'transformer/index.html')

@csrf_exempt
def transform_text(request):
    """Vista que maneja la transformación de texto via AJAX"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            original_text = data.get('text', '')
            
            # Transformar el texto: reemplazar ` por -
            transformed_text = original_text.replace('`', '-')
            
            return JsonResponse({
                'success': True,
                'transformed_text': transformed_text
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})
