from rest_framework.serializers import ModelSerializer
from .models import *



class GeneralSerializer(ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = '__all__'

    

class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

    

class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'



class ResumeSerializer(ModelSerializer):
    general = GeneralSerializer()
    experience = ExperienceSerializer(many=True)
    education = EducationSerializer()

    class Meta:
        model = Resume
        fields = '__all__'


    def create(self,validated_data):
        general_info = GeneralInfo.objects.create(**validated_data['general'])
        #my_experience = Experience.objects.create(**validated_data['experience'])
        #my_education = Education.objects.create(**validated_data['education'])
        
        resume = Resume(
            general=general_info,
            #experience=my_experience,
            #education=my_education,
        )
        resume.save()

        for education in validated_data['education']:
            new_education = Education.objects.create(**education)
            resume.education.add(new_education)
        for experience in validated_data['experience']:
            new_experience = Experience.objects.create(**experience)
            resume.experience.add(new_experience)

        resume.save()

        return resume
    

    def update(self,instance, validated_data):
        experiences = validated_data.pop('experience')
        education_list = validated_data.pop('education')

        instance.experience.clear()
        instance = super().update(instance, validated_data)


        for education in education_list:
            if 'id' in education.keys():
                instance.education.add(education)
            else:
                new_education = Experience.objects.create(**education)
                instance.education.add(new_education)

        for experience in experiences:
            if 'id' in experience.keys():
                instance.experience.add(experience)
            else:
                new_experience = Experience.objects.create(**experience)
                instance.experience.add(new_experience)

        instance.save()
        return instance 



