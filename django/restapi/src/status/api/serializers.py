from rest_framework import serializers
from status.models import Status
from accounts.api.serializers import UserPublicSerializer
from rest_framework.reverse import reverse as api_reverse




class StatusSerializer(serializers.ModelSerializer): # serializers konvertuju u JSON i validiraju podatke json.dumps() konvertuje recnik ili listu u string (tj recnik ili lista u okviru string), a json.loads() vraca nazad
	user = UserPublicSerializer(read_only=True)
	#user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
	#user_id = serializers.HyperlinkedRelatedField(source='user',
												  # lookup_field='username',
												  # view_name='api-user:detail', 
												  # read_only=True)
	uri = serializers.SerializerMethodField(read_only=True)
	#user = serializers.SerializerMethodField(read_only=True)
	#user = serializers.SlugRelatedField(read_only=True, slug_field='username')

	class Meta:
		model = Status
		fields = [
			'uri',
			'id',
			'user',
			'content',
			'image'

		]
		read_only_fields = ['user'] # za GET metod
	# def validate_content(self, value): # posle validate_ ide naziv polja koji hocu da validiram, validiranje na nivou odredjenog polja
	# 		raise serializers.ValidationError('content too long')
	# 	return value
	def get_uri(self, obj):
		request = self.context.get('request')

		return api_reverse('api-status:detail', kwargs={'id':obj.id}, request=request)

	# def get_user(self, obj):
	# 	request = self.content.get('request')
	# 	user = obj.user
	# 	return UserPublicSerializer(user, read_only=True, content={'request': request}).data

	def validate(self, data): # validiranje generalno
		content = data.get('content', None)
		if content == '':
			content - None
		image = data.get('image', None)
		if content is None and image is None:
			raise serializers.ValidationError('content or image required')
		return data

class StatusInlineUserSerializer(StatusSerializer): # serializers konvertuju u JSON i validiraju podatke json.dumps() konvertuje recnik ili listu u string (tj recnik ili lista u okviru string), a json.loads() vraca nazad
	#uri = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Status
		fields = [
			'uri',
			'id',
			'content',
			'image'
		]
	# def get_uri(self, obj):
	# 	return '/api/status/{id}/'.format(id=obj.id)