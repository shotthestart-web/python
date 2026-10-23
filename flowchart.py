from graphviz import Digraph
flowchart = Digraph('Daily_Routine', comment='My Daily Routine Flowchart')


flowchart.attr('node', fontname='Helvetica', fontsize='12', shape='box', style='filled', fillcolor='#f9f9f9', color='#333333')
flowchart.attr('edge', fontname='Helvetica', fontsize='10', color='#555555')


flowchart.node('Start', 'Start', shape='ellipse', fillcolor='#d4edda', color='#28a745') # Terminal block
flowchart.node('WakeUp', 'Wake Up\n(6:00 AM)')
flowchart.node('CheckDay', 'Is it a\nWeekend?', shape='diamond', fillcolor='#fff3cd', color='#ffc107') # Decision block
flowchart.node('WorkSchool', 'Go to Work / School')
flowchart.node('Relax', 'Enjoy Free Time / Hobbies')
flowchart.node('Lunch', 'Have Lunch')
flowchart.node('Dinner', 'Have Dinner & Wind Down')
flowchart.node('Sleep', 'Go to Bed')
flowchart.node('End', 'End', shape='ellipse', fillcolor='#f8d7da', color='#dc3545') # Terminal block


flowchart.edge('Start', 'WakeUp')
flowchart.edge('WakeUp', 'CheckDay')

flowchart.edge('CheckDay', 'Relax', label='Yes')
flowchart.edge('CheckDay', 'WorkSchool', label='No')

flowchart.edge('WorkSchool', 'Lunch')
flowchart.edge('Relax', 'Lunch')


flowchart.edge('Lunch', 'Dinner')
flowchart.edge('Dinner', 'Sleep')
flowchart.edge('Sleep', 'End')

flowchart.render('daily_routine_flowchart', format='png', cleanup=True)

print("Flowchart successfully generated and saved as 'daily_routine_flowchart.png'!")