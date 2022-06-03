import constant.request
from model.request_info import RequestInfo
from service.crawl import crawl_message
import service.precondition

if __name__ == '__main__':
    try:
        headers = service.precondition.get_real_headers()
    except Exception as e:
        headers = constant.request.BACKUP_HEADERS
        print(e)

    request_info = RequestInfo().headers_only(headers)
    crawl_message(request_info)