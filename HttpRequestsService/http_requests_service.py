import json
import requests
import random

url = "https://todo.pixegami.io"


class HttpRequestsService:

    def test_get_status_200(self):
        response = requests.request("GET", url)

        assert response.status_code == 200


    def test_create_task(self):
        payload = self.new_task()

        create_task_response = self.create_task(payload)
        data = create_task_response.json()

        task_id = data['task']['task_id']
        get_task_id_response = self.get_task(task_id)

        assert create_task_response.status_code == 200
        get_data_task = get_task_id_response.json()

        assert get_data_task['user_id'] == payload['user_id']
        assert get_data_task['content'] == payload['content']

    def test_update_data(self):
        payload = self.new_task()
        create_task = self.create_task(payload)
        task_id = create_task.json()['task']['task_id']

        new_payload = {
            "user_id": payload["user_id"],
            "task_id": task_id,
            "content": "my contend is updated",
            "is_done": True
        }
        update_task = self.update_task(new_payload)
        assert update_task.status_code == 200

        get_data = self.get_task(task_id).json()

        assert get_data["content"] == new_payload["content"]
        assert get_data["is_done"] == new_payload["is_done"]


    def create_task(self, payload):
        return requests.request('PUT', url + '/create-task', json=payload)

    def update_task(self, payload):
        return requests.request('PUT', url + '/update-task', json=payload)

    def get_task(self, task_id):
        return requests.request('GET', url + f'/get-task/{task_id}')

    def new_task(self):
        return {
            "content": "Hello",
            "user_id": "test_user",
            "is_done": False
        }