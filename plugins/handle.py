# encoding: utf-8

"""You can write youself control code in here..."""

def wyproxy_request_handle(flow):
    """wyproxy send data to server before processing"""

    # disable cache
    flow.request.anticache()

    # disable gzip compress
    flow.request.anticomp()

    # change the request headers['Host']
    # flow.request.headers['X-Online-Host'] = 'wap.gd.10086.cn'

def wyproxy_response_handle(flow):
    """wyproxy request task is over"""

    # print(flow.request.url)
    # print(flow.request.headers)
    # print(flow.response.headers)
    pass
