import matplotlib.pyplot as pltt 

def generate_bar_chart(labels, values):    
    fig, ax = pltt.subplots()
    ax.bar(labels, values)
    pltt.show()

def generate_pie_chart(labels, values):
    fig, ax = pltt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    pltt.show()

if __name__ == "__main__":
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)