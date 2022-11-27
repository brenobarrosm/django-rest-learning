from django.db.models import Avg
from rest_framework import serializers

from .models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

    def validate_avaliacao(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError('A avaliação precisa ser um número entre 1 e 5')

class CursoSerializer(serializers.ModelSerializer):
    #Nested Relationship
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #HyperLinked Related Field
    """
    avaliacoes = serializers.HyperlinkedRelatedField(many=True, 
                                                    read_only=True, 
                                                    view_name='avaliacao-detail')
    """

    #Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True,
                                                    read_only=True)
    
    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'media_avaliacoes',
            'avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        if media is None:
            return 0
        return round((media * 2) / 2)
