from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Instruction

@login_required
def all_instructions(request):
    instructions = Instruction.objects.all()
    context = {
        'instructions': instructions
    }
    return render(request, 'instructions/all.html', context)


@login_required
def instruction_detail(request, instruction_id):
    instruction = Instruction.objects.get(id=instruction_id)
    context = {
        'instruction': instruction
    }
    return render(request, 'instructions/single.html', context)
