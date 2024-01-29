function updateUniqueItems(map) {
  for (const [key, value] of map) {
    if (value === 1) {
      map.set(key, 100);
    }
  }
  return map;
}

export default updateUniqueItems;
