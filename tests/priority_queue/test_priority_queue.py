from ting_file_management.priority_queue import PriorityQueue

# import pytest


def test_basic_priority_queueing():
    queue_with_priority = PriorityQueue()
    queue_with_priority.enqueue({"qtd_linhas": 2})
    queue_with_priority.enqueue({"qtd_linhas": 12})
    queue_with_priority.enqueue({"qtd_linhas": 3})
    queue_with_priority.enqueue({"qtd_linhas": 8})

    assert queue_with_priority.dequeue() == {"qtd_linhas": 12}
    assert queue_with_priority.search(0) == {"qtd_linhas": 2}


# def test_tries_to_remove_nothing():
#     queue_with_priority = PriorityQueue()
#     queue_with_priority.dequeue()

#     with pytest.raises(IndexError):
#         queue_with_priority.search(0)
