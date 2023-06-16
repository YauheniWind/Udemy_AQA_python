import requests
import uuid


class HttpRequestsService:
    url_todo_pixegami = "https://todo.pixegami.io"

    def requests_get_status(self):
        response = requests.request("GET", self.url_todo_pixegami)
        return response

    def requests_create_task(self, payload):
        return requests.request("PUT", self.url_todo_pixegami + "/create-task", json=payload)

    def requests_update_task(self, payload):
        return requests.request("PUT", self.url_todo_pixegami + "/update-task", json=payload)

    def requests_get_task(self, task_id):
        return requests.request("GET", self.url_todo_pixegami + f"/get-task/{task_id}")

    def requests_get_list_tasks(self, user_id):
        return requests.request("GET", self.url_todo_pixegami + f"/list-tasks/{user_id}")

    def requests_delete_task(self, task_id):
        return requests.request("DELETE", self.url_todo_pixegami + f"/delete-task/{task_id}")

    @staticmethod
    def new_task():
        user_id = uuid.uuid4().hex
        content = uuid.uuid4().hex

        return {
            "content": f"Hello_{content}",
            "user_id": f"test_user_{user_id}",
            "is_done": False,
        }
