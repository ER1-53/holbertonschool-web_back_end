import hasValuesFromArray from './7-has_array_values';

function groceriesList() {
  const mySet = new Map();

  mySet.set('Apples', 10);
  mySet.set('Tomatoes', 10);
  mySet.set('Pasta', 1);
  mySet.set('Rice', 1);
  mySet.set('Banana', 5);
  return mySet;
}

export default groceriesList;
