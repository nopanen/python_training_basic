import random
# import plotly.plotly as py
# import plotly.graph_objs as go


# py.sign_in(username='your_user_name', api_key='your_api_key')


def one_try():
    """
    returns True if stick wins
    """

    items = [0, 1, 2]
    random.shuffle(items)

    correctitem = random.choice(items)
    selection = random.choice(items)

    return selection == correctitem


def run_trials(trials):
    """
    run n trials and save number of both outcomes
    """

    timeswon = 0
    timeslost = 0

    for trial in range(trials):
        res = one_try()
        if res:
            timeswon += 1
        else:
            timeslost += 1

    return [timeswon, timeslost]


def display_sim(sim_result):
    """
    Make a piechart with plotly
    """
    pass

res = run_trials(100)
print "Won: " + str(res[0]) + ". Lost: " + str(res[1])