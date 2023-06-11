from HttpRequestsService.http_requests_service import HttpRequestsService


class TestAPI:

    def test_get_request(self):
        get_request = HttpRequestsService()
        get_request.test_get_status_200()

    def test_create_tasks(self):
        create_tasks = HttpRequestsService()
        create_tasks.test_create_task()