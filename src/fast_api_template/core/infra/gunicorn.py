from gunicorn.arbiter import Arbiter
from gunicorn.workers.base import Worker


def post_fork(server: Arbiter, worker: Worker) -> None:
    return
