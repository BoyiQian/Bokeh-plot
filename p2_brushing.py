from logging import log
from bokeh.layouts import column, gridplot, row
from bokeh.models.annotations import ColorBar, Legend, LegendItem, Title
from bokeh.models.glyphs import Circle
from bokeh.models.mappers import LinearColorMapper
from bokeh.models.sources import ColumnDataSource
from bokeh.models import CustomJS, Dropdown
from bokeh.models.transforms import LinearInterpolator
from bokeh.palettes import Blues256, Colorblind, Magma256, Oranges, Turbo256, Viridis256, mpl
from bokeh.transform import linear_cmap
from bokeh.models.widgets import Select,MultiSelect, Slider
from numpy import sqrt, square
import numpy as np
from numpy.core.arrayprint import format_float_positional
import pandas as pd
from bokeh.plotting import figure, output_file, show, curdoc


file = "factbook.csv"
data = pd.read_csv(file)
data = data.drop(["Country","Current account balance","Natural gas consumption"],axis=1)


output_file('Q3.html')


bokeh_doc=curdoc()

for name in data.columns.values.tolist():
    try:
        data[name] = data[name].replace({"\$": "", ",": "", " ":"0"}, regex=True).astype(float)
    except ValueError:
        continue

menu=[]
for name in data.columns.values.tolist():
    newname = name + " to size"
    data[newname] = 10 + (200 - 10) / (data[name].max() - data[name].min()) * (data[name] - data[name].min())
    menu.append(name)

data["size"] = data["Population to size"]
data["color"]=data[" Birth rate"]

source=ColumnDataSource(data={
    '1x':data["GDP per capita"],
    '1y':data["Life expectancy at birth"],
    '2x': data["GDP per capita"],
    '2y': data["Life expectancy at birth"],
    '3x': data["GDP per capita"],
    '3y': data["Life expectancy at birth"],
    '4x': data["GDP per capita"],
    '4y': data["Life expectancy at birth"],
    'size':data["size"],
    'color':data["color"]
})

def callback11(attr, old, new):
    current_size = select3.value + " to size"
    source.data ={
        '1x': data[new],
        '1y': data[select21.value],
        '2x': data[select12.value],
        '2y': data[select22.value],
        '3x': data[select13.value],
        '3y': data[select23.value],
        '4x': data[select14.value],
        '4y': data[select24.value],
        'size': data["size"],
        'color': data["color"]
    }
    update()


select11 = Select(title="plot 1 x", options=menu, value = "GDP per capita")
select11.on_change("value", callback11)

def callback12(attr, old, new):
    current_size = select3.value + " to size"
    source.data ={
        '1x': data[select11.value],
        '1y': data[select21.value],
        '2x': data[new],
        '2y': data[select22.value],
        '3x': data[select13.value],
        '3y': data[select23.value],
        '4x': data[select14.value],
        '4y': data[select24.value],
        'size': data["size"],
        'color': data["color"]
    }
    update()

select12 = Select(title="plot 2 x", options=menu, value = "GDP per capita")
select12.on_change("value", callback12)

def callback13(attr, old, new):
    current_size = select3.value + " to size"
    source.data ={
        '1x': data[select11.value],
        '1y': data[select21.value],
        '2x': data[select12.value],
        '2y': data[select22.value],
        '3x': data[new],
        '3y': data[select23.value],
        '4x': data[select14.value],
        '4y': data[select24.value],
        'size': data["size"],
        'color': data["color"]
    }
    update()
select13 = Select(title="plot 3 x", options=menu, value = "GDP per capita")
select13.on_change("value", callback13)

def callback14(attr, old, new):
    current_size = select3.value + " to size"
    source.data ={
        '1x': data[select11.value],
        '1y': data[select21.value],
        '2x': data[select12.value],
        '2y': data[select22.value],
        '3x': data[select13.value],
        '3y': data[select23.value],
        '4x': data[new],
        '4y': data[select24.value],
        'size': data["size"],
        'color': data["color"]
    }
    update()
select14 = Select(title="plot 4 x", options=menu, value = "GDP per capita")
select14.on_change("value", callback14)

################ widget 2 #################
def callback21(attr, old, new):
    current_size = select3.value + " to size"
    source.data ={
        '1x': data[select11.value],
        '1y': data[new],
        '2x': data[select12.value],
        '2y': data[select22.value],
        '3x': data[select13.value],
        '3y': data[select23.value],
        '4x': data[select14.value],
        '4y': data[select24.value],
        'size': data["size"],
        'color': data["color"]
    }
    update()

select21 = Select(title="plot 1 y", options=menu, value = "Life expectancy at birth")
select21.on_change("value", callback21)

def callback22(attr, old, new):
    current_size = select3.value + " to size"
    source.data ={
        '1x': data[select11.value],
        '1y': data[select21.value],
        '2x': data[select12.value],
        '2y': data[new],
        '3x': data[select13.value],
        '3y': data[select23.value],
        '4x': data[select14.value],
        '4y': data[select24.value],
        'size': data["size"],
        'color': data["color"]
    }
    update()

select22 = Select(title="plot 2 y", options=menu, value = "Life expectancy at birth")
select22.on_change("value", callback22)

def callback23(attr, old, new):
    current_size = select3.value + " to size"
    source.data ={
        '1x': data[select11.value],
        '1y': data[select21.value],
        '2x': data[select12.value],
        '2y': data[select22.value],
        '3x': data[select13.value],
        '3y': data[new],
        '4x': data[select14.value],
        '4y': data[select24.value],
        'size': data["size"],
        'color': data["color"]
    }
    update()

