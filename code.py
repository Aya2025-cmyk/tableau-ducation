{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a5127124-9390-4eab-82a6-1b5be437e8f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-22 00:03:38.774 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 00:03:38.777 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 00:03:38.779 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 00:03:38.780 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 00:03:38.781 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 00:03:38.781 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 00:03:38.783 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 00:03:38.785 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 00:03:38.786 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 00:03:38.786 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "\n",
    "st.set_page_config(page_title=\"Tableau de bord éducatif\", layout=\"wide\")\n",
    "\n",
    "st.title(\"📊 Tableau de bord de l'éducation rurale au Sénégal\")\n",
    "\n",
    "# Upload du fichier CSV\n",
    "uploaded_file = st.file_uploader(\"Téléversez le fichier CSV des données scolaires\", type=[\"csv\"])\n",
    "\n",
    "if uploaded_file:\n",
    "    df = pd.read_csv(uploaded_file)\n",
    "\n",
    "    st.success(\"✅ Données chargées avec succès !\")\n",
    "\n",
    "    # Calculs de base\n",
    "    df[\"taux_abandon\"] = (df[\"inscrits\"] - df[\"presents\"]) / df[\"inscrits\"] * 100\n",
    "    df[\"taux_reussite\"] = df[\"admis\"] / df[\"presents\"] * 100\n",
    "\n",
    "    # Filtres\n",
    "    annee_select = st.selectbox(\"Sélectionnez l'année\", df[\"annee\"].unique())\n",
    "    df_filtré = df[df[\"annee\"] == annee_select]\n",
    "\n",
    "    # Graphique 1 : taux d'abandon par école\n",
    "    fig1 = px.bar(df_filtré, x=\"ecole\", y=\"taux_abandon\", color=\"village\", title=\"Taux d'abandon par école\")\n",
    "    st.plotly_chart(fig1, use_container_width=True)\n",
    "\n",
    "    # Graphique 2 : taux de réussite\n",
    "    fig2 = px.bar(df_filtré, x=\"ecole\", y=\"taux_reussite\", color=\"village\", title=\"Taux de réussite par école\")\n",
    "    st.plotly_chart(fig2, use_container_width=True)\n",
    "\n",
    "    # Affichage tableau\n",
    "    st.dataframe(df_filtré)\n",
    "\n",
    "else:\n",
    "    st.info(\"📥 Veuillez téléverser un fichier CSV pour commencer.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e3fd678-2ef3-44ba-a561-b96b754facfe",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
