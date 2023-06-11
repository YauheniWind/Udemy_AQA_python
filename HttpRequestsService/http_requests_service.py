import json
import requests

url = "https://todo.pixegami.io"


class HttpRequestsService:

    def test_get_status_200(self):
        response = requests.request("GET", url)

        assert response.status_code == 200


    def test_create_task(self):
        payload = {
            "content": "My sunny day",
            "user_id": "ttt",
            "is_done": False
        }

        create_task_response = requests.request('PUT', url + '/create-task', json=payload)
        data = create_task_response.json()

        task_id = data['task']['task_id']
        get_task_id_response = requests.request('GET', url + f'/get-task/{task_id}')

        assert create_task_response.status_code == 200
        get_data_task = get_task_id_response.json()

        assert get_data_task['user_id'] == payload['user_id']
        assert get_data_task['content'] == payload['content']
