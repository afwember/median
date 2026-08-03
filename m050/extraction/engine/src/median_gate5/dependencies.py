from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass

from .errors import ContractError


@dataclass(frozen=True, order=True)
class DependencyEdge:
    upstream_id: str
    downstream_id: str
    relation: str


def stale_descendants(changed_ids: set[str], edges: list[DependencyEdge]) -> list[str]:
    graph: dict[str, set[str]] = defaultdict(set)
    for edge in edges:
        if not edge.upstream_id or not edge.downstream_id or not edge.relation:
            raise ContractError("dependency edge fields must be non-empty")
        graph[edge.upstream_id].add(edge.downstream_id)

    queue = deque(sorted(changed_ids))
    visited = set(changed_ids)
    descendants: set[str] = set()
    while queue:
        current = queue.popleft()
        for child in sorted(graph.get(current, set())):
            if child in visited:
                continue
            visited.add(child)
            descendants.add(child)
            queue.append(child)
    return sorted(descendants)
