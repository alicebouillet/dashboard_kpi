# Script vidéo — Dashboard NovaBank
**Public :** Jury académique
**Support :** Dashboard Streamlit (app.py)

---

## 🎬 INTRODUCTION
*(écran : page d'accueil du dashboard)*

« Bonjour, je vais vous présenter le dashboard que j'ai développé dans le cadre de l'étude de cas NovaBank.

L'objectif de ce projet était d'analyser une hausse alarmante du churn client — c'est-à-dire du taux de résiliation — et d'en identifier les causes pour aider la direction à prendre des décisions.

Le dashboard est construit avec Streamlit et organisé en 5 onglets que je vais vous parcourir. »

---

## 📊 ONGLET 1 — Vue d'ensemble
*(cliquer sur "Vue d'ensemble")*

« On commence par la vue d'ensemble, qui donne le constat principal en un coup d'œil.

Les 4 KPIs en haut résument la situation : le taux de churn a atteint 4 % en décembre, contre 2,1 % en juillet — soit pratiquement le double en 6 mois. Dans le même temps, le NPS est passé de 41 à 21, les incidents sur l'application mobile ont été multipliés par près de 4, et les plaintes ont quasiment doublé.

Le graphique du bas montre deux choses importantes : à gauche, le classement des segments par taux de churn — les nouveaux clients et les jeunes actifs sont les plus touchés. À droite, le classement par canal — l'application mobile ressort clairement comme le canal le plus problématique. »

---

## 📈 ONGLET 2 — Tendances mensuelles
*(cliquer sur "Tendances mensuelles")*

« Cet onglet permet d'explorer l'évolution mois par mois. J'ai ajouté un filtre de période pour que la direction puisse zoomer sur un intervalle précis.

Le premier graphique superpose le taux de churn et le nombre d'incidents applicatifs. On voit clairement que les deux courbes s'emballent à partir de septembre — ce n'est pas une coïncidence.

Le deuxième graphique montre que les plaintes ont triplé pendant que le temps d'attente au support a doublé. Quand l'app dysfonctionne, les clients appellent — et ils attendent de plus en plus longtemps, ce qui aggrave encore leur frustration.

Le troisième graphique illustre le paradoxe central de cette situation : le taux d'adoption digitale progresse régulièrement, pendant que la qualité de connexion mobile se dégrade. Plus les clients utilisent l'app, plus ils subissent les incidents. »

---

## 👥 ONGLET 3 — Analyse par segment
*(cliquer sur "Analyse par segment")*

« Ici on descend au niveau des segments. J'ai ajouté un filtre multi-sélection pour isoler les populations d'intérêt.

Le scatter en haut confirme la corrélation entre usage digital et churn : les segments les plus connectés — nouveaux clients à 96 % d'usage digital, jeunes actifs à 92 % — sont aussi ceux qui churne le plus. Ce n'est pas un problème de fidélité en général, c'est un problème d'expérience digitale.

En bas à gauche, le graphique montre que les nouveaux clients cumulent le NPS le plus bas — 17 — et le taux de réclamation le plus élevé — 8,4 %. Les deux métriques racontent la même histoire.

En bas à droite, on croise la valeur financière du client avec son churn. Les nouveaux clients sont en haut à gauche : ils partent beaucoup et ont le solde moyen le plus faible. C'est le segment le plus urgent à traiter. »

---

## 📱 ONGLET 4 — Canaux & services
*(cliquer sur "Canaux & services")*

« Cet onglet zoome sur les canaux de contact pour identifier d'où vient la défaillance.

Le graphique de gauche superpose trois signaux sur l'application mobile : le taux d'incident le plus élevé à 8,9 %, la satisfaction la plus basse à 2,8 sur 5, et le temps de résolution le plus long à 18 heures. Tous les voyants sont au rouge sur ce même canal.

Le graphique de droite confirme que l'app mobile génère à elle seule 44 % de tous les contacts clients — c'est le canal dominant — mais c'est aussi celui qui met le plus longtemps à résoudre les problèmes.

Le scatter en bas synthétise tout : plus un canal a d'incidents, plus son churn est élevé. L'application mobile est clairement hors norme sur les deux axes, et c'est le cercle le plus grand — ce qui signifie qu'il concentre aussi le plus grand volume de contacts. »

---

## ✅ ONGLET 5 — Recommandations & Décisions
*(cliquer sur "Recommandations & Décisions")*

« Le dernier onglet traduit l'analyse en décisions concrètes, structurées en trois horizons temporels.

En urgence — dans les 30 jours — deux actions prioritaires : un plan de crise technique sur l'application mobile avec un objectif de retour à 98 % de succès de connexion, et un programme de rétention ciblé sur les nouveaux clients, avec un contact proactif après chaque incident.

À moyen terme, trois chantiers complémentaires : réduire la pression sur le support, renforcer l'expérience des jeunes actifs, et refondre le chatbot qui contribue lui aussi à la friction.

Sur le long terme, deux actions de pilotage : intégrer le NPS et les incidents comme KPIs au comité de direction, et construire un modèle prédictif de churn pour anticiper les prochaines vagues.

La matrice en bas positionne ces 7 actions selon leur impact et leur effort. Les deux actions immédiates — corriger l'app et retenir les nouveaux clients — offrent le meilleur rapport impact/effort. C'est là qu'il faut commencer. »

---

## 🎬 CONCLUSION
*(revenir sur la vue d'ensemble)*

« Pour conclure : la hausse du churn chez NovaBank n'est pas un phénomène diffus — elle a une cause principale identifiable, qui est la dégradation de l'expérience digitale, et elle frappe des segments précis que l'on peut cibler.

Ce dashboard a été conçu pour permettre à la direction d'explorer ces données de façon autonome et de prioriser ses décisions. Merci. »
