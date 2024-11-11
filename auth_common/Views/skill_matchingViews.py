from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from auth_common.model.student import Student
from auth_common.model.vacancy import Vacancy
from auth_common.serializers.skillMatchingSerializer import SkillsMatchingSerializer


class SkillsMatchingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        student = get_object_or_404(Student, user=request.user)

        vacancies = Vacancy.objects.all()

        matched_vacancies = []
        for vacancy in vacancies:
            # Pass student to the serializer's context
            serializer = SkillsMatchingSerializer(vacancy, context={'student': student})
            
            serializer_data = serializer.data
            
            if serializer_data.get('similarity_score', 0) > 0:
                matched_vacancies.append(serializer_data)

        # Sort the vacancies by similarity score in descending order
        matched_vacancies.sort(key=lambda x: x['similarity_score'], reverse=True)

        return Response(matched_vacancies)
