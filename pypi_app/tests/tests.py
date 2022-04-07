import pytest
from pypi_app.models import Item

# Create your tests here.
@pytest.mark.django_db
def test_all_packages(client, create_items):
    response = client.get("/")
    assert response.status_code == 200
    assert len(response.context['result']) == Item.objects.all().count()


@pytest.mark.django_db
def test_search_packages(client, create_items):
    item = Item.objects.all().order_by('-title').first()
    search = item.title[:3]

    response = client.post("/", {'search': search})
    assert response.status_code == 200

    assert len(response.context['result']) < Item.objects.all().count()
    assert len(response.context['result']) > 0


@pytest.mark.django_db
def test_api_search_packages(client, create_items):
    item = Item.objects.all().order_by('-title')
    search = item.first().title[:3]
    search += ' ' + item[1].author_name[:3]

    response = client.post("/api/", {'search': search}, format='json')

    assert response.status_code == 200
    assert len(response.data) < Item.objects.all().count()
    assert len(response.data['packages']) > 1

    search = item.first().title[:3]
    response = client.post("/api/", {'search': search}, format='json')
    assert response.status_code == 200

    response = client.post("/api/", {'search': "there_is_no_way_to_find_this"}, format='json')
    assert response.status_code == 204
    assert not response.data

    response = client.post("/api/", {'search': ''}, format='json')
    assert response.status_code == 400
    assert not response.data