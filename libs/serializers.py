#these classes take python objects and turn them into JSON objects.

from rest_framework.serializers import ModelSerializer
from .models import Author, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ["name", "authors", "publication_year", "edition"]

    def create(self, validated_data):
        authr = validated_data.pop('authors')
        bk = Book.objects.create(**validated_data)
        bk.save()

        for athr in authr:
           a = Author.objects.create(name=athr["name"])
           a.save()
           bk.authors.add(a)
           
        return bk

    def update(self, instance, validated_data):
        
        instance_authors = validated_data["authors"]
        instance.name = validated_data.get("name", instance.name)
        instance.publication_year = validated_data.get("publication_year", instance.publication_year)
        instance.edition = validated_data.get("edition", instance.edition)
        

        inst_authors = [c["name"] for c in instance_authors]

        prev_authors = [f.name for f in instance.authors.all()]
        for d in inst_authors:
            if d in prev_authors:
                continue
            else:
                at = Author.objects.create(name=d)
                instance.authors.add(at)
                instance.save()

        print(instance.authors.all())
        
        return instance

