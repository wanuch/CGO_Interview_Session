from rest_framework.views import APIView
from rest_framework.response import Response

import CGO_Interview_Session.module as module

class index(APIView):


    def get(self, request):

        X = 5
        A = [1,3,1,4,2,3,5,4]
        
        return Response(module.solution(X, A))