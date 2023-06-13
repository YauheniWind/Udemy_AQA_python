import allure

from HttpRequestsService.http_requests_service import HttpRequestsService


@allure.suite("Test API")
class TestAPI:
    @allure.title("Test API: get success status")
    def test_get_request(self):
        get_request = HttpRequestsService()
        get_request.test_get_status_200()

    @allure.title("Test API: create task")
    def test_create_task(self):
        create_tasks = HttpRequestsService()
        create_tasks.test_create_task()

    @allure.title("Test API: update task")
    def test_update_task(self):
        update_task = HttpRequestsService()
        update_task.test_update_data()

    @allure.title("Test API: create tasks")
    def test_list_tasks(self):
        list_tasks = HttpRequestsService()
        list_tasks.test_get_list_tasks()

    @allure.title("Test API: delete task")
    def test_delete_task(self):
        delete_task = HttpRequestsService()
        delete_task.test_delete_task()
