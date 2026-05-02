# État actuel du projet NZ IT Services

## Résumé fonctionnel de l'ancienne version

Le site web de NZ IT Services est une page d'accueil monopage conçue pour promouvoir les services de l'entreprise en tant que partenaire IT spécialisé dans SAP, avec un modèle nearshore. Voici un résumé fonctionnel de ses principales caractéristiques et fonctionnalités :

### **Objectif principal**
- Présenter NZ IT Services comme un centre de livraison SAP (SAP Delivery Center) avec une approche nearshore alignée sur le fuseau horaire français.
- Attirer des clients potentiels en mettant en avant l'expertise, la stabilité et la proximité géographique (Paris - France et Oran - Algérie).

### **Structure et contenu**
Le site est organisé en sections séquentielles sur une seule page, avec un thème sombre (slate-950 à slate-900) et des animations fluides pour une expérience visuelle engageante :
- **En-tête/Héro** : Introduction avec le logo, slogan "VOTRE PARTENAIRE IT", et mise en avant du modèle nearshore. Inclut des particules animées flottantes et un arrière-plan avec effets de lumière (radial gradients en ambre et cyan).
- **À propos** : Description de l'entreprise fondée par un consultant SAP franco-algérien expérimenté (>8 ans), inspirée des standards des ESN françaises. Présente les bureaux et les valeurs clés (confiance et exigence).
- **Expertise SAP** : Mise en avant des modules principaux couverts : FI-CO (Finance & Contrôle), SD-MM (Vente et logistique), ABAP (Développement), EDI (Échanges de données). Chaque module est présenté dans une carte animée avec effets de survol.
- **Processus opérationnel** : Description de la démarche en trois étapes : Sourcing (recrutement de profils qualifiés), Validation (présentation des consultants), Intégration (intégration rapide en présentiel).
- **Localisation** : Carte stylisée montrant Paris (siège européen) et Oran (centre de delivery nearshore), avec des marqueurs colorés.
- **Valeurs** : Quatre piliers présentés en cartes : Stabilité (missions durables), Organisation (processus inspirés des ESN françaises), Expertise (consultants expérimentés), Confiance (relation transparente).

### **Fonctionnalités techniques**
- **Technologies** : Construit avec Astro (générateur de sites statiques) et Tailwind CSS pour le styling. Utilise des animations CSS personnalisées (fade-in, bounce, rotate, etc.) pour les effets visuels.
- **Design** : Thème sombre avec couleurs accentuées (ambre pour les éléments clés, cyan pour les compléments). Effets de hover sur les cartes (changement de couleur, échelle, ombres) pour l'interactivité.
- **Responsive** : Adapté aux mobiles et desktops via des grilles CSS (grid-cols pour les sections).
- **Performance** : Site statique léger, optimisé pour le chargement rapide, sans JavaScript dynamique apparent (hormis les animations CSS).
- **Accessibilité** : Langue française, titre de page "NZ IT Services", favicon, et structure sémantique HTML.

### **Limites et absence de fonctionnalités**
- **Pas de navigation** : Aucune barre de menu ou liens vers d'autres pages – c'est une landing page purement informative.
- **Pas de formulaires** : Aucun moyen de contact direct (pas de formulaire de contact, email, ou téléphone visible).
- **Pas de contenu dynamique** : Aucun blog, portfolio de projets, ou section témoignages.
- **Pas de multilinguisme** : Contenu exclusivement en français.

En résumé, ce site agit comme une vitrine professionnelle pour générer des leads, en se concentrant sur la présentation de l'offre de services SAP nearshore plutôt que sur des fonctionnalités interactives avancées. Il est optimisé pour une première impression visuelle forte et une lecture fluide.

## Plans de développement futur

Je souhaite développer ce site pour le rendre plus dynamique, innovant et beau à voir et à lire, en m'inspirant de sites comme https://www.iliadeconsulting.com/ et d'autres dans le domaine du consulting IT/SAP. L'objectif est de passer d'une simple landing page statique à un site web moderne et interactif qui renforce la crédibilité de NZ IT Services et facilite l'engagement des visiteurs.

### **Améliorations visuelles et UX**
- **Design moderne** : Adopter un design plus épuré et professionnel, avec des animations subtiles (comme des transitions fluides, des effets de parallax avancés, et des micro-interactions). S'inspirer des sites de consulting pour une esthétique premium (gradients sophistiqués, typographie élégante, espaces blancs optimisés).
- **Thème dynamique** : Ajouter un mode sombre/clair, et peut-être des variations de thème basées sur l'heure ou les préférences utilisateur.
- **Responsive avancé** : Optimiser pour tous les appareils, avec des layouts adaptatifs et des performances mobiles excellentes.

### **Nouvelles fonctionnalités**
- **Navigation multi-pages** : Créer une structure avec plusieurs pages (Accueil, À propos, Services/Offres, Contact, Nous rejoindre, etc.) avec une barre de navigation fixe et un menu hamburger pour mobile.
- **Section Contact** : Ajouter un formulaire de contact interactif (avec validation en temps réel, envoi d'emails via un service comme Netlify Forms ou un backend simple). Inclure des coordonnées, une carte interactive, et des liens vers LinkedIn/WhatsApp.
- **Offres/Services** : Page dédiée aux offres d'emploi ou de services, avec des descriptions détaillées, des filtres, et des appels à l'action (postuler, demander un devis).
- **À propos** : Développer la section avec une équipe, des témoignages clients, des études de cas, et une timeline de l'entreprise.
- **Nous rejoindre** : Section carrière avec offres d'emploi, processus de recrutement, et formulaire de candidature.
- **Changement de langue** : Ajouter un sélecteur de langue pour du contenu en français et anglais (voire arabe pour l'Algérie).
- **Contenu dynamique** : Intégrer un blog pour des articles sur SAP, des actualités de l'entreprise, et des ressources (guides, webinars).
- **Portfolio/Projets** : Montrer des projets passés avec des galeries d'images, des vidéos, et des métriques de succès.
- **Intégrations** : Ajouter des widgets pour les réseaux sociaux, un chatbot pour les questions fréquentes, et des intégrations avec des outils comme Calendly pour les rendez-vous.

### **Technologies et architecture**
- **Passer à un framework plus dynamique** : Garder Astro pour la performance, mais ajouter des îles (Astro Islands) pour du JavaScript interactif. Intégrer React/Vue pour les composants dynamiques si nécessaire.
- **Backend léger** : Utiliser des services serverless (Vercel/Netlify) pour les formulaires et les emails.
- **SEO et performance** : Optimiser pour les moteurs de recherche avec des métadonnées, des images lazy-loadées, et des scores Lighthouse élevés.
- **Accessibilité** : Améliorer l'accessibilité (ARIA, contrastes, navigation clavier).

### **Étapes de développement**
1. **Audit et planification** : Analyser les sites inspirants pour identifier les meilleures pratiques.
2. **Wireframes et design** : Créer des maquettes pour les nouvelles pages.
3. **Développement itératif** : Commencer par la navigation et les pages clés, puis ajouter les fonctionnalités une par une.
4. **Tests et déploiement** : Tester sur différents appareils, optimiser les performances, et déployer sur un CDN.

Ce développement transformera le site en une plateforme complète pour attirer des clients et des talents, tout en renforçant l'image innovante de NZ IT Services.