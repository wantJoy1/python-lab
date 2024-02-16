from random import randint, sample

def random() -> str:
    sentense = "モバイルバッテリー"
    random_size = randint(1, len(sentense))
    random_list = sample(list(sentense), random_size)
    return "".join(random_list)
