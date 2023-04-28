import streamlit as st
import graphviz

if 'inputs' not in st.session_state:
    st.session_state['inputs'] = 1

a= []

st.title('KNAPSACK PROBLEM (GLOUTON)')
st.number_input(':red[CAPACITY OF THE SAC]',key='capacity')
col1,col2,col3 = st.columns([3,1,1])

for i in range(st.session_state['inputs']):
    if i ==0:
        label_visibility = 'visible'
    else:
        label_visibility = 'collapsed'
    with col1:
            st.text_input(':blue[Objet]',key='name'+str(i),label_visibility=label_visibility)
    with col2:
            st.number_input(':blue[Masse]',key='masse'+str(i),label_visibility=label_visibility)
    with col3:
            st.number_input(':blue[Utilité]',key='utilité'+str(i),min_value=0,label_visibility=label_visibility)

btn_col1,btn_col2,btn_col3 = st.columns([1,6.5,1])
with btn_col1:
    if st.button('ADD'):
        st.session_state['inputs'] = st.session_state['inputs']+1
        st.experimental_rerun()

with btn_col2:
    if st.session_state['inputs'] >1:
        if st.button('REMOVE'):
            st.session_state['inputs'] = st.session_state['inputs']-1
            st.experimental_rerun()

def affichage(l):
    graph = graphviz.Digraph()

    for i in l:
        graph.node(i)
    
    st.graphviz_chart(graph)

def glouton():
    #données
    masse_sac=0
    a_emporter=[]
    list_masse=[]
    list_utilite=[]
    j=0
    #création du dictionnaire
    for i in range(st.session_state['inputs']):
        a.append({
            'name': str(st.session_state['name'+str(i)]),
            'masse': str(st.session_state['masse'+str(i)]),
            'utilité': str(st.session_state['utilité'+str(i)]),
            })
    #rajout de l'utilité massique
    for objet in a:
        objet['utilite_massique']=eval(objet['utilité'])/eval(objet['masse'])
    sorted_a=sorted(a,key=lambda x: x['utilite_massique'])
    sorted_a.reverse()
    while j<len(sorted_a):
        if masse_sac + eval(sorted_a[j]['masse'])<= st.session_state['capacity']:
            masse_sac += eval(sorted_a[j]['masse'])
            a_emporter.append(sorted_a[j]['name'])
            #list_masse.append(float(sorted_a[j]['masse']))
            list_utilite.append(float(sorted_a[j]['utilité']))
        j=j+1
    st.text('Les objets que Adam peut emporter sont:')
    affichage(a_emporter)
    st.header("La solution optimale est d'utilité:" + " "+ str(int(sum(list_utilite))) )


with btn_col3:
    button= st.button('START')

if button:
    glouton()
        

        








