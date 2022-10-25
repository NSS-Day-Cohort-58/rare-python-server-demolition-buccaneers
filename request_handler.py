from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
from views import get_all_posts, get_single_post, create_post, update_post, delete_post
from views import (
    get_all_categories,
    get_single_category,
    delete_category,
    update_category,
    # create_category,
)
from views import (
    get_all_subscriptions,
    get_single_subscription,
    create_subscription,
    delete_subscription,
    update_subscription,
)
from views.user_requests import create_user, login_user


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    # ========== GET REQUEST =========
    def do_GET(self):
        self._set_headers(200)

        response = {}

        # Parse URL and store entire tuple in a variable

        # getting a too many positional arguments error
        parsed = self.parse_url(self.path)

        # If the path does not include a query parameter, continue with the original if block
        if "?" not in self.path:
            (resource, id) = parsed

            if resource == "posts":
                if id is not None:
                    response = get_single_post(id)
                else:
                    response = get_all_posts()

            elif resource == "subscriptions":
                if id is not None:
                    response = get_single_subscription(id)
                else:
                    response = get_all_subscriptions()

            elif resource == "categories":
                if id is not None:
                    response = get_single_category(id)
                else:
                    response = get_all_categories()

        self.wfile.write(json.dumps(response).encode())

    # ========== POST REQUEST =========

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        resource, _ = self.parse_url(self.path)

        new_post = None

        if resource == 'login':
            response = login_user(post_body)

        if resource == 'register':
            response = create_user(post_body)

        if resource == "posts":
            response = create_post(post_body)
            # Encode the new post and send in response

        # currently not working
        # if resource == "categories":
        #     response = create_category(post_body)

        if resource == "subscriptions":
            response = create_subscription(post_body)

        self.wfile.write(response.encode())

        self.wfile.write(json.dumps(new_post).encode())

    # ========== PUT REQUEST =========
    def do_PUT(self):
        """Handles PUT requests to the server"""
        self._set_headers(204)
        content_len = int(self.headers.get("content-length", 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # getting a too many positional arguments error
        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "posts":
            success = update_post(id, post_body)
        elif resource == "subscriptions":
            success = update_subscription(id, post_body)
        elif resource == "categories":
            success = update_category(id, post_body)
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)
        # Encode the new post and send in response
        self.wfile.write("".encode())

# ========== DELETE REQUEST =========

    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        # getting a too many positional arguments error
        (resource, id) = self.parse_url(self.path)

        # Delete a single post from the list
        if resource == "posts":
            delete_post(id)
        elif resource == "subscriptions":
            delete_subscription(id)

        elif resource == "categories":
            delete_category(id)
        # Encode the new post and send in response
        self.wfile.write("".encode())

    # Another method! This supports requests with the OPTIONS verb.

    def do_OPTIONS(self):
        """Sets the OPTIONS headers"""
        self.send_response(200)

        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')

        self.end_headers()

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split("/")  # ['', 'animals', 1]
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()


def main():
    """Starts the server on port 8088 using the HandleRequests class"""
    host = ""
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
