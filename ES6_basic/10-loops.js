// export default (array, appendString) => array.map((value) => appendString + value);
export default function appendToEachArrayValue(array, appendString) {
  const arrayNew = [];
  for (const index of array) {
    arrayNew.push(appendString + index);
  }

  return arrayNew;
}
