from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .services.ai_service import generate_email

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def ai_generate(request):
    """
    Minimal AI endpoint — expects JSON {"prompt": "...", "type": "email"}
    Returns { result: "..." }
    """
    prompt = request.data.get("prompt", "")
    if not prompt:
        return Response({"error": "prompt required"}, status=400)

    result = generate_email(prompt)
    return Response({"result": result})

