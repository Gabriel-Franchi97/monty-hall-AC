import random


NUM_OF_SIMULATIONS = 10000
NUM_BOXES = 30
GUESS = 31


def monty_hall(num_boxes: int, guess: int):
    boxes = [num for num in range(num_boxes)]
    prize = random.choice(boxes)
    if guess not in boxes:
        raise Exception("guess should be inside the range of the doors")
    boxes.remove(guess)
    if guess != prize:
        boxes.remove(prize)
    print("host reveals all the other empty boxes, leaving you with two options")
    if guess==prize:
        return 0
    return 1


def proving_best_option_in_monty_hall(num_boxes: int, guess: int):
    win_by_remaining = 0
    win_by_switching = 0
    for _ in range(NUM_OF_SIMULATIONS):
        result = monty_hall(num_boxes, guess)
        if result > 0:
            win_by_switching += 1
        else:
            win_by_remaining += 1
    print(f"Total wins by switching: {win_by_switching}")
    print(f"Total wins by not switching: {win_by_remaining}")


if __name__ == "__main__":
    proving_best_option_in_monty_hall(NUM_BOXES, GUESS)