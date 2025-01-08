def get_runner_up(scores):
    max_score = max(scores)
    scores = [score for score in scores if score != max_score]
    return max(scores)

if __name__ == '__main__':
    n = int(input())
    scores = map(int, input().split())
    scores = list(scores)
    runner_up = get_runner_up(scores)
    print(runner_up)
