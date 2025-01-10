import pytest
from rest_framework.test import APIClient

client=APIClient()
@pytest.mark.django_db
def test_register_user():
    
    payload=dict(
        
        username = "jack",
        password= "1Jack23@",
        password2= "1Jack23@",
        email= "jack23@gmail.com",
        first_name= "jack",
        last_name= "son"
    )
    
    response=client.post('/api/user/register',payload)
    data=response.data
    assert data['status']==201
    assert data['message']=='User added successfully'