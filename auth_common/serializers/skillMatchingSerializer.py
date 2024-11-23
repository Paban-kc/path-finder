# skillMatchingSerializer.py

from rest_framework import serializers
from auth_common.model.vacancy import Vacancy
from auth_common.serializers.register_organization.organizationListSerializer import OrganizationListSerializer
from auth_common.utils.jaccard_similarity import jaccard_similarity

class SkillsMatchingSerializer(serializers.ModelSerializer):
    organization=OrganizationListSerializer()
    class Meta:
        model = Vacancy
        fields = "__all__"

    def to_representation(self, instance):
        student = self.context.get('student')
        student_skills = set([skill.strip() for skill in student.skills.split(',') if skill.strip()])
        # print(">>>>>>>>>>>>>>>>>>>>",student_skills)
        vacancy_skills = set([skill.strip() for skill in instance.requirements.split(',') if skill.strip()])
        # print("organization req.",vacancy_skills)

        similarity_score = float(jaccard_similarity(student_skills, vacancy_skills))

        # Prepare the serialized data
        data = super().to_representation(instance)
        data['similarity_score'] = similarity_score
        return data
