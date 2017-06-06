import matplotlib.pyplot as plt
import matplotlib


def get_list(result, data):
    list = []
    count = 0
    for r in result:
        count = count + 1
        list.append(r[data]['count'])
    return list,count


def plot(name,list, count):
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    locator = matplotlib.ticker.NullLocator()
    axes.xaxis.set_major_locator(locator=locator)
    plt.plot(range(count), list)
    plt.title(name)
    plt.savefig(name+'.png', format='png')
    plt.clf()


def plot_system(result):
    matplotlib.rc('font', family='Verdana')
    ylist, count = get_list(result,'likes')
    plot('likes',ylist,count)
    ylist, count = get_list(result, 'views')
    plot('views', ylist, count)
    ylist, count = get_list(result, 'comments')
    plot('comments', ylist, count)
