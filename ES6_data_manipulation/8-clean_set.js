function cleanSet(set, startString) {
  // Créer un tableau pour stocker les valeurs nettoyées
  const cleanedValues = [];

  // Parcourir chaque valeur dans l'ensemble
  if (startString) {
    for (const value of set) {
      // Vérifier si la valeur commence par la chaîne startString
      if (value.startsWith(startString)) {
        // Si oui, ajouter le reste de la chaîne (après startString) au tableau
        cleanedValues.push(value.slice(startString.length));
      }
    }

    return cleanedValues.join('-');
  }
  return '';
  // Joindre les valeurs nettoyées avec -
}

export default cleanSet;
