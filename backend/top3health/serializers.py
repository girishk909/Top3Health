from rest_framework import serializers
# from top3health.models import Goals
# from top3health.models import MyProfile


# class GoalsSerializer(serializers.ModelSerializer):

#         id = serializers.ReadOnlyField()

#         class Meta:
#             model = Goals
#             fields = ('id','Become_Healthier', 'Lose_Weight', 'Maintain_Weight','Gain_Weight','Improve_Productivity', 'Increase_Strength', 
#             'Increase_Endurance',  'Organize_Kitchen', 'Reduce_Stress', 'Improve_Sleep','Reduce_fast_foods',  
#             'Quit_Smoking', 'Quit_Alcohol', 'Include_Yoga', )
     
    
# class ProfileSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = MyProfile
#             fields = ['Height_ft_in', 'Weight_in_pounds', 'Gender', 'Calories_intake', 'Calories_burned', 
#             'Protein_intake', 'Carbs_intake', 'Water_intake', 'Stress_level', 'Sleep_quality', 'Race', 
#             'Ethnicity', 'Blood_type']    