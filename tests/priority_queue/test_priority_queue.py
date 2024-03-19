import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    # Criar uma fila de prioridade
    pq = PriorityQueue()

    # Adicionar arquivos com diferentes quantidades de linhas
    pq.enqueue({"nome": "arquivo1", "qtd_linhas": 9})  # não prioritário
    pq.enqueue({"nome": "arquivo2", "qtd_linhas": 4})  # prioritário
    pq.enqueue({"nome": "arquivo3", "qtd_linhas": 2})  # prioritário
    pq.enqueue({"nome": "arquivo4", "qtd_linhas": 5})  # não prioritário
    pq.enqueue({"nome": "arquivo5", "qtd_linhas": 7})  # não prioritário
    pq.enqueue({"nome": "arquivo6", "qtd_linhas": 11})  # não prioritário
    pq.enqueue({"nome": "arquivo7", "qtd_linhas": 3})  # prioritário

    # Testar o método dequeue
    assert pq.dequeue() == {
        "nome": "arquivo2",
        "qtd_linhas": 4,
    }  # primeiro prioritário
    assert pq.dequeue() == {
        "nome": "arquivo3",
        "qtd_linhas": 2,
    }  # segundo prioritário
    assert pq.dequeue() == {
        "nome": "arquivo7",
        "qtd_linhas": 3,
    }  # terceiro prioritário
    assert pq.dequeue() == {
        "nome": "arquivo1",
        "qtd_linhas": 9,
    }  # primeiro não prioritário
    assert pq.dequeue() == {
        "nome": "arquivo4",
        "qtd_linhas": 5,
    }  # segundo não prioritário
    assert pq.dequeue() == {
        "nome": "arquivo5",
        "qtd_linhas": 7,
    }  # terceiro não prioritário
    assert pq.dequeue() == {
        "nome": "arquivo6",
        "qtd_linhas": 11,
    }  # quarto não prioritário

    # Testar o método search
    pq.enqueue({"nome": "arquivo8", "qtd_linhas": 2})  # prioritário
    pq.enqueue({"nome": "arquivo9", "qtd_linhas": 6})  # não prioritário

    assert pq.search(0) == {
        "nome": "arquivo8",
        "qtd_linhas": 2,
    }  # primeiro prioritário
    assert pq.search(1) == {
        "nome": "arquivo9",
        "qtd_linhas": 6,
    }  # segundo não prioritário

    # Testar exceção ao acessar índices inválidos
    with pytest.raises(IndexError):
        pq.search(2)

    with pytest.raises(IndexError):
        pq.search(-1)
