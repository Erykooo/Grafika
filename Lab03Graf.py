import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

Path = mpath.Path
fig, ax = plt.subplots()

### LITERA E
### fc = none ustawia sie czestotliwosc z jaka ma sie poruszac wykres wzgledem osi x
pp1 = mpatches.PathPatch(
    Path([(153,-85),(152, -57), (218, -391),(138,-392)], ### podane punkty krzywej
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]), ### curve4 rysuje krzywa 4 punktowa
    fc="none", transform=ax.transData)
### kolejny pkt itd
pp2 = mpatches.PathPatch(
    Path([(138,-392),(123,-392),(422,-362),(422,-390)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp3 = mpatches.PathPatch(
    Path([(422,-390),(422,-405),(456,-324),(415,-323)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp4 = mpatches.PathPatch(
    Path([(415,-323),(400,-323),(225,-328),(234,-335)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp5 = mpatches.PathPatch(
    Path([(234,-335),(243,-342),(239,-234),(235,-245)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp6 = mpatches.PathPatch(
    Path([(235,-245),(231,-256),(412,-235),(413,-252)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp7 = mpatches.PathPatch(
    Path([(413,-252),(414,-266),(448,-181),(410,-182)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp8 = mpatches.PathPatch(
    Path([(410,-182),(386,-183),(236,-174),(236,-190)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp9 = mpatches.PathPatch(
    Path([(236,-190),(236,-205),(257,-133),(231,-134)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp10 = mpatches.PathPatch(
    Path([(231,-134),(216,-134),(414,-119),(417,-134)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp11 = mpatches.PathPatch(
    Path([(417,-134),(419,-144),(439,-64),(413,-76)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp12 = mpatches.PathPatch(
    Path([(413,-76),(398,-75),(187,-106),(153,-86)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)

### LITERA  K

pp13 = mpatches.PathPatch(
    Path([(553,-86),(487, -46), (531, -335),(520,-410)], ### podane punkty krzywej
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]), ### curve4 rysuje krzywa 4 punktowa
    fc="none", transform=ax.transData)
pp14 = mpatches.PathPatch(
    Path([(520,-410),(516,-437),(605,-420),(616,-409)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp15 = mpatches.PathPatch(
    Path([(616,-409),(627,-398),(624,-306),(613,-296)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp16 = mpatches.PathPatch(
    Path([(613,-296),(602,-286),(723,-402),(728,-420)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp17 = mpatches.PathPatch(
    Path([(728,-420),(732,-434),(835,-407),(832,-395)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp18 = mpatches.PathPatch(
    Path([(832,-395),(829,-382),(638,-228),(627,-238)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp19 = mpatches.PathPatch(
    Path([(627,-238),(616,-248),(787,-86),(790,-72)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp20 = mpatches.PathPatch(
    Path([(790,-72),(793,-57),(713,-61),(698,-79)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp21 = mpatches.PathPatch(
    Path([(698,-79),(679,-102),(595,-170),(595,-185)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp22 = mpatches.PathPatch(
    Path([(595,-185),(595,-200),(601,-92),(599,-85)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)
pp23 = mpatches.PathPatch(
    Path([(599,-85),(595,-71),(513,-69),(555,-86)],
         [Path.MOVETO,Path.CURVE4, Path.CURVE4,Path.CURVE4]),
    fc="none", transform=ax.transData)


### dodaje kolejne krzywe do wykresu
ax.add_patch(pp1)
ax.add_patch(pp2)
ax.add_patch(pp3)
ax.add_patch(pp4)
ax.add_patch(pp5)
ax.add_patch(pp6)
ax.add_patch(pp7)
ax.add_patch(pp8)
ax.add_patch(pp9)
ax.add_patch(pp10)
ax.add_patch(pp11)
ax.add_patch(pp12)
ax.add_patch(pp13)
ax.add_patch(pp14)
ax.add_patch(pp15)
ax.add_patch(pp16)
ax.add_patch(pp17)
ax.add_patch(pp18)
ax.add_patch(pp19)
ax.add_patch(pp20)
ax.add_patch(pp21)
ax.add_patch(pp22)
ax.add_patch(pp23)
ax.set_title('Krzywe Beziera')
plt.axis('equal')
plt.show()
