import requests
import uuid

url = "https://todo.pixegami.io"


class HttpRequestsService:
    def test_get_status_200(self):
        response = requests.request("GET", url)

        assert response.status_code == 200

    def test_create_task(self):
        payload = self.new_task()

        create_task_response = self.create_task(payload)
        data = create_task_response.json()

        task_id = data["task"]["task_id"]
        get_task_id_response = self.get_task(task_id)

        assert create_task_response.status_code == 200
        get_data_task = get_task_id_response.json()

        assert get_data_task["user_id"] == payload["user_id"]
        assert get_data_task["content"] == payload["content"]

    def test_update_data(self):
        payload = self.new_task()
        create_task = self.create_task(payload)
        task_id = create_task.json()["task"]["task_id"]

        new_payload = {
            "user_id": payload["user_id"],
            "task_id": task_id,
            "content": "my contend is updated",
            "is_done": True,
        }
        update_task = self.update_task(new_payload)
        assert update_task.status_code == 200

        get_data = self.get_task(task_id).json()

        assert get_data["content"] == new_payload["content"]
        assert get_data["is_done"] == new_payload["is_done"]

    def test_get_list_tasks(self):
        payload = self.new_task()
        for _ in range(3):
            create_task = self.create_task(payload)
            assert create_task.status_code == 200

        list_tasks = self.get_list_tasks(payload["user_id"])
        assert list_tasks.status_code == 200

        data = list_tasks.json()

        tasks = data["tasks"]
        assert len(tasks) == 3

    def test_delete_task(self):
        payload = self.new_task()
        create_task = self.create_task(payload)
        assert create_task.status_code == 200

        data_test_id = create_task.json()["task"]["task_id"]

        delete_test_id = self.delete_task(data_test_id)
        assert delete_test_id.status_code == 200

        get_task_response = self.get_task(data_test_id)
        assert get_task_response.status_code == 404

    def create_task(self, payload):
        return requests.request("PUT", url + "/create-task", json=payload)

    def update_task(self, payload):
        return requests.request("PUT", url + "/update-task", json=payload)

    def get_task(self, task_id):
        return requests.request("GET", url + f"/get-task/{task_id}")

    def get_list_tasks(self, user_id):
        return requests.request("GET", url + f"/list-tasks/{user_id}")

    def delete_task(self, task_id):
        return requests.request("DELETE", url + f"/delete-task/{task_id}")

    def new_task(self):
        user_id = uuid.uuid4().hex
        content = uuid.uuid4().hex

        return {
            "content": f"Hello_{content}",
            "user_id": f"test_user_{user_id}",
            "is_done": False,
        }
