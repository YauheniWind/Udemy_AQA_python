import requests
import allure
from serviceObject.http_requests_service import HttpRequestsService

url = "https://todo.pixegami.io"


class HttpService(HttpRequestsService):
    @allure.step("get response 200")
    def get_status_200(self):
        response = requests.request("GET", url)

        assert response.status_code == 200

    @allure.step("created task")
    def create_task(self):
        payload = self.new_task()
        create_task_response = self.requests_create_task(payload)
        data = create_task_response.json()

        task_id = data["task"]["task_id"]
        get_task_id_response = self.requests_get_task(task_id)

        assert create_task_response.status_code == 200
        get_data_task = get_task_id_response.json()

        assert get_data_task["user_id"] == payload["user_id"]
        assert get_data_task["content"] == payload["content"]

    @allure.step("updated task")
    def update_data(self):
        payload = self.new_task()
        create_task = self.requests_create_task(payload)
        task_id = create_task.json()["task"]["task_id"]

        new_payload = {
            "user_id": payload["user_id"],
            "task_id": task_id,
            "content": "my contend is updated",
            "is_done": True,
        }
        update_task = self.requests_update_task(new_payload)
        assert update_task.status_code == 200

        get_data = self.requests_get_task(task_id).json()

        assert get_data["content"] == new_payload["content"]
        assert get_data["is_done"] == new_payload["is_done"]

    @allure.step("get list of tasks")
    def get_list_tasks(self):
        payload = self.new_task()
        for _ in range(3):
            create_task = self.requests_create_task(payload)
            assert create_task.status_code == 200

        list_tasks = self.requests_get_list_tasks(payload["user_id"])
        assert list_tasks.status_code == 200

        data = list_tasks.json()

        tasks = data["tasks"]
        assert len(tasks) == 3

    @allure.step("deleted task")
    def delete_task(self):
        payload = self.new_task()
        create_task = self.requests_create_task(payload)
        assert create_task.status_code == 200

        data_test_id = create_task.json()["task"]["task_id"]

        delete_test_id = self.requests_delete_task(data_test_id)
        assert delete_test_id.status_code == 200

        get_task_response = self.requests_get_task(data_test_id)
        assert get_task_response.status_code == 404