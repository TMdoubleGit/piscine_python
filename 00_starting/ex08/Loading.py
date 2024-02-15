import time


class SimpleProgressBar:
    def __init__(self, total, length=65):
        self.total = total
        self.length = length

    def update(self, progress):
        percent = progress / self.total
        bar_length = int(percent * self.length)
        bar = ('%|' + '=' * (bar_length - 1) + '>' +
               '-' * (self.length - bar_length) + '|')
        progress_str = f'{progress}/{self.total}'
        displayed_percent = int(percent * 100)
        print(f'\r{displayed_percent}{bar} {progress_str}', end='', flush=True)


def ft_tqdm(lst: range) -> None:
    total_iterations = len(lst)
    progress_bar = SimpleProgressBar(total_iterations)

    for i, item in enumerate(lst):
        time.sleep(0.05)
        progress_bar.update(i + 1)

    yield item
    print()
