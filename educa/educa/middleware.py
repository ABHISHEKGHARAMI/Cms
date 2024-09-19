'''import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = datetime.now()
        logger.info(
            f'Time: {start_time}, Operation: {request.method}, URL: {request.get_full_path()}'
        )

        response = self.get_response(request)

        end_time = datetime.now()
        time_taken = (end_time - start_time).total_seconds()
        logger.info(
            f'Response status: {response.status_code}, Time taken: {time_taken} seconds'
        )

        return response
'''