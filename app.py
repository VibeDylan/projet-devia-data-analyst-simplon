import pandas as pd
import plotly.express as px

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv'
ventes = pd.read_csv(url, sep=None, engine='python') 
ventes = ventes[ventes['date'] != 'date']

ventes['chiffre_affaires'] = ventes['prix'] * ventes['qte'] # remove phantom line in CSV (for "date")

ventes_par_produit = ventes.groupby('produit', as_index=False)['qte'].sum().sort_values('qte', ascending=False)

fig1 = px.bar(
    ventes_par_produit,
    x='produit',
    y='qte',
    title='Ventes par produit (quantité)',
    text='qte'
)
fig1.write_html('ventes-par-produit.html', include_plotlyjs='cdn')
fig1.show()

ca_par_produit = ventes.groupby('produit', as_index=False)['chiffre_affaires'].sum().sort_values('chiffre_affaires', ascending=False)

fig2 = px.bar(
    ca_par_produit,
    x='produit',
    y='chiffre_affaires',
    title="Chiffre d'affaires par produit (€)",
    text='chiffre_affaires'
)
fig2.update_layout(yaxis_title="Chiffre d'affaires (€)")
fig2.write_html('ca-par-produit.html', include_plotlyjs='cdn')
fig2.show()

print("✅ Graphiques générés : 'ventes-par-produit.html' et 'ca-par-produit.html'")
