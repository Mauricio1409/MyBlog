from rest_framework.permissions import BasePermission
from comments.models import Comments

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):

        # Verifica si el metodo es GET o POST
        if request.method == 'GET' or request.method == 'POST':
            return True
        
        # Si no es GET o POST verifica si es de ese usuario
        else:

            # Obtener id del comentario y comentario con el id
            id_comment = view.kwargs['pk']
            comment = Comments.objects.get(pk=id_comment)

            # Obtener el id del usuario y el id del comentario 
            id_user = request.user.pk
            id_user_comment = comment.user_id

            # Verificar si son iguales
            if id_user == id_user_comment:
                return True
            
            return False