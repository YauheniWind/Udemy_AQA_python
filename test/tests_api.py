import allure

from serviceObject.http_service import HttpService


@allure.suite("Test API")
class TestAPI:
    @allure.title("Test API: get success status")
    def test_get_request(self):
        get_request = HttpService()
        get_request.get_status_200()

    @allure.title("Test API: create task")
    def test_create_task(self):
        create_task = HttpService()
        create_task.create_task()

    @allure.title("Test API: update task")
    def test_update_task(self):
        update_task = HttpService()
        update_task.update_data()

    @allure.title("Test API: create tasks")
    def test_list_tasks(self):
        list_tasks = HttpService()
        list_tasks.get_list_tasks()

    @allure.title("Test API: delete task")
    def test_delete_task(self):
        delete_task = HttpService()
        delete_task.delete_task()
