import networkx as nx
import matplotlib.pyplot as plt
import time
import vk

session = vk.Session(access_token='5914e9cf5914e9cf5914e9cf4159715e63559145914e9cf026dd056a192cf6e3c749885')
api = vk.API(session)

# создаем пустой граф
G = nx.Graph()

domain = 'm_sosin04'
ID = '350374836'

# выбираем группу
members = api.groups.getMembers(user_id=ID, fields='domain', v=5.74)

# каждого участника добавляем в граф
for member in members['items']:
    G.add_node(member['domain'], label='{} {}'.format(member['first_name'], member['last_name']))

for member in members['items']:
    try:
        print("current user: {} {}".format(member['first_name'], member['last_name']))
        # TODO: получить список друзей
        friends = []

        for friend in friends['items']:
            if friend in G:
                G.add_edge(member['first_name'], member['last_name'])
            # если друг есть в графе - добавить связь
                if G.has_node(friend['domain']):
                    G.add_edge(member['first_name'], member['last_name'])
                    # TODO: добавить ребро в граф
                    pass

        time.sleep(0.2)
    except Exception as e:
        print(e)

# сохраняем в файле
nx.write_gexf(G, 'friends.gexf')

# рисуем
pos=nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='red', node_size=50) 
nx.draw_networkx_edges(G, pos, edge_color='green')
nx.draw_networkx_labels(G, pos, font_size=11)
plt.axis('off')
plt.show()