select23 = Select(title="plot 3 y", options=menu, value = "Life expectancy at birth")
select23.on_change("value", callback23)

def callback24(attr, old, new):
    current_size = select3.value + " to size"
    source.data ={
        '1x': data[select11.value],
        '1y': data[select21.value],
        '2x': data[select12.value],
        '2y': data[select22.value],
        '3x': data[select13.value],
        '3y': data[select23.value],
        '4x': data[select14.value],
        '4y': data[new],
        'size': data["size"],
        'color': data["color"]
    }
    update()
select24 = Select(title="plot 4 y", options=menu, value = "Life expectancy at birth")
select24.on_change("value", callback24)


################ widget 3 #################
def callback3(attr, old, new):
    current_size = new + " to size"
    data["size"] = data[current_size]
    source.data ={
        '1x': data[select11.value],
        '1y': data[select21.value],
        '2x': data[select12.value],
        '2y': data[select22.value],
        '3x': data[select13.value],
        '3y': data[select23.value],
        '4x': data[select14.value],
        '4y': data[select24.value],
        'size': data["size"],
        'color': data["color"]
    }
    update()




select3 = Select(title="size", options=menu, value = "Population")
select3.on_change("value", callback3)

################ widget 4 #################
def callback4(attr, old, new):
    current_size = select3.value + " to size"
    data["color"] = data[new]
    source.data ={
        '1x': data[select11.value],
        '1y': data[select21.value],
        '2x': data[select12.value],
        '2y': data[select22.value],
        '3x': data[select13.value],
        '3y': data[select23.value],
        '4x': data[select14.value],
        '4y': data[select24.value],
        'size': data["size"],
        'color': data["color"]
    }
    #data["color"] = 256/ (data[new].max() - data[new].min()) * (data[new] - data[new].min())
    update()

select4 = Select(title="color", options=menu, value = " Birth rate")
select4.on_change("value", callback4)


def creat_legend():
    ###legend
    p2_x = [0,0,0]
    p2_y = [0, 3.7,8]
    size = [10,100, 200]
    x0 = [0.5, 25, 45]
    x1 = [60,60,60]
    text = [data[select3.value].min(),
            (9/19) * (data[select3.value].max()-data[select3.value].min())+data[select3.value].min(),data[select3.value].max()]
    p2 = figure(width=500, height=500, x_range=(-100,100), y_range=(-10,30), title = "bubble size legend")
    p2.circle(x=p2_x, y=p2_y, size=size, fill_alpha=0, line_color='black', line_width=2, radius_dimension='y')
    p2.segment(x0=x0, y0=p2_y, x1=x1, y1=p2_y, line_dash='dashed', line_color='black')
    p2.text(x=62, y=[v - 1 for v in p2_y], text=[str(v) for v in text])
    p2.xaxis.visible = False
    p2.yaxis.visible = False
    return p2

def creat_figure():
    tools = 'pan,wheel_zoom,xbox_select,reset'
    plot1 = figure(title=select11.value + " vs " + select21.value, tools=tools, width=800, height=800)
    plot2 = figure(title=select12.value + " vs " + select22.value, tools=tools, width=800, height=800)
    plot3 = figure(title=select13.value + " vs " + select23.value, tools=tools, width=800, height=800)
    plot4 = figure(title=select14.value + " vs " + select24.value, tools=tools, width=800, height=800)

    # print(data[select4.value])
    plot1.xaxis.axis_label = select11.value
    plot1.yaxis.axis_label = select21.value

    plot2.xaxis.axis_label = select21.value
    plot2.yaxis.axis_label = select22.value

    plot3.xaxis.axis_label = select13.value
    plot3.yaxis.axis_label = select23.value

    plot4.xaxis.axis_label = select14.value
    plot4.yaxis.axis_label = select24.value

    color_mapper = linear_cmap(field_name='color', palette=Viridis256, low=data["color"].min(),
                               high=data["color"].max())

    plot1.circle('1x', '1y', source=source, fill_color=color_mapper, fill_alpha=0.6, line_color="black", size='size')
    plot2.circle('2x', '2y', source=source, fill_color=color_mapper, fill_alpha=0.6, line_color="black", size='size')
    plot3.circle('3x', '3y', source=source, fill_color=color_mapper, fill_alpha=0.6, line_color="black", size='size')
    plot4.circle('4x', '4y', source=source, fill_color=color_mapper, fill_alpha=0.6, line_color="black", size='size')

    color_bar = ColorBar(color_mapper=color_mapper['transform'], width=20, height=600, label_standoff=8,
                         title=str(select4.value))
    plot1.add_layout(color_bar, 'right')
    plot2.add_layout(color_bar, 'right')
    plot3.add_layout(color_bar, 'right')
    plot4.add_layout(color_bar, 'right')
    return plot1, plot2, plot3, plot4

def update():
    plot1, plot2, plot3, plot4 = creat_figure()
    layout.children[1].children[0]= plot1
    layout.children[1].children[1]= plot3
    layout.children[2].children[0]= plot2
    layout.children[2].children[1]= plot4
    layout.children[3]=creat_legend()



plot1, plot2, plot3, plot4 = creat_figure()
r1 = column(plot1, plot3)
r2 = column(plot2, plot4)

widgets = column(select11, select21, select12,select22,select13,select23,select14,select24, select3, select4)
layout = row(widgets, r1, r2, creat_legend())

bokeh_doc.title = "Task 3"
bokeh_doc.add_root(layout)

