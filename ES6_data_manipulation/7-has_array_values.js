function hasValuesFromArray(set, array) {
  for (const element of array) {
    if (!set.has(element)) {
      return false;
    }
  }
  return true;
}
export default hasValuesFromArray;
