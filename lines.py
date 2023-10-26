# read lines in group of `group_size` lines at a time
from typing import Iterator


def read_lines(filename: str, group_size: int | None = None) -> Iterator[str | tuple[str]]:
    assert (group_size is None) or (type(group_size) == int and group_size >= 2)
    with open(filename) as file:
        rv = []
        for line in file:
            line = line.strip()
            rv.append(line)
            if group_size is None or len(rv) == group_size:
                if group_size:
                    yield tuple(rv)
                else:
                    yield rv[0]
                rv = []

        # make sure we don't leave any extra lines
        assert not rv, f'{len(rv)} left unprocessed at the end of the file!'
